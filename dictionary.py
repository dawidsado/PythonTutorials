#Ex1
chanels = {"Google":1480,"Email":300,"Natural Traffic":440,"TV Spot":700}
#Ex2
print(chanels["Email"])
#Ex3
updateChanels = {"Natural Traffic":520, "News":600}
#Ex4
chanels.update(updateChanels)
print(chanels)
#Ex5
print(chanels.keys())
#Ex6
chanels.pop("Email")
print(chanels)