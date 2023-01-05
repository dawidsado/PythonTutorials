#Ex1
MIN_LIKES = 500
MIN_SHARES = 100

min_likes = 300
min_shares = 400

if min_likes < MIN_LIKES:
    print("There is lack of likes")
elif min_shares < MIN_SHARES:
    print("There is lack of shares")
else:
    print("You receive 10% discount")

#Ex2
isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False

if isWeekend:
    print("Your ordered on the weekend, promotion is only available on week")
elif (not isBigDrinkOrdered) and (not isPizzaOrdered):
    print("You didnt make an order")
else:
    print("Congrats, you receiving a burger discount")

