import re

englishDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

total = 0
with open(file="data/1201.csv") as f:
    lines = f.readlines()
    for line in lines:
        # Sub out each key, does the order matter?  Probably not
        for key in englishDict.keys():
            line = re.sub(key, str(englishDict[key]), line)

        # Dump all non-numeric characters and grab the first and last with reverse index (gets first on len one)
        numstr = re.sub("[^0-9]", str(), line)
        print(numstr)
        total = total + int(numstr[0] + numstr[-1])

print(total)