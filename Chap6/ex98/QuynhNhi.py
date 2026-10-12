from random import randrange

while True:
    machine=randrange(1,101)
    count = 0
    win = False
    while count<7:
        count=count+1
        human=int(input("enter human number:"))
        print(f"Guesing times {count}")
        if machine==human:
            print("You won")
            print(f"Your number = machine ={human}")
            win=True
            break
        else:
            if machine>human:
                print("")
    if win==False:
        print("Game Over")

    ask = input("continue?")
    if ask=="n":
        print("Thank you for your playing game")