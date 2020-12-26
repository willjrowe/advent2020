#DONE
f = open("day5.txt", "r")
currLine = "will"
maxseatid = -5
seatList = [0] * 1023
while currLine != "":
    currLine = f.readline().rstrip().strip()
    if currLine == "":
        break
    low = 0
    high = 127
    for i in range(0,7):
        if currLine[i] == "B":
            low = int((high-low)/2) + low + 1
        else: #currLine[i] == "F":
            high = high - int((high-low)/2) - 1
    row = low
    low = 0
    high = 7
    for i in range(7,10):
        if currLine[i] == "R":
            low = int((high-low)/2) + low + 1
        else: #currLine[i] == "L":
            high = high - int((high-low)/2) - 1
    column = low
    seatid = 8 * row + column
    seatList[seatid] = 1
    if seatid > maxseatid:
        maxseatid = seatid
print(maxseatid)
print(seatList)
print(seatList.index(0,15))
