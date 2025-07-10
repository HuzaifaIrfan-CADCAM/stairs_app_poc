# main.py
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication
import sys
import os
os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"

from pprint import pprint

from stair_calculator import auto_stair_calculator, stair_calculator

from pdf_tools import create_cut_list



from freecad_doc import FreecadDoc
from freecad_doc.stair_stringer import create_stair_stringer, create_job


from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QImage, QPainter, QPen
from PyQt6.QtCore import Qt, QByteArray, QBuffer
import base64



class Backend(QObject):
    cutListChanged = pyqtSignal(list)
    displayStair=pyqtSignal(float,float, float,int,int,float,float)

    message = pyqtSignal(str)

    imageReady = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    
    def generateStairImage(self, rise, run, steps, total_rise, total_run):
        # rise = 7.5
        # run = 10.5
        # steps = 8
        scale = 2

        width = int(run * steps * scale + 20)
        height = int(rise * steps * scale + 20)

        image = QImage(width, height, QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.white)

        painter = QPainter(image)
        pen = QPen(Qt.GlobalColor.black, 2)
        painter.setPen(pen)

        x, y = 10, height - 10

        # First riser
        next_y = y - rise * scale
        painter.drawLine(int(x), int(y), int(x), int(next_y))
        y = next_y

        for _ in range(steps):
            # Draw tread first (horizontal)
            next_x = x + run * scale
            painter.drawLine(int(x), int(y), int(next_x), int(y))  # tread

            x = next_x

            # Draw riser (vertical) — except skip after last tread
            next_y = y - rise * scale
            if _ != steps - 1:
                painter.drawLine(int(x), int(y), int(x), int(next_y))
                y = next_y

        floor_y = y
        painter.drawLine(int(x - run * scale), int(floor_y), int(x + 40), int(floor_y))

        painter.end()

        buffer = QBuffer()
        buffer.open(QBuffer.OpenModeFlag.ReadWrite)
        image.save(buffer, "PNG")

        byte_array: QByteArray = buffer.data()
        base64_data = base64.b64encode(byte_array.data()).decode("utf-8")
        data_url = f"data:image/png;base64,{base64_data}"

        self.imageReady.emit(data_url)

    @pyqtSlot(str, str, str, str)
    def calculate_stair(self, job_name, builder_name, stair_width, total_rise):
        print(job_name)
        print(builder_name)
        print(stair_width)
        print(total_rise)

        

        result = auto_stair_calculator(
            total_rise=float(total_rise),
            step_height=7.625,
            tread_thickness=1.0,
            tread_depth=11.5,
            mount_type="standard"
        )
        result["width_stair"] = float(stair_width)
        pprint(result)

        self.message.emit("Stair Calculated")


        cut_list_data = [
            ["Part", "Qty", "Material", "Dimension"],
            ["Treads", result["num_treads"], '1" Plywood', result["width_stair"]],
            ["Risers", result["num_steps_risers"], '3/8" Plywood', result["width_stair"]],
            ["Top Riser", "1", '5/8" Plywood', result["width_stair"]],
            ["Stringers", "2", 'LSL or 2x12', result["stringer_length"]],
        ]

        
        self.displayStair.emit(result["total_rise"], result["width_stair"],result["actual_step_riser_height"], result["num_steps_risers"], result["num_treads"], result["tread_depth"], result["total_run"] )

        print("displayStair")

        self.message.emit("Display Stairs")

        self.generateStairImage(rise=result["actual_step_riser_height"], run=result["tread_depth"], steps=result["num_steps_risers"],total_rise=result["total_rise"],total_run=result["total_run"])
        

        create_cut_list(output_folder= f"output/{job_name}/", job_name=job_name, builder_name=builder_name, total_rise=result["total_rise"], width=result["width_stair"],riser_height=result["actual_step_riser_height"], num_riser=result["num_steps_risers"], num_tread=result["num_treads"], tread_depth=result["tread_depth"], total_run=result["total_run"],cut_list_data=cut_list_data)

        self.message.emit("cut list pdf generated")


        cut_list = [
            { "part": "Treads", "qty": result["num_treads"], "dimensions": f'{result["width_stair"]}" x {result["tread_depth"]}"' },
            { "part": "Risers", "qty": result["num_steps_risers"], "dimensions": f'{result["width_stair"]}" x {result["actual_step_riser_height"]}"' },
            { "part": "Stringers", "qty": 2, "dimensions": f'16 3/4" x {result["stringer_length"]}"' }
        ]
        self.cutListChanged.emit(cut_list)

        self.message.emit("Display Cut list")


    @pyqtSlot(str, str, str, str)
    def export_gcode(self, job_name, builder_name, stair_width, total_rise):
        print(job_name)
        print(builder_name)
        print(stair_width)
        print(total_rise)

        result = auto_stair_calculator(
            total_rise=float(total_rise),
            step_height=7.625,
            tread_thickness=1.0,
            tread_depth=11.5,
            mount_type="standard"
        )
        result["width_stair"] = float(stair_width)
        pprint(result)

        current_directory = os.getcwd()
        print("Current Working Directory:", current_directory)
        output_folder=f"{current_directory}/output/{job_name}/"


        freecad_doc=FreecadDoc(doc_name=f"{job_name}_stair_stringer_cnc", output_folder=output_folder)

        doc=freecad_doc.doc
        
        stair_stringer_body=create_stair_stringer(doc, body_name="stair_stringer", stringer_thickness = 1.5, first_rise_height = result["first_step_riser_height"], rise_height = result["actual_step_riser_height"],num_rise = result["num_steps_risers"], run_depth = result["tread_depth"], num_run = result["num_treads"],  kicker=False, kicker_depth = 5.5, kicker_height = 1.5, stair_angle=result["stair_angle"], back_cut_increase=5, rotate_for_cnc=True)
        
        gcode=create_job(doc, stair_stringer_body)

        freecad_doc.save()
        freecad_doc.export_gcode(gcode)
        freecad_doc.export_body(stair_stringer_body)



app = QApplication(sys.argv)

engine = QQmlApplicationEngine()
backend = Backend()
engine.rootContext().setContextProperty("backend", backend)
engine.load(QUrl("ui.qml"))

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())
