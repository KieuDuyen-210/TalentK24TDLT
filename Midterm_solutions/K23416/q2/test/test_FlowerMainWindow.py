from PyQt6.QtWidgets import QApplication, QMainWindow

from Midterm_solutions.K23416.q2.ui.FlowerMainWindowEx import FlowerMainWindowEx

app=QApplication([])
myWindow= FlowerMainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()