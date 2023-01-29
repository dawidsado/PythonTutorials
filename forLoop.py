#Ex1
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for data in data:
    print(data.upper())


for data in data:
    elements = data.split(":")
    print(elements[0].upper())

    if (elements[0] == "Error"):
        print(elements[1].upper())

    else:
        print(elements[1])