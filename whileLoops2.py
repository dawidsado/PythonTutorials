#Ex1
number = 1
previousNumber = 0

while number < 50:
   sum = number + previousNumber
   print(sum)
   previousNumber = number
   number+=1


#Ex2 Mini game
'''import random
my_number = random.randint(0,20)

guess = -1
print("Guess my number")
trials = 0

while guess != my_number:
   print(my_number)
   guess = int(input())
   trials +=1

   if (guess == my_number):
      print("Gratki")
      print("Liczba prób: ",trials)

   else:
      print("Sorry - my number is smaller than your guess, Try again!")
    '''
#Ex3
initialCapital = 20_000
percent = 0.3
maxTimeYears = 10
i=1

while(i<=maxTimeYears):
   final = initialCapital + (initialCapital * percent)
   print(i,"year",final)
   initialCapital+=(initialCapital*percent)
   i+=1


number = 20730906
sum = 0
res = [int(x) for x in str(number)]

for nums in range(0, len(res)):
   sum+=res[nums]

print(sum)

Text = "United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier."

wordLength = 6

text_splited = Text.replace('\n',' ').split(' ')

shortWords = 0
longWords = 0

while i < len(text_splited):
   if len(text_splited[i]) > wordLength:
      longWords+=1
   elif len(text_splited[i]) > 0:
      shortWords += 1

   print(longWords)

