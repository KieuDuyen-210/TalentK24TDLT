from PyQt6.QtWidgets import QApplication, QMainWindow

from Chap5.ex82.ui.ex82MainWindowEx import ex82MainWindowEx

app=QApplication([])
myui=ex82MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()