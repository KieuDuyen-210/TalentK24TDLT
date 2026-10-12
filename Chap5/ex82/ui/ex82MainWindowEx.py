from Chap5.ex82.libs.my_module import calculatebills
from Chap5.ex82.ui.ex82MainWindow import Ui_MainWindow


class ex82MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_calc.clicked.connect(self.calc_bill)

    def calc_bill(self):
        group=int(self.groupLineEdit.text())
        numofkwh=float(self.umberOfKWhUsedLineEdit.text())

        bill=calculatebills(group, numofkwh)

        self.theUtilityBillLineEdit.setText(f"{bill} VND")
