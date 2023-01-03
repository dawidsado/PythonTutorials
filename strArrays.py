#Ex1
q = "The eyes".upper()
print(q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6])

#Ex2
q = "a gentleman"
print(q[3] + q[6] + q[7] + q[2] + q[0] + q[4] + q[5] + q[1] + q[8:])

#Ex3
q = "THE MORSE CODE"
print(q[1]+q[2]+q[6]+q[2], q[10:12]+q[4]+q[2], q[12]+q[11]+q[0]+q[7])

#Ex4
line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[33:]
tmp = line[line.find('"')+1:]
title = tmp[:tmp.find('"')]
print(title, time)

#Ex5
line2 = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
tmp2 = line2[line2.find('"')+1:]
title2 = tmp2[:tmp2.find('"')]
time2 = line2[line2.find(":")+2:]
print("Another show:",title2,"at",time2)
