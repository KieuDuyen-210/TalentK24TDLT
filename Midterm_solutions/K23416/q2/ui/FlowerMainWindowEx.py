from Midterm_solutions.K23416.q2.ui.FlowerMainWindow import Ui_MainWindow
from Midterm_solutions.K23416.q2.libs.FlowerPricing import calculate_dalat_value, calculate_sapa_value


class FlowerMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()

    def show(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_buy.clicked.connect(self.process_buy)
        self.pushButton_clear.clicked.connect(self.process_clear)

    def process_clear(self):
        self.checkBox_dalatflower.setChecked(False)
        self.checkBox_sapaflower.setChecked(False)

    def process_buy(self):
        dalat_sold = 0
        dalat_value = 0
        sapa_sold = 0
        sapa_value = 0

        if self.checkBox_dalatflower.isChecked():
            dalat_num_str = self.lineEdit_dalatnum.text()
            if dalat_num_str.isdigit():
                dalat_sold = int(dalat_num_str)
                dalat_value = calculate_dalat_value(dalat_sold)
        
        if self.checkBox_sapaflower.isChecked():
            sapa_num_str = self.lineEdit_sapanum.text()
            if sapa_num_str.isdigit():
                sapa_sold = int(sapa_num_str)
                sapa_value = calculate_sapa_value(sapa_sold)

        total_revenue = dalat_value + sapa_value

        self.dalatFlowerSoldLineEdit.setText(str(dalat_sold))
        self.dalatvalueLineEdit.setText(f"{int(dalat_value):,} VND")
        self.sapaFlowerSoldLineEdit.setText(str(sapa_sold))
        self.sapavalueLineEdit_2.setText(f"{int(sapa_value):,} VND")
        self.totalRevenueLineEdit.setText(f"{int(total_revenue):,} VND")
