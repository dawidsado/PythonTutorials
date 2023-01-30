string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

#Ex1
for strings in range(0,9):
    if(strings % 2 == 0):
        print(string_A)
    else:
        print(string_B)

#Ex2
for numbers in range(1,10):
    if(numbers % 2 == 0):
        print("x"*numbers)
    else:
        print("o"*numbers)

print("Nested for loop")
print()


#Ex1
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
for i in range(len(list_noun)):
    for j in range(len(list_adj)):
        print(list_adj[j], list_noun[i])


#Ex2
result = 1
for i in range(0,10):
    i += 1
    result *= i
    print(result)

