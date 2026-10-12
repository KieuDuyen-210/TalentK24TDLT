from PyQt6.QtWidgets import QMessageBox

from Chap5.ex77.libs.my_module import do_math
from Chap5.ex77.ui.MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_calculate.clicked.connect(self.call_math_operation)
        self.pushButton_exit.clicked.connect(self.call_close_app)

    def call_math_operation(self):
        a = float(self.lineEdit_soa.text())
        b = float(self.lineEdit_sob.text())
        op=""
        if self.radioButton_cong.isChecked():
            op="+"
        elif self.radioButton_tru.isChecked():
            op="-"
        elif self.radioButton_nhan.isChecked():
            op="*"
        elif self.radioButton_chia.isChecked():
            op="/"
        result=do_math(a,b,op)
        self.label_result.setText(str(result))

    def call_close_app(self):
        msgBox=QMessageBox()
        msgBox.setWindowTitle("Xác nhận thoát")
        msgBox.setText("Muốn thoát hả?")
        msgBox.setIcon(QMessageBox.Icon.Question)
        buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)
        ret=msgBox.exec()
        if ret == QMessageBox.StandardButton.Yes:
            exit(0)
