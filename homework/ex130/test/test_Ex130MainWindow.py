from PyQt6.QtWidgets import QApplication, QMainWindow

try:
    from ex130.ui.Ex130MainWindowEx import Ex130MainWindowEx
except ImportError:
    from homework.ex130.ui.Ex130MainWindowEx import Ex130MainWindowEx

app = QApplication([])
myWindow = Ex130MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()