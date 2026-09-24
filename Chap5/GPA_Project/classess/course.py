class Course:
    def __init__(self,
                 qt=None,qtpercent=0.225,
                 gk=0,gkpercent=0.15,
                 ck=0,ckpercent=0.375,
                 talent=0,talentpercent=0.25):
        self.qt=qt
        self.qtpercent=qtpercent
        self.gk=gk
        self.gkpercent=gkpercent
        self.ck=ck
        self.ckpercent=ckpercent
        self.talent=talent
        self.talentpercent=talentpercent

    def cal_GPA(self):
        gpa = (self.qt * self.qtpercent +
               self.gk * self.gkpercent +
               self.ck * self.ckpercent +
               self.talent * self.talentpercent)
        return gpa