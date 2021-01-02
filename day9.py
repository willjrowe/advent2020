#DONE
f = open("day9.txt", "r")
currNumbers = []
#get the preamble
while len(currNumbers) < 25:
    currLine = f.readline().rstrip().strip()
    currNumbers.append(int(currLine))
while True:
    nextNum = int(f.readline().rstrip().strip())
    validNum = False
    for i in range(0,24):
        for j in range(i+1,25):
            if currNumbers[i] + currNumbers[j] == int(nextNum) and i != j:
                validNum = True
    if validNum:
        currNumbers.pop(0)
        currNumbers.append(nextNum)
    else:
        print(nextNum)
        exit()