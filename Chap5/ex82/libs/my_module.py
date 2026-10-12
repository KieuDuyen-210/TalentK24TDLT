#chianhomkhachhang
def customergroup(group, numofkwh):
    if group == 1:
        if numofkwh<=50:
            return 'level1'
        elif numofkwh<=100:
            return 'level2'
        elif numofkwh<=200:
            return 'level3'
        elif numofkwh<=300:
            return 'level4'
        elif numofkwh<=400:
            return 'level5'
        else:
            return 'level6'
    else:
        return group == 2

#Tinhtongtiendien
def calculatebills(group, numofkwh):
    if group == 1:
        if group == 'level1':
            bill=numofkwh * 1.549
        elif group == 'level2':
            bill=numofkwh * 1.600
        elif group == 'level3':
            bill=numofkwh + 1.858
        elif group == 'level4':
            bill=numofkwh * 2.340
        elif group == 'level5':
            bill=numofkwh * 2.615
        else:
            bill=numofkwh * 2.701
    else:
        bill=numofkwh * 2.271
    return bill