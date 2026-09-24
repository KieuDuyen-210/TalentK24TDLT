from PyQt6.QtWidgets import QApplication, QMainWindow

from Chap5.ex73.ui.ptb2_MainWindowEx import ptb2_MainWindowEx

app=QApplication([])
myui=ptb2_MainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()