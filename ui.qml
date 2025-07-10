import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Window 2.15

// Import your table QML component
import "."  // assumes CutListTable.qml is in the same directory

ApplicationWindow {
    id: root
    visible: true
    width: 1000
    height: 600
    title: "Treads by Design"

    property string stairImageData: ""

    ListModel {
        id: cutListModel
        ListElement {
            part: "Treads"
            qty: 0
            dimensions: "34 1/2'' x 10"
        }
        ListElement {
            part: "Risers"
            qty: 0
            dimensions: "34 1/2'' x 7 1/2''"
        }
        ListElement {
            part: "Stringers"
            qty: 0
            dimensions: "16 3/4'' x 139''"
        }
    }

    function setCutList(list) {
        cutListModel.clear()
        for (var i = 0; i < list.length; i++) {
            cutListModel.append(list[i])
        }
    }


    Item {
        anchors.fill: parent

        RowLayout {
            anchors.fill: parent
            anchors.margins: 20

            // === Left Panel: Input Form ===
            ColumnLayout {
                spacing: 10
                width: 300

                Label {
                    text: "Treads by Design"
                    font.bold: true
                    font.pixelSize: 20
                }

                TextField {
                    Layout.fillWidth: true

                    placeholderText: "Job Name"
                    text:"Crestmont"
                    id: job_name
                }

                TextField {
                    Layout.fillWidth: true

                    placeholderText: "Builder Name"

                    text:"Smith Builders"
                    id: builder_name
                }

                ColumnLayout {
                    spacing: 2
                    Label {
                        text: "Stair Type"
                    }
                    ComboBox {
                        model: ["Straight", "L-shaped", "U-shaped"]
                        currentIndex: 0
                        Layout.fillWidth: true
                        editable: false
                    }
                }

                ColumnLayout {
                    spacing: 2
                    Label {
                        text: "Nosing"
                    }
                    ComboBox {
                        model: ["None", "Straight", "Curved"]
                        currentIndex: 0
                        Layout.fillWidth: true
                        editable: false
                    }
                }

                // RowLayout {
                //     spacing: 10
                //     Label {
                //         text: "Stringer Type"
                //     }
                //     Switch {
                //         checked: true
                //     }
                // }

                // ColumnLayout {
                //     spacing: 2
                //     Label {
                //         text: "Material"
                //     }
                //     ComboBox {
                //         model: ["SSL", "PT", "MS"]
                //         Layout.fillWidth: true
                //     }
                // }

                RowLayout {
                    spacing: 10
                    Label {
                        text: "Stair Width"
                    }
                    TextField {
                        Layout.fillWidth: true

                        placeholderText: "44.5"
                        text:"36.75"
                        width: 80
                        id: stair_width
                    }
                    Label {
                        text: "in"
                    }
                }

                RowLayout {
                    spacing: 10
                    Label {
                        text: "Total Rise"
                    }
                    TextField {
                        Layout.fillWidth: true

                        placeholderText: "Enter height"
                        width: 100
                        text:"122"
                        id: total_rise
                    }
                    Label {
                        text: "in"
                    }
                }

                RowLayout {
                    Layout.alignment: Qt.AlignHCenter

                    spacing: 10
                    Button {
                        text: "Calculate"
                        onClicked: backend.calculate_stair(job_name.text, builder_name.text, stair_width.text, total_rise.text)
                    }
                    Button {
                        text: "Export G-Code"
                        onClicked: backend.export_gcode(job_name.text, builder_name.text, stair_width.text, total_rise.text)
                    }
                }
                RowLayout {
                    Layout.alignment: Qt.AlignHCenter

                    spacing: 10
                    Button {
                        text: "Save Job"
                        onClicked: backend.save_job()
                    }
                    Button {
                        text: "Duplicate Job"
                        onClicked: backend.duplicate_job()
                    }
                }
            }

            // === Right Panel ===
            ColumnLayout {
                spacing: 20
                Layout.fillWidth: true

                // Rectangle {
                //     width: 600
                //     height: 250
                //     color: "#f5f5f5"
                //     border.color: "gray"
                //     radius: 5
                //     Text {
                //         anchors.centerIn: parent
                //         text: "Stair Drawing"
                //         color: "#888"
                //         font.pixelSize: 18
                //     }
                // }


                    Image {
        id: stairImage
        source: stairImageData
        fillMode: Image.PreserveAspectFit
        asynchronous: true
        

        // Fill width of layout
        // Layout.fillWidth: true
        width: 10//parent.width

        // Maintain aspect ratio
        // Set height proportionally if you want:
        // height: width * (originalHeight / originalWidth)
        // Or let PreserveAspectFit handle it automatically
    }

                RowLayout {
                    spacing: 10

                    Label {
                        text: "Total Rise"
                    }
                    Label {
                        text:""
                        id: total_rise_label
                    }
                    Label {
                        text: "in "
                    }
                    
                    Label {
                        text: " Total Run"
                    }
                    Label {
                        text:""
                        id: total_run_label
                    }
                    Label {
                        text: "in "
                    }

                    Label {
                        text: " Stair Width"
                    }
                    Label {
                        text:""
                        id: stair_width_label
                    }
                    Label {
                        text: "in "
                    }
                }

                RowLayout {
                    spacing: 10
                    Label {
                        text: "Num Steps"
                    }
                    Label {
                        text:""
                        id: num_risers_label
                    }


                    Label {
                        text: "Num Tread"
                    }
                    Label {
                        text:""
                        id: num_tread_label
                    }

                }

                               RowLayout {
                    spacing: 10

                    Label {
                        text: "Riser Height"
                    }
                    Label {
                        text:""
                        id: risers_height_label
                    }
                    Label {
                        text: "in "
                    }
                    
                    Label {
                        text: " Tread Depth"
                    }
                    Label {
                        text:""
                        id: tread_depth_label
                    }
                    Label {
                        text: "in "
                    }

                               }

                // Cut List Table
                ColumnLayout {

                    Layout.fillHeight: true
                    spacing: 10

                    Label {
                        text: "Cut List"
                        font.bold: true
                        font.pixelSize: 16
                    }

                    CutListTableView {
                        model: cutListModel
                    }
                }
            }
        }
    }


    Connections {
        target: backend

        function onMessage(msg) {
            console.log( msg)
        }

        function onDisplayStair(
            total_rise, width_stair, actual_step_riser_height,
            num_steps_risers, num_treads, tread_depth, total_run
        ) {
            console.log("✅ Signal received!")
            console.log("  total_rise:", total_rise)
            console.log("  width_stair:", width_stair)
            console.log("  actual_step_riser_height:", actual_step_riser_height)
            console.log("  num_steps_risers:", num_steps_risers)
            console.log("  num_treads:", num_treads)
            console.log("  tread_depth:", tread_depth)
            console.log("  total_run:", total_run)
            total_rise_label.text=total_rise
            total_run_label.text=total_run
            stair_width_label.text=width_stair

            num_risers_label.text=num_steps_risers
            risers_height_label.text=actual_step_riser_height

            num_tread_label.text=num_treads
            tread_depth_label.text=tread_depth

        }
        function onCutListChanged(list) {
            root.setCutList(list)
            setCutList(list)
        }

        function onImageReady(base64Data) {
            root.stairImageData = base64Data
            console.log("✅ Image received and updated.")
        }
        
    }

}
