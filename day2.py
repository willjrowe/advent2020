#DONE
f = open("day2.txt", "r")
validCount = 0
while True:
    currLine = f.readline().rstrip().strip()
    if currLine == "":
        print(validCount)
        exit()
    splitCurr = currLine.split()
    splitRange = splitCurr[0].split("-")
    minLetter = int(splitRange[0])
    maxLetter = int(splitRange[1])
    keyLetter = splitCurr[1][0]
    passwordAttempt = splitCurr[2]
    numOfLetter = passwordAttempt.count(keyLetter)
    # part 1
    # if numOfLetter >= minLetter and numOfLetter<= maxLetter:
    #     validCount+=1
    if passwordAttempt[minLetter-1] == keyLetter and passwordAttempt[maxLetter-1] != keyLetter:
        validCount+=1
    elif passwordAttempt[minLetter-1] != keyLetter and passwordAttempt[maxLetter-1] == keyLetter:
        validCount+=1