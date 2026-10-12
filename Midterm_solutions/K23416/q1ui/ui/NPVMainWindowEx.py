from Midterm_solutions.K23416.Q1 import calc_NPV, is_investment
from Midterm_solutions.K23416.q1ui.ui.NPVMainWindow import Ui_MainWindow

class NPVMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()

    def show(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_calcnpv.clicked.connect(self.process_NPV)

    def process_NPV(self):
        c0=float(self.initialInvestmentCostsLineEdit.text())
        ct=float(self.netCashFlowAtTimeTCtLineEdit.text())
        r=float(self.requiredRateRLineEdit.text())/100
        T=int(self.projectImplementationTimeTLineEdit.text())
        NPV=calc_NPV(c0,ct,r,T)
        result=is_investment(NPV)
        self.nPVLineEdit.setText(str(NPV))
        self.resultLineEdit.setText(result)