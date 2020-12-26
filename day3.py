#NOT DONE
f = open("day3.txt", "r")
treeCount = 0
pos=0
while True:
    currLine = f.readline().rstrip().strip()
    if currLine == "":
        print(treeCount)
        exit()
    for i in range(pos,pos+3):
        print(pos)
        print(currLine[i])

        if i <= 30 and currLine[i] == "#":
            treeCount+=1
    pos+=3
    if (pos==30):
        pos=0
    if (pos > 30):
        remainder = pos % 31
        currLine = f.readline().rstrip().strip()
        if currLine == "":
            print(treeCount)
            exit()
        print(currLine)
        for i in range(0,remainder):
            if currLine[i] == "#":
                treeCount+=1
        pos = remainder
        print(pos)