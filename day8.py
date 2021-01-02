#DONE
f = open("day8.txt", "r")
currLine = f.readline().rstrip().strip()
listOfInstructions = []
i=0
while currLine != "":
    listOfInstructions.append(currLine)
    i+=1
    currLine = f.readline().rstrip().strip()

i = 0
accCount = 0
alreadyRan = [0] * len(listOfInstructions)
while True: #assume termination
    if alreadyRan[i] == 1:
        print(accCount)
        exit()
    else:
        alreadyRan[i] = 1
        currInstruction = listOfInstructions[i]
        splitInstruction = currInstruction.split()
        instr = splitInstruction[0]
        instrNum = int(splitInstruction[1])
        if instr == "jmp":
            i+=instrNum
        elif instr == "nop":
            i+=1
        else:
            accCount+=instrNum
            i+=1