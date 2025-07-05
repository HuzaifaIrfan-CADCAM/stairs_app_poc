import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Window 2.15

// Import your table QML component
import "."  // assumes CutListTable.qml is in the same directory

ApplicationWindow {
    visible: true
    width: 1000
    height: 600
    title: "Treads by Design"

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
                }

                TextField {
                    Layout.fillWidth: true

                    placeholderText: "Builder Name"
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
                        model: ["Straight", "Curved"]
                        currentIndex: 0
                        Layout.fillWidth: true
                        editable: false
                    }
                }

                RowLayout {
                    spacing: 10
                    Label {
                        text: "Stringer Type"
                    }
                    Switch {
                        checked: true
                    }
                }

                ColumnLayout {
                    spacing: 2
                    Label {
                        text: "Material"
                    }
                    ComboBox {
                        model: ["SSL", "PT", "MS"]
                        Layout.fillWidth: true
                    }
                }

                RowLayout {
                    spacing: 10
                    Label {
                        text: "Stair Width"
                    }
                    TextField {
                        Layout.fillWidth: true

                        placeholderText: "44.5"
                        width: 80
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
                    }
                    Label {
                        text: "in"
                    }
                }

                RowLayout {

                    anchors.horizontalCenter: parent.horizontalCenter
                    spacing: 10
                    Button {
                        text: "Generate PDF"
                    }
                    Button {
                        text: "Export DCode"
                    }
                }
                RowLayout {
                    anchors.horizontalCenter: parent.horizontalCenter
                    spacing: 10
                    Button {
                        text: "Save Job"
                    }
                    Button {
                        text: "Duplicate Job"
                    }
                }
            }

            // === Right Panel ===
            ColumnLayout {
                spacing: 20
                Layout.fillWidth: true

                Rectangle {
                    width: 600
                    height: 250
                    color: "#f5f5f5"
                    border.color: "gray"
                    radius: 5
                    Text {
                        anchors.centerIn: parent
                        text: "Stair Drawing"
                        color: "#888"
                        font.pixelSize: 18
                    }
                }

                // Cut List Table
                ColumnLayout {
                    spacing: 5

                    Label {
                        text: "Cut List"
                        font.bold: true
                        font.pixelSize: 16
                    }

                    CutListTable {}
                }
            }
        }
    }
}
