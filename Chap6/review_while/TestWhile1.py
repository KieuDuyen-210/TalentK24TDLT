"""
enter a Gpa within [0..10]
if user does not enter a valid GPA
then user has to repeat their task
"""
while True:
    name=input("enter Student name:")
    gpa=-1
    while gpa<0 or gpa>10:
        gpa=float(input("enter a GPA [0..10]:"))
    print (f"GPA of [{name}]={gpa}")
    ask=input("Do you want to continue? [y/n]")
    if ask=="n":
        break