from PyQt6.QtWidgets import QMessageBox

from homework.ex109.ex109 import calculate_original_price, calculate_annual_depreciation, \
    calculate_monthly_depreciation, get_depreciation_display_lines
from homework.ex130.ui.Ex130MainWindow import Ui_MainWindow


class Ex130MainWindowEx(Ui_MainWindow):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.setupSignalAndSlot()

    def show(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonTinhKhauHao.clicked.connect(self.process_tinh_khau_hao)
        self.pushButtonXemChiTiet.clicked.connect(self.process_xem_chi_tiet)

    def process_tinh_khau_hao(self):
        try:
            purchase_price = float(self.lineEditGiaMuaMoi.text())
            if purchase_price < 0:
                raise ValueError
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi")
            msg.setText("Giá mua mới phải là số không âm!")
            msg.exec()
            return False

        try:
            shipping_fee_str = self.lineEditPhiVanChuyen.text().strip()
            shipping_fee = float(shipping_fee_str) if shipping_fee_str else 0.0
            if shipping_fee < 0:
                raise ValueError
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi")
            msg.setText("Phí vận chuyển phải là số không âm (nhập 0 nếu không có)!")
            msg.exec()
            return False

        try:
            installation_fee_str = self.lineEditPhiLapDat.text().strip()
            installation_fee = float(installation_fee_str) if installation_fee_str else 0.0
            if installation_fee < 0:
                raise ValueError
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi")
            msg.setText("Phí lắp đặt phải là số không âm (nhập 0 nếu không có)!")
            msg.exec()
            return False

        try:
            years = int(self.lineEditSoNam.text())
            if years <= 0:
                raise ValueError
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Lỗi")
            msg.setText("Số năm sử dụng dự kiến phải là số nguyên lớn hơn 0!")
            msg.exec()
            return False

        original_price = calculate_original_price(purchase_price, shipping_fee, installation_fee)
        annual_depreciation = calculate_annual_depreciation(original_price, years)
        monthly_depreciation = calculate_monthly_depreciation(annual_depreciation)

        self.lineEditNguyenGia.setText(str(int(round(original_price))))
        self.lineEditKhauHaoNam.setText(str(int(round(annual_depreciation))))
        self.lineEditKhauHaoThang.setText(str(int(round(monthly_depreciation))))
        return True

    def process_xem_chi_tiet(self):
        if not self.process_tinh_khau_hao():
            return

        purchase_price = float(self.lineEditGiaMuaMoi.text())
        shipping_fee_str = self.lineEditPhiVanChuyen.text().strip()
        shipping_fee = float(shipping_fee_str) if shipping_fee_str else 0.0
        installation_fee_str = self.lineEditPhiLapDat.text().strip()
        installation_fee = float(installation_fee_str) if installation_fee_str else 0.0
        years = int(self.lineEditSoNam.text())

        original_price = calculate_original_price(purchase_price, shipping_fee, installation_fee)
        display_lines = get_depreciation_display_lines(original_price, years)

        self.plainTextEditChiTiet.setPlainText("\n".join(display_lines))
