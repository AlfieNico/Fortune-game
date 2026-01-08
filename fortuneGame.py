import random

#---------- Variables ----------

coins = 0
level = 0
xp = 0

#---------- Subprograms ----------

def fortuneType():
    if random.randint(1,2) == 1:
        return "Positive"
    else:
        return "Negative"

def getFortune():
    if fortuneType() == "Positive":
        with open("positiveFortunes.txt", "r") as f:
            fortunes = f.read().split(",")
    else:
        with open("negativeFortunes.txt", "r") as f:
            fortunes = f.read().split(",")

    fortunes = [s.strip() for s in fortunes]
    fortune = fortunes[random.randint(0,4)]
    return fortune

def playerAction(choice):
    global coins
    if choice.lower() == "actions":
        print("possible actions are: getCoins, looseCoins, fortuneRoll, profile, quit.")
        return False
    elif choice.lower() == "getcoins":
        coins += int(input("How many coins should be added: "))
    elif choice.lower() == "loosecoins":
        coins -= int(input("How many coins do you want to loose: "))
    elif choice.lower() == "profile":
        print(f"you are on {coins} coins.")
        print(f"your level {level}")
        print(f"xp untill next level {xp}")
    elif choice.lower() == "fortuneroll":
        if coins >= 5:
            fortune = getFortune()
            print(fortune)
        else:
            print("This costs 5 coins")
    elif choice.lower() == "quit":
        return True
    return False
        

def main():
    while True:
        choice = input("What would you like to do (type actions to see possible choices): ")
        if playerAction(choice):
            break

#---------- Main ----------

main()
