#NOT DONE
lastTimeSpoken = [-1] * 100000
firstTimeSpoken = [-1] * 100000
lastTimeSpoken[13] = 1
firstTimeSpoken[13] = 0
lastTimeSpoken[16] = 2
firstTimeSpoken[16] = 0
lastTimeSpoken[0] = 3
firstTimeSpoken[0] = 0
lastTimeSpoken[12] = 4
firstTimeSpoken[12] = 0
lastTimeSpoken[15] = 5
firstTimeSpoken[15] = 0
lastTimeSpoken[1] = 6
firstTimeSpoken[1] = 0
lastNumSpoken = 1
turnNumber = 7
while turnNumber < 2021:
    turnNumber+=1
    if firstTimeSpoken[lastNumSpoken] == 0:
        #that was the first time this was said
        #so say zero
        lastNumSpoken = 0
        firstTimeSpoken[0] = firstTimeSpoken[0] + 1
        lastTimeSpoken[0] = turnNumber
    elif firstTimeSpoken[lastNumSpoken] > 0:

        #might be the first time this number was said or the nth (n>1)



