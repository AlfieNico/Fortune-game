import random

with open("fortunes.txt", "r") as f:
    fortunes = f.read().split(",")

fortunes = [s.strip() for s in fortunes]  # clean spaces
print(fortunes[10])