#Ex1
firstRow = 1
lastRow = 31
currentRow = firstRow

while (currentRow <= lastRow):
    print("Row number", currentRow)
    currentRow+=1

#Ex2
firstNumber = 1
lastNumber = 13
i = firstNumber
while (i <= lastNumber):
    print("square", i**2)
    print("cube", i**3)
    i+=1

#Ex3
beg = 0
end = 16
i = beg
while(i <= end):
    print(i,"square root equals",i**2)
    i+=1

#Ex4
beg = 1
end = 10
i = beg
while (i <= end):
    print(i*'x')
    i+=1

#Ex5
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers)-1
while i < max:
    print(i,numbers[i],numbers[i+1])
    if numbers[i]**2 == numbers[i+1]:
        print("\tFOUND:")
        i+=1

#Ex6
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers)-2

while i<max:
    print(i, numbers[i], numbers[i+1], numbers[i+2])
    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
        print("FOUND: ")
        i+=1

#Ex7
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
i = 0
j = 1
max = len(texts)

while i<max and j<max:
    print(i, texts[i], texts[j])
    i+=2
    j+=2
    if len(texts[i])==len(texts[j]):
        print("FOUND: ")
