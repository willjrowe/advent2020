#DONE
f = open("day6.txt", "r")
currLine = f.readline().rstrip().strip()
total = 0
while currLine != "":
    currentGroup = {}
    groupSize = 0
    realTotal = 0
    while currLine!="":
        groupSize+=1
        for i in range(0,len(currLine)):
            if currLine[i] in currentGroup:
               currentGroup[currLine[i]] += 1 
            else:
                currentGroup[currLine[i]] = 1
        currLine = f.readline().rstrip().strip()
    for q in currentGroup.values():
        if q == groupSize:
            realTotal+=1
    total+=realTotal
    currLine = f.readline().rstrip().strip()
    if currLine == "":
        print(total)
        exit()
    