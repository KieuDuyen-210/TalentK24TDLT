def calc_bmi(h,w):
    bmi=w/h**2
    type="Thin"
    risk="Low"
    if bmi<18:
        type="Thin"
        risk = "Low"
    elif 18.5<=bmi<=25:
        type="Normal"
        risk = "Normal"
    elif 25<=bmi<30:
        type="Slightly Fat"
        risk = "High"
    elif 30<=bmi<35:
        type="Obesity level 1"
        risk = "High"
    elif bmi <= 40:
        type = "Obesity level 2"
        risk = "Very High"
    else:
        type = "Obesity level 3"
        risk = "Danger"
    return bmi,type,risk
