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


#Ex3
fibonacciIterations=20
a1 = 0

a2 = 1

a3 = 0

for i in range (0, 20):
    a1=a2
    a2=a3
    a3=a1 + a2
    print(i, a3)

#Ex4

Text = 'Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was found that this solution just couldn’t do the job. Python was compared to other languages, such as Tcl and Perl, and chosen because it’s an easier-to-learn language that the organization can implement incrementally. In addition, Python can be embedded within a larger software system as a scripting language, even if the system is written in a language such as C/C++. It turns out that Python can successfully interact with these other languages in situations in which some languages can’t.'

txt_splited = Text.replace("\n"," ").split(' ')

for word in txt_splited:
    if (word.find("p")>=0):
        print(word)

#Ex5

dictionary = {'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less than 50%'}


for categories in dictionary.keys():
    print(categories,"-",dictionary[categories])