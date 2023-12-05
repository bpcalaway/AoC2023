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
    # To everyone's shock, we're using a generic dict object.  K=coord pair, V=list of numbers adjacent
    gearMap = dict()

    for y, line in enumerate(lines):
        for x, c in enumerate(list(line)):
            if c == "*":
                pCoords.append((y, x))
                gearMap[(y, x)] = list()
    return pCoords, gearMap

def updateValidCoord(start, end, y, p, num, gmap):
    # For every num in range, do a comparison +-1 
    while start < end:
        for pc in p:
            if abs(pc[0] - y) < 2 and abs(pc[1] - start) < 2:
                gmap[(pc[0], pc[1])].append(num)
                return gmap
        start = start + 1
    return gmap


with open(file="data/1203.data") as f:
    lines = f.readlines()
    pCoords, gearMap = findCoords(lines)
    for y, line in enumerate(lines):
        # Find all numbers.  End coordinate is one later than you want it to be
        numCoords = re.finditer("[0-9]+", line)
        for c in numCoords:
            #print(c.start(), c.end(), c.group())
            gearMap = updateValidCoord(c.start(), c.end(), y, pCoords, int(c.group()), gearMap)
    
    # Anyone who gets mad at me for not being algorithmically smarter about this should be nicer to me
    gearTotal = 0
    for k in gearMap:
        if len(gearMap[k]) == 2:
            gearTotal = gearTotal + (gearMap[k][0] * gearMap[k][1])

print(gearTotal)