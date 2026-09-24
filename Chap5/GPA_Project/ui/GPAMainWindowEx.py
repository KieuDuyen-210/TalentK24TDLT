from Chap5.GPA_Project.classess.course import Course
from Chap5.GPA_Project.ui.GPAMainWindow import Ui_MainWindow


class GPAMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_calcgpa.clicked.connect(self.invoke_gpa)
    def invoke_gpa(self):
        qt=float(self.lineEdit_qt.text())
        gk = float(self.lineEdit_gk.text())
        ck = float(self.lineEdit_ck.text())
        talent = float(self.lineEdit_talent.text())
        qt_percent = float(self.lineEdit_qtpercent.text()) / 100
        gk_percent = float(self.lineEdit_gkpercent.text()) / 100
        ck_percent = float(self.lineEdit_ckpercent.text()) / 100
        talent_percent = float(self.lineEdit_talentpercent.text()) / 100
        c = Course(
            qt, qtpercent=qt_percent,
            gk=gk, gkpercent=gk_percent,
            ck=ck, ckpercent=ck_percent,
            talent=talent, talentpercent=talent_percent)
        gpa=c.cal_GPA()
        self.lineEdit_9.setText(str(gpa))