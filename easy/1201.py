import re

total = 0
with open(file="data/1201.csv") as f:
    lines = f.readlines()
    for line in lines:
        numstr = re.sub("[^0-9]", str(), line)
        total = total + int(numstr[0] + numstr[-1])

print(total)