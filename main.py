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



class Backend(QObject):
    cutListChanged = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def sendCutList(self):
        cut_list = [
            { "part": "Treads", "qty": "6", "dimensions": "34 1/2'' x 10" },
            { "part": "Risers", "qty": "7", "dimensions": "34 1/2'' x 7 1/2''" },
            { "part": "Stringers", "qty": "2", "dimensions": "16 3/4'' x 139''" }
        ]
        self.cutListChanged.emit(cut_list)


    @pyqtSlot(str, str, str, str)
    def generate_pdf(self, job_name, builder_name, stair_width, total_rise):
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


        cut_list_data = [
            ["Part", "Qty", "Material", "Dimension"],
            ["Treads", result["num_treads"], '1" Plywood', result["width_stair"]],
            ["Risers", result["num_steps_risers"], '3/8" Plywood', result["width_stair"]],
            ["Top Riser", "1", '5/8" Plywood', result["width_stair"]],
            ["Stringers", "2", 'LSL or 2x12', result["stringer_length"]],
        ]

        create_cut_list(output_folder= "output/", job_name=job_name, builder_name=builder_name, total_rise=result["total_rise"], width=result["width_stair"],riser_height=result["actual_step_riser_height"], num_riser=result["num_steps_risers"], num_tread=result["num_treads"], tread_depth=result["tread_depth"], total_run=result["total_run"],cut_list_data=cut_list_data)

        
        self.sendCutList()

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


        freecad_doc=FreecadDoc(doc_name=f"{job_name}_stair_stringer_cnc")

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
