// CutListTableView.qml
import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: root
    property alias model: repeater.model

    width: 350
    height: 240

    Column {
        anchors.fill: parent
        spacing: 0

        // ✅ Table header
        Row {
            width: root.width
            height: 40

            Rectangle {
                width: 100; height: parent.height
                color: "#cccccc"; border.color: "black"
                Text {
                    anchors.centerIn: parent
                    text: "Part"
                    font.bold: true
                }
            }

            Rectangle {
                width: 50; height: parent.height
                color: "#cccccc"; border.color: "black"
                Text {
                    anchors.centerIn: parent
                    text: "Qty"
                    font.bold: true
                }
            }

            Rectangle {
                width: 200; height: parent.height
                color: "#cccccc"; border.color: "black"
                Text {
                    anchors.centerIn: parent
                    text: "Dimensions"
                    font.bold: true
                }
            }
        }

        // ✅ Repeated rows below header
        Repeater {
            id: repeater

            delegate: Row {
                width: root.width
                height: 35

                Rectangle {
                    width: 100; height: parent.height
                    color: index % 2 === 0 ? "#f9f9f9" : "#ffffff"
                    border.color: "#999"
                    Text {
                        anchors.centerIn: parent
                        text: model.part
                    }
                }

                Rectangle {
                    width: 50; height: parent.height
                    color: index % 2 === 0 ? "#f9f9f9" : "#ffffff"
                    border.color: "#999"
                    Text {
                        anchors.centerIn: parent
                        text: model.qty
                    }
                }

                Rectangle {
                    width: 200; height: parent.height
                    color: index % 2 === 0 ? "#f9f9f9" : "#ffffff"
                    border.color: "#999"
                    Text {
                        anchors.centerIn: parent
                        text: model.dimensions
                    }
                }
            }
        }
    }
}
