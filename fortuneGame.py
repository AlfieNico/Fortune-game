#---------- imports ----------

import random
import json
import os

#---------- Variables ----------

coins = 0
level = 0
xp = 0
classType = "null"
loads = -1



#---------- Lists ----------

classes = ["mage", "warrior", "tank"]
statNames = ["health", "attackSpeed", "attackDamage", "intelligence", "mana", "luck", "agility", "defence"]
statNumbers = ["20", "20", "20"]

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

def getClassStats():
    global classType, statNumbers
    with open("stats.json", "r") as f:
        classStats = json.load(f)
    statNumbers = classStats[classType]

def save():
    data = {"coins": coins,"level": level,"xp": xp,"classType": classType,"loads": loads,"statNumbers": statNumbers}
    with open("save.json", "w") as f:
        json.dump(data, f)

def load():
    global coins, level, xp, classType, loads, statNumbers
    if not os.path.exists("save.json") or os.stat("save.json").st_size == 0:
        return
    with open("save.json", "r") as f:
        data = json.load(f)
        coins = data.get("coins", coins)
        level = data.get("level", level)
        xp = data.get("xp", xp)
        classType = data.get("classType", classType)
        loads = data.get("loads", loads)
        statNumbers = data.get("statNumbers", statNumbers)
    loads += 1

def classChose():
    global classType, statNumbers
    classType = input("What class would you like to choose, type classes to see options: ")
    if classType.lower() == "classes":
        with open("classes.txt", "r") as f:
            print(f.read())
        classType = input("What class would you like to choose: ")
    while classType not in classes:
        classType = input("What class would you like to choose, type classes to see options: ")
        if classType.lower() == "classes":
            with open("classes.txt", "r") as f:
                print(f.read())
            classType = input("What class would you like to choose: ")
    getClassStats()

def xpToNextLevel():
    global level
    return round(100 * (1.5 ** (level - 1))) - xp 

def addXp(adding):
    global xp, level
    xpHold = xp + adding
    while xpHold >= xpToNextLevel():
        xpHold -= xpToNextLevel()
        level += 1
    xp = xpHold

def playerAction(choice):
    global coins, statNames, statNumbers
    if choice.lower() == "actions":
        print("possible actions are: getCoins, looseCoins, fortuneRoll, profile, stats, addXp, quit.")
        return False
    elif choice.lower() == "getcoins":
        coins += int(input("How many coins should be added: "))
    elif choice.lower() == "loosecoins":
        coins -= int(input("How many coins do you want to loose: "))
    elif choice.lower() == "profile":
        print(f"you are on {coins} coins.")
        print(f"your level {level}")
        print(f"you on {xp} xp ")
        print(f"{xpToNextLevel()} xp untill next level")
        print(f"your class is {classType}")
    elif choice.lower() == "fortuneroll":
        if coins >= 5:
            fortune = getFortune()
            print(fortune)
        else:
            print("This costs 5 coins")
    elif choice.lower() == "stats":
        print("your stats are")
        for stat in statNames:
            print(f"{stat} : {statNumbers[stat]}")
    elif choice.lower() == "addxp":
        adding = int(input("enter: "))
        addXp(adding)
    elif choice.lower() == "quit":
        save()
        return True
    return False

def main():
    global classType
    load()
    if loads == 0:
        classChose()
    while True:
        choice = input("What would you like to do (type actions to see possible choices): ")
        if playerAction(choice):
            break

#---------- Main ----------

main()
