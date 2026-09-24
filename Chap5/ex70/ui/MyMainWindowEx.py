from Chap5.ex70.libs.my_module import get_number_of_days
from Chap5.ex70.ui.MyMainWindow import Ui_MainWindow


class MyMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.count_days)

    def count_days(self):
        year=int(self.yearLineEdit.text())
        month=int(self.monthLineEdit.text())
        day=get_number_of_days(year,month)
        self.resultLineEdit.setText(str(day))
