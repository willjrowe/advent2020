#NOT DONE
f = open("day10.txt", "r")
currLine = f.readline().rstrip().strip()
validAdapters = [0] * 200
while currLine != "":
    adapterRating = int(currLine)
    validAdapters[adapterRating] = 1
    currLine = f.readline().rstrip().strip()
lastAdapter = 0
oneJoltDiff = 1
threeJoltDiff = 0
i=1
while i < 195:
    print(i)
    if validAdapters[i+1]==1:
        i=i+1
        oneJoltDiff+=1
    else:
        threeJoltDiff+=1
        i=i+3
threeJoltDiff+=1
print(oneJoltDiff)
print(threeJoltDiff)
print(oneJoltDiff*threeJoltDiff)
