blist=['Americano','Café Latte','Cappuccino','Oranges ','Colacola','Grapefruit']
plist=[2500,3000,3000,4000,1500,4000]
blistUserChoose=[]#the index of food name that user selected
plistUserChoose=[]#the quantity of food name that user selected
#print the menu for food/drink
print("No.","Food Name\tPrice")
for i in range(len(blist)):
    print(i+1,'.',blist[i],'\t',plist[i])
print("Please tell me the drink you ordered.")
while True:#the loop for choosing menu food/drink from menu
    noFoodName=0
    # User has to choose from 1->n
    while noFoodName<=0 or noFoodName > len(blist):
        strnoFoodName=input("Please choose the food name(enter number)[{}-{}]:"
                            .format(1,len(blist)))
        # If the value is a digit, we convert to int
        if strnoFoodName.isdigit():
            noFoodName=int(strnoFoodName)
        else:
            noFoodName=0#reset 0 if the user input
    blistUserChoose.append(noFoodName)
    noQuantity=0
    while noQuantity<=0:#quantity must >0
        strnoQuantity = input("Please enter quantity[>0]:")
        if strnoQuantity.isdigit():
            noQuantity=int(strnoQuantity)
        else:
            noQuantity=0
    plistUserChoose.append(noQuantity)
    # confirm continue or not
    question=input("Do you want to choose another food?(yes/no):")
    # if no, finish choosing the food/drink
    if question=='no':
        break
print("The list of ordered food/drink:")
sum = 0
print("Food Name\tPrice\tQuantity\tMoney")
#the loop to print all food/drink that user has chosen
for i in range(len(blistUserChoose)):
    # get the food name from user's choosing
    foodName=blist[blistUserChoose[i]-1]
    # get quantity that user bought
    quantity=plistUserChoose[i]
    # get the unit price for food/drink
    unitPrice=plist[blistUserChoose[i]-1]
    # calculate money for each food/drink
    money=quantity*unitPrice
    # sum every food/drink
    sum=sum+money
    # print detail information for each item
    print(foodName,"\t",unitPrice,"\t",quantity,"\t\t\t",money)
print("\tThe total amount is:\t",sum," money ")
money=0
while True:#loop for user to pay money
    strmoney=input("Enter the amount to be paid >>")
    if strmoney.isdigit()==False:
        print(strmoney," is not valid, it should be a digit numer ")
    else:
        money=int(strmoney)
        if money<0:
            print(strmoney, " is not valid number, it should be positive")
        else:
            if money < sum:
                print("Not enough money., you have to pay ",sum," money ")
            else:
                print("Paid is successfully!")
                if money>sum:
                    print("Change is", money - sum, " money")
                break
print("Thank you so much! see you again!")
