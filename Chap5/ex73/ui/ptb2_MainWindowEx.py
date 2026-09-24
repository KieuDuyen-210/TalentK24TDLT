from Chap5.ex73.libs.my_module import quadratic_solver
from Chap5.ex73.ui.ptb2_MainWindow import Ui_MainWindow


class ptb2_MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.solver)

    def solver(self):
        a=float(self.aLineEdit.text())
        b=float(self.bLineEdit.text())
        c=float(self.cLineEdit.text())
        result=quadratic_solver(a,b,c)
        self.solutionLineEdit.setText(result)