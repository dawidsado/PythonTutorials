inputdata = [0,1,2,3,5,8,13,21,34,55,89]

factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

import math

#Ex1

firstListLen = len(inputdata)
secondListLen = len(factortable)
print("First list length: ", secondListLen)
print("Second list length: ", secondListLen)

minvalue = 0
maxvalue = 0
if(firstListLen == secondListLen):
    print("Ok")
    for i in range(len(inputdata)):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        minint = math.floor(minvalue)
        maxint = math.ceil(maxvalue)
else:
    print("inputdata and factortable need to have equal number of elements")

print(minvalue, minint)
print(maxvalue, maxint)

print("-------------------------------------------------------")

#Ex2
import random


for i in range(len(inputdata)):
    minvalue = inputdata[i] - random.random() * inputdata[i]
    maxvalue = inputdata[i] + random.random() * inputdata[i]

print(minvalue)
print(maxvalue)


print("-----------------------------------------------------")

#Ex3

import datetime

datetime.datetime

print(datetime.datetime.today().strftime("%Y-%m-%d"))