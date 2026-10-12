from PyQt6.QtWidgets import QMessageBox

from Chap5.ex80.libs.my_module import calc_bmi
from Chap5.ex80.ui.ex80MainWindow import Ui_MainWindow


class ex80MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_BMI.clicked.connect(self.process_bmi)
        self.pushButton_exit.clicked.connect(self.call_close_app)

    def process_bmi(self):
        try:
            h = float(self.heightLineEdit.text())
            w = float(self.weightLineEdit.text())

            bmi, type, risk = calc_bmi(h, w)

            self.bMIValueLineEdit.setText(str(bmi))
            self.classificationLineEdit.setText(type)
            self.riskOfDiseaseLineEdit.setText(risk)

        except ValueError:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Lỗi dữ liệu")
            msgBox.setText("Lỗi nhập dữ liệu. "
                           "Chiều cao và cân nặng phải là số hợp lệ! Vui lòng kiểm tra lại.")
            msgBox.setIcon(QMessageBox.Icon.Critical)
            ret = msgBox.exec()

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