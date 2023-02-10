import random

#Ex1
for i in range(0,5):
    print(random.randint(1,100))

print("-------------------------------")

#Ex2
number1 = random.randint(1,100)
counter = 1
number2 = random.randint(1,100)

print(counter, number2)

while (number1 != number2):
    counter+=1
    number2 = random.randint(1,100)
    print(counter, number2)

print("Attempts", counter)

print("-----------------------------")

#Ex3
'''countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

randomTeams = random.shuffle(countries)
groupNumber = 0

for i in range(len(countries)):
    if i%4==0:
        groupNumber+=1
        print("----Grupa %d----" % (groupNumber))
        print(countries[i])
'''
#Ex4
print("-----------------------------------------")

min = 1
max = 6

dice = random.randint(min, max)

print(dice)
if(dice == 1):
    print()
    print("0")
    print()
elif(dice == 2):
    print(        "0")
    print("          ")
    print("0"        )
elif(dice == 3):
    print(     "0")
    print(  "0" )
    print("0"     )
elif(dice==4):
    print("0","0")
    print()
    print("0", "0")
elif(dice==5):
    print("0", "0")
    print(   "0"    )
    print("0", "0")
else:
    print("0", "0")
    print("0","0")
    print("0", "0")

#Ex5
print("-------------------")
dices = []
for i in range(5):
    i = random.randint(min,max)
    print(i)
    dices.append(i)

dices.sort()
print(dices)

#Ex6
print("------------------")
colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

for i in colors:
    for j in figures:
        allCards.append(i)
        allCards.append(j)

random.shuffle(allCards)

player1 = []
player2 = []

#1 approach

max = len(allCards)

for i in range(max-1):
    if (i %2==0):
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print(player1)
print(player2)

#2 approach
player1 = allCards[:12]
player2 = allCards[12:]