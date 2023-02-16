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

