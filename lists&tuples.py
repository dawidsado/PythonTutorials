#Ex1
marketing = ["loyality program", "client promotion","market research"]
#Ex2
marketing.append("public relations")
#Ex3
print(marketing[2])
#Ex4
marketing[1] = "investor relations"
print(marketing)
#Ex5
emailMarketing = marketing.copy()
#Ex6
emailMarketing.sort()
#Ex7
internalEmails = ["internal communication"]
#Ex8
emailMarketing.extend(internalEmails)
#Ex9
print(emailMarketing)
krotka = tuple(emailMarketing)
print(krotka)