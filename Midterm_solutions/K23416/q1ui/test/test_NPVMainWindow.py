from PyQt6.QtWidgets import QApplication, QMainWindow

from Midterm_solutions.K23416.q1ui.ui.NPVMainWindowEx import NPVMainWindowEx

app=QApplication([])
myWindow= NPVMainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()