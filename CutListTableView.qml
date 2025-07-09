// CutListTableView.qml
import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: root
    property alias model: tableRepeater.model

    width: 350
    height: 200

    Column {
        spacing: 2

        // Table Header
        Rectangle {
            width: parent.width
            height: 40
            color: "#dddddd"
            border.color: "#999"

            Row {
                anchors.fill: parent
                spacing: 1

                Rectangle {
                    width: 100; height: parent.height
                    color: "#dddddd"; border.color: "#999"
                    Text {
                        anchors.centerIn: parent
                        text: "Part"
                        font.bold: true
                    }
                }

                Rectangle {
                    width: 50; height: parent.height
                    color: "#dddddd"; border.color: "#999"
                    Text {
                        anchors.centerIn: parent
                        text: "Qty"
                        font.bold: true
                    }
                }

                Rectangle {
                    width: 200; height: parent.height
                    color: "#dddddd"; border.color: "#999"
                    Text {
                        anchors.centerIn: parent
                        text: "Dimensions"
                        font.bold: true
                    }
                }
            }
        }

        // Data Rows
        Repeater {
            id: tableRepeater
            delegate: Rectangle {
                width: parent.width
                height: 35
                color: index % 2 === 0 ? "#f9f9f9" : "#ffffff"
                border.color: "#ccc"

                Row {
                    anchors.fill: parent
                    spacing: 1

                    Rectangle {
                        width: 100; height: parent.height
                        color: "transparent"; border.color: "#ccc"
                        Text {
                            anchors.centerIn: parent
                            text: model.part
                        }
                    }

                    Rectangle {
                        width: 50; height: parent.height
                        color: "transparent"; border.color: "#ccc"
                        Text {
                            anchors.centerIn: parent
                            text: model.qty
                        }
                    }

                    Rectangle {
                        width: 200; height: parent.height
                        color: "transparent"; border.color: "#ccc"
                        Text {
                            anchors.centerIn: parent
                            text: model.dimensions
                        }
                    }
                }
            }
        }
    }
}
