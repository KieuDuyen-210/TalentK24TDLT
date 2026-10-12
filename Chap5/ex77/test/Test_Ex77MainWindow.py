from PyQt6.QtWidgets import QApplication, QMainWindow

from Chap5.ex77.ui.MainWindowEx import MainWindowEx

app=QApplication([])
myui=MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()