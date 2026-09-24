from PyQt6.QtWidgets import QMainWindow, QApplication

from Chap5.GPA_Project.ui.GPAMainWindowEx import GPAMainWindowEx

app=QApplication([])
gpa_ui=GPAMainWindowEx()
gpa_ui.setupUi(QMainWindow())
gpa_ui.show_window()
app.exec()