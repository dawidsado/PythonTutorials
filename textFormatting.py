#Ex1
helloMessage = "Hello %s!"

#Ex2
print(helloMessage % ("Kate"))
print(helloMessage % ("Evan"))

#Ex3
helloMessage = "Hello {0:s}!"

#Ex4
print(helloMessage.format("Kate"))
print(helloMessage.format("Evan"))

#Ex5
helloMessage = "%s has %d %s"

#Ex6
print(helloMessage % ("Kate", 1, "animal"))
print(helloMessage % ("Chris", 100000, "$"))

#Ex7
helloMessage = "{0:s} has {1:d} {2:s}"

#Ex8
print(helloMessage.format("Kate", 1, "animal"))
print(helloMessage.format("Chris", 100000, "$"))

#Ex9
line = "{0:s} {1:d} "
print(line.format("Ice cream ", 3))
print(line.format("Trip to venice", 119))
print(line.format("Pizza hawaii", 6))