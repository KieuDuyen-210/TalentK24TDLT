n=10
sum = 0
for i in range (1, n+1):
    if i % 2 != 0:
        continue
    sum+=i
print ("sum:",sum)
#Cách 1
gpa=-1
while gpa < 0 or gpa > 10:
    gpa=int(input("Enter your GPA:"))
print("Your GPA is ",gpa)
#Cách 2
drl=-1
while True:
    drl = int (input("Enter your drl:"))
    if drl >= 0 and drl <= 100:
        break
print("Your DRL is ", drl)