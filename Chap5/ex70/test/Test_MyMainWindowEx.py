from PyQt6.QtWidgets import QMainWindow, QApplication

from Chap5.ex70.ui.MyMainWindowEx import MyMainWindowEx

app=QApplication([])
myui=MyMainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()