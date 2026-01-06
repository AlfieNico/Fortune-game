import random

fortune = "null"
type = "null"
#---------- Subprograms ----------

def fortuneType():
    if random.randint(1,2) == 1:
        return "Positive"
    else:
        return "Negative"

        
def getFortune(fortune):
    if fortuneType() == "Positive":
        with open("positiveFortunes.txt", "r") as f:
            fortunes = f.read().split(",")
    else:
        with open("negativeFortunes.txt", "r") as f:
            fortunes = f.read().split(",")

    fortunes = [s.strip() for s in fortunes]
    fortune = fortunes[random.randint(0,4)]
    return fortune

#---------- Main ----------

fortune = getFortune(fortune)
print(fortune)