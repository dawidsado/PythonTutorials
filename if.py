#Ex1
MIN_LIKES = 500
MIN_SHARES = 100

min_likes = 800
min_shares = 120

if min_likes >= MIN_LIKES and min_shares >= MIN_SHARES:
    print("10% discount")
else:
    print("Not enough likes/shares")

#Ex2
isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if isPizzaOrdered or isBigDrinkOrdered and not isWeekend:
    print("Congrats, you received burger coupon")
else:
    print("Keep on trying")

#Ex3
diskSize = 140
diskSizeUsed = 100
fileSize = 20
if fileSize <= (diskSize-diskSizeUsed):
    print("There is some space for your file")
else:
    print("There is lack of space")

#Ex4
musclePain = False
fever = True
weakness = True
if musclePain and fever and weakness:
    print("suspicion of influenza")
elif weakness and (not fever) or (not musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")

isMan = True

if musclePain and fever and weakness:
    print("suspicion of influenza")
elif (musclePain or fever or weakness) and isMan:
    print("suspicion of influenza")
else:
    print("you may be cold")


#Ex5
isCheckCompleted = False

print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")



