from PyQt6.QtWidgets import QApplication, QMainWindow

from Chap5.ex80.ui.ex80MainWindowEx import ex80MainWindowEx

app=QApplication([])
myui=ex80MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()