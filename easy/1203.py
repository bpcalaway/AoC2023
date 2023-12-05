import re

lines = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

# List of tuples of special character coordinates, for math later.
def findCoords(lines):
    pCoords = list()

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line)):
            if c != "." and not str.isalnum(c) and c != "\n":
                pCoords.append((y, x))
    return pCoords

def validCoord(start, end, y, p):
    # For every num in range, do a comparison +-1 
    while start < end:
        for pc in p:
            if abs(pc[0] - y) < 2 and abs(pc[1] - start) < 2:
                return True 
        start = start + 1
    return False

partTotal = 0
with open(file="data/1203.data") as f:
    lines = f.readlines()
    pCoords = findCoords(lines)
    for y, line in enumerate(lines):
        # Find all numbers.  End coordinate is one later than you want it to be
        numCoords = re.finditer("[0-9]+", line)
        for c in numCoords:
            #print(c.start(), c.end(), c.group())
            if validCoord(c.start(), c.end(), y, pCoords):
                print(c.group())
                partTotal = partTotal + int(c.group())

print(partTotal)