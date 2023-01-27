#Ex1
number = 1
previousNumber = 0

while number < 50:
   sum = number + previousNumber
   print(sum)
   previousNumber = number
   number+=1


#Ex2 Mini game
import random
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