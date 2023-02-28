#Ex1

def printCat():
    txt = r'''
     |\---/|
     | o_o |
      \_^_/'''
    print(txt)
    return

def printBear():
    txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    print(txt)
    return

def printBat():
    txt = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/       '''
    print(txt)
    return


printCat()

printBear()

printBat()


#Ex2

import datetime
def getDaysTillEnd():
    date_today = datetime.date.today()

    current_year = date_today.year

    date_end_year = datetime.date(current_year,12,31)

    delta = (date_end_year - date_today).days
    print(delta)
    return

getDaysTillEnd()

#Ex3

def printAnimal(animal):
    if animal == "cat":
        printCat()
    elif animal == "bear":
        printBear()
    elif animal == "bat":
        printBat()
    else:
        print("Cannot print",animal,"Correct values for the parameter are: cat, bear, bat")
        return

printAnimal("cat")

#Ex4

def getDaysTillEnd(year, month, day):

    given_date = datetime.date(year,month,day)

    date_end_year = datetime.date(year,12,31)

    delta = (date_end_year - given_date).days
    print(delta)
    return

getDaysTillEnd(2023,2,18)


print("-------------")

#Now ex for default parameters

#Ex5

def printAnimal(animal=" "):
    if animal == "cat":
        printCat()
    elif animal == "bear":
        printBear()
    elif animal == "bat":
        printBat()
    else:
        print("Cannot print",animal,"Correct values for the parameter are: cat, bear, bat")
        return

def getDaysTillEnd(year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().month):

    given_date = datetime.date(year,month,day)

    date_end_year = datetime.date(year,12,31)

    delta = (date_end_year - given_date).days
    print(delta)
    return
getDaysTillEnd()

#Ex6

def printAnimal(animal=" "):
    if animal == "cat":
        printCat()

    elif animal == "bear":
        printBear()

    elif animal == "bat":
        printBat()

    else:
        print("Cannot print",animal,"Correct values for the parameter are: cat, bear, bat")
        return False
    return True


    if PrintAnimal():
        print('The parameter was correct')

    else:
        print('The parameter was INCORRECT')

    if PrintAnimal('dog'):
        print('The parameter was correct')
    else:
        print('The parameter was INCORRECT')

    if PrintAnimal('bat'):
        print('The parameter was correct')
    else:
        print('The parameter was INCORRECT')

#Ex7
def getDaysTillEnd(year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().month):

    given_date = datetime.date(year,month,day)

    date_end_year = datetime.date(year,12,31)

    delta = (date_end_year - given_date).days

    return delta

#Ex8
def printAnimal(*animals):
    for animal in animals:
        if animal == "cat":
            printCat()

        elif animal == "bear":
            printBear()

        elif animal == "bat":
            printBat()

        else:
            print("Cannot print",animals,"Correct values for the parameter are: cat, bear, bat")
            return


printAnimal("cat","doggo")

#Ex9
def getDaysTillEnd(*dates):

    for given_date in dates:

        date_end_year = datetime.date(given_date.year,12,31)

        delta = (date_end_year - given_date).days

        print(delta)

getDaysTillEnd(datetime.date(2023,3,1))