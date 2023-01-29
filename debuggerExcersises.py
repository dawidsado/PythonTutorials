#Ex1

'''number = 1
previus_number = 0

while number < 50:
    print(number + previus_number)
    previus_number = number
    number += 1
'''

#Ex2

text = ''
number = 10
text2 = ''
condition = True

while condition:
    if len(text) > number:
        condition = False
    text += 'x'
    print(text)