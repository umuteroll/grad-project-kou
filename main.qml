import QtQuick
import QtQuick.Controls.Basic
ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "HelloApp"
    Text {
        horizontalAlignment: Text.AlignTop
        text: "Hello World"
        font.pixelSize: 24
    }
    TextInput {
        horizontalAlignment: TextInput.AlignHCenter
        text: "Hello World"
        font.pixelSize: 24
    }
    Button {

  signal messageRequired
  objectName: "myButton"
  text : "About"
  onClicked: messageRequired()

 }
}