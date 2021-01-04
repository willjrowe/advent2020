#DONE
f = open("day12.txt", "r")
currLine = "will"
currDirection = "E"
currDegree = 0 #polar?
currNS = 0
currEW = 0
while currLine != "":
    currLine = f.readline().rstrip().strip()
    if currLine == "":
        break
    operation = currLine[0]
    opNum = int(currLine[1:])
    if operation == "N":
        currNS+=opNum
    elif operation == "S":
        currNS-=opNum
    elif operation == "E":
        currEW+=opNum
    elif operation == "W":
        currEW-=opNum
    elif operation == "F": #im lazy
        if currDirection == "N":
            currNS+=opNum
        elif currDirection == "S":
            currNS-=opNum
        elif currDirection == "E":
            currEW+=opNum
        elif currDirection == "W":
            currEW-=opNum
    else:
        if operation == "L":
            currDegree+=opNum
            if currDegree >= 360:
                currDegree-=360
        elif operation == "R":
            currDegree-=opNum
            if currDegree < 0:
                currDegree+=360
        if currDegree == 0:
            currDirection = "E"
        elif currDegree == 90:
            currDirection = "N"
        elif currDegree == 180:
            currDirection = "W"
        elif currDegree == 270:
            currDirection = "S"
        else:
            print("UH OH")
            exit()
print(str(currEW))
print(str(currNS))
print(str(currEW + currNS))