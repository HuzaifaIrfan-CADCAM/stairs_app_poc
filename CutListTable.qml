// CutListTable.qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Column {
    id: root
    width: 600
    spacing: 5

    // Header
    Row {
        spacing: 1
        Rectangle {
            width: 150; height: 30; color: "#ddd"; border.color: "#999"
            Text { anchors.centerIn: parent; text: "Part"; font.bold: true }
        }
        Rectangle {
            width: 80; height: 30; color: "#ddd"; border.color: "#999"
            Text { anchors.centerIn: parent; text: "Qty"; font.bold: true }
        }
        Rectangle {
            width: 300; height: 30; color: "#ddd"; border.color: "#999"
            Text { anchors.centerIn: parent; text: "Dimensions"; font.bold: true }
        }
    }

    // Data rows
    ListView {
        width: 600
        height: 100
        model: ListModel {
            ListElement { part: "Treads"; qty: "6"; dimensions: "34 1/2'' x 10" }
            ListElement { part: "Risers"; qty: "7"; dimensions: "34 1/2'' x 7 1/2''" }
            ListElement { part: "Stringers"; qty: "2"; dimensions: "16 3/4'' x 139''" }
        }

        delegate: Row {
            spacing: 1
            Rectangle {
                width: 150; height: 30; color: "#fefefe"; border.color: "#ccc"
                Text { anchors.centerIn: parent; text: part }
            }
            Rectangle {
                width: 80; height: 30; color: "#fefefe"; border.color: "#ccc"
                Text { anchors.centerIn: parent; text: qty }
            }
            Rectangle {
                width: 300; height: 30; color: "#fefefe"; border.color: "#ccc"
                Text { anchors.centerIn: parent; text: dimensions }
            }
        }

        clip: true
    }
}
