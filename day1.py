#DONE
f = open("day1.txt", "r")
currLine = f.readline().rstrip().strip()
listOfNums = []
while currLine != "":
    listOfNums.append(int(currLine))
    currLine = f.readline().rstrip().strip()
for i in range(0,len(listOfNums)):
    for j in range(i+1,len(listOfNums)):
        for k in range(j+1,len(listOfNums)):
            if listOfNums[i] + listOfNums[j] + listOfNums[k] == 2020 and i != j and i!= k and j!=k:
                print(str(listOfNums[i] * listOfNums[j] * listOfNums[k]))
                exit()