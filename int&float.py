#Ex1
import datetime

name = "Dawid"

#Ex2
age = 20

#Ex3
daysInYear = 365

#Ex4
message = "%s is %d years old, so is about %d days old"

#Ex5
print(message % ("Jan", 26, 9490))

#Ex6
print(message % (name, age, age*daysInYear))

#Ex7
message = '{0:s} is {1:d} years old, so is about {2:d} days old'

#Ex8
print(message.format("Chris", 17, 6205))

#Ex9
print("1234567890 divided by 12345 is", int(123456890/12345), "and the rest is", (123456890 % 12345))