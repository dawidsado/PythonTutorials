hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.append("CHILD IN TIME")
hitsTitles.append("AGAIN")
hitsTitles[2]=("Hotel california".upper())
hitsTitles[0] = ("THE SOUND OF SILENCE")
print(hitsTitles.index(("Hotel california".upper())))
hitsTitles.remove("Hotel california".upper())
hitsTitles[0] = "ENJOY THE SILENCE"

hitsToRead = hitsTitles.copy()
hitsToRead.reverse()
hitsToRead.sort()
print(hitsToRead)
hitsToRead.pop(0)
hitsToRead.pop(1)
print(hitsToRead)
additionalSongs = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
hitsToRead.append(additionalSongs[0])
hitsToRead.append(additionalSongs[1])
hitsToRead.clear()