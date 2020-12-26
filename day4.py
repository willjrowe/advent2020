#DONE
import re

f = open("day4.txt", "r")

required_words = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
validPassportCount = 0
potential = ""
potential2 = ""
firstRound = True
while True:
    passport = ""
    currLine = ""
    passport+=potential+" "
    passport+=potential2+" "
    if potential2 == "" and not firstRound:
        currLine = potential2
    else:
        currLine = f.readline().rstrip()
    while True:
        if (currLine == ""):
            break
        passport+=currLine+" "
        currLine = f.readline().rstrip()
    print(passport)
    validPassport = True
    idList = passport.split(' ')
    for ident in idList:
        ident = ident.strip()
    for word in required_words:
        if word not in passport:
            validPassport = False
        else:
            for ident in idList:
                first4 = ident[:4]
                rest = ident[4:]
                if first4 == "byr:":
                    if (rest.isdigit()):
                        rest = int(rest)
                        if not (1920<= rest <=2002):
                            validPassport = False
                    else:
                        validPassport = False
                elif first4 == "iyr:":
                    if (rest.isdigit()):
                        rest = int(rest)
                        if not (2010<= rest <=2020):
                            validPassport = False
                    else:
                        validPassport = False
                elif first4 == "eyr:":
                    if (rest.isdigit()):
                        rest = int(rest)
                        if not (2020<= rest <=2030):
                            validPassport = False
                    else:
                        validPassport = False
                elif first4 == "hgt:":
                    if "cm" in rest:
                        rest = rest.replace("cm","")
                        if (rest.isdigit()):
                            rest = int(rest)
                            if not (150<=rest<=193):
                                validPassport = False
                        else:
                            validPassport = False
                    elif "in" in rest:
                        rest = rest.replace("in","")
                        if (rest.isdigit()):
                            rest = int(rest)
                            if not (59<=rest<=76):
                                validPassport = False
                        else:
                            validPassport = False
                    else:
                        validPassport = False
                elif first4 == "hcl:":
                    if (rest[0:1]=='#'):
                        rest = rest[1:]
                        if (len(rest)==6):
                            if (not re.search("^[a-f0-9]*$",rest)):
                                validPassport = False
                        else:
                            validPassport = False
                    else:
                        validPassport = False
                elif first4 == "ecl:":
                    hairColores = ['amb','blu','brn','gry','grn','hzl','oth']
                    if not rest in hairColores:
                        validPassport = False
                elif first4 == "pid:":
                    if len(rest) == 9:
                        if not rest.isdigit():
                           validPassport = False
                    else:
                        validPassport = False
    if (validPassport):
        validPassportCount+=1
    potential = f.readline().rstrip().strip()
    potential2 = f.readline().rstrip().strip()
    firstRound = False
    if potential == "" and potential=="":
        break

print(validPassportCount)
