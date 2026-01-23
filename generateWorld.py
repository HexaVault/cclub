from types import SimpleNamespace
import curses
from settings import genPara
from random import uniform


# Data variables
worldWidth = genPara.worldGen.length
worldHeight = genPara.worldGen.height

window = curses.initscr()
clr = window.clrtoeol
def prnt(x):
    window.addstr(x)
    window.refresh()

def prntc(x):
    clr()
    prnt("\r" + x)

tileSet = SimpleNamespace()

tileSet.edge = "#"
tileSet.floor = "."
tileSet.hill = "^"
tileSet.mountain = "M"
tileSet.waterL1 = "w"
tileSet.waterL2 = "W"
tileSet.waterL3 = "₩"
tileSet.waterL4 = "ʬ"

prnt("Setting up World")
n = 0
world = [[*(tileSet.edge * worldWidth)]]
i = 0
while i < worldHeight - 2:
    world.append([*(tileSet.floor * worldWidth)])
    i += 1
world.append([*(tileSet.edge * worldWidth)])
prntc("Finished setting up World\n")

# Generate world and borders
prntc("Adding Edges")
i = 0
while i < len(world):
    world[i][0] = tileSet.edge
    world[i][worldWidth - 1] = tileSet.edge
    i += 1
prntc("Added Edges\n")

# First we should generate the "total landmass". 
prntc("Generating landmass")
i = 0
wW = genPara.worldGen.waterWeight
# Top, bottom, left, right
depthsL1 = [5 + uniform(wW // 2, wW * 4), 5 + uniform(wW // 2, wW * 4), 5 + uniform(wW // 2, wW * 4), 5 + uniform(wW // 2, wW * 4)]
while i < len(world):
    if i < depthsL1[0] or (len(world) - i < depthsL1[1]):
        j = 0
        while j < len(world[i]):
            if world[i][j] != tileSet.edge:
                world[i][j] = tileSet.waterL1
            j += 1
    else:
        j = 0
        while j < len(world[i]):
            if world[i][j] != tileSet.edge and (j < depthsL1[2] or (len(world[i]) - j) < depthsL1[3]):
                world[i][j] = tileSet.waterL1
            j += 1
    i += 1

def countAdjTiles(x, y, tileType, tiles = [(1,1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]):
    numberOfTiles = 0
    for value in tiles:
        x1 = x + value[0]
        y1 = y + value[1]
        if x1 < worldWidth and y1 < worldHeight and x1 > 0 and y1 > 0:
            if world[y1][x1] == tileType: numberOfTiles += 1
    return numberOfTiles

i = 1
j = 1
# Higher water weight basically means its more likely for the water check to go off
# Uniformity is what range it should take. Lower values means it takes water from further away
# and so makes islands seem very fragemented and weird
tilings = [(1, 0), (0, 1), (0, -1), (-1, 0)]

oddsBoost = 0.03
adjustment = 1.2

def fiftyfifty():
    return 1 if (uniform(0, 1) > 0.5) else 0

tilingTest = [
    [80, (1, 1), 100],
    [80, (-1, -1), 100],
    [80, (-1, 1), 100],
    [80, (1, -1), 100],
    [60, (2, 0), 100],
    [60, (-2, 0), 100],
    [60, (0, 2), 100],
    [60, (0, -2), 100],
    [40, (2, 1), 85],
    [40, (-2, 1), 85],
    [40, (1, 2), 85],
    [40, (1, -2), 85],
    [40, (2, -1), 85],
    [40, (-2, -1), 85],
    [40, (-1, 2), 85],
    [40, (-1, -2), 85],
    [20, (2, -2), 70],
    [20, (-2, -2), 70],
    [20, (-2, 2), 70],
    [20, (-2, -2), 70],
    [0, (3, 0), 55],
    [0, (-3, 0), 55],
    [0, (0, 3), 55],
    [0, (0, -3), 55],
    [-20, (1, -3), 35],
    [-20, (-1, -3), 35],
    [-20, (-1, 3), 35],
    [-20, (-1, -3), 35],
    [-20, (3, -1), 35],
    [-20, (-3, -1), 35],
    [-20, (-3, 1), 35],
    [-20, (-3, -1), 35],
]

for value in tilingTest:
    odds = (100 - (genPara.worldGen.uniformity - value[0])) / 100
    odds = max(odds, 0)
    odds **= adjustment

    if abs(value[1][0]) != abs(value[1][1]) and odds != 0:
        odds += oddsBoost
    elif odds != 0:
        odds += fiftyfifty() * oddsBoost

    if uniform(0, 1) <= odds and genPara.worldGen.uniformity <= value[2]:
        tilings.append(value[1])

while i < (len(world) - 1):
    j = 1
    while j < (len(world[i]) - 1):
        #if (i > 35 and (abs(j - depthsL1[2]) < 2 or abs(j - 800 + depthsL1[3]) < 2)):
        #    i = i
        val = countAdjTiles(j, i, tileSet.waterL1, tilings)
        if val > 2 and uniform(0, (val**(1 - genPara.worldGen.uniformity/200))/5) > 0.2:
            world[i][j] = tileSet.waterL1
        j += 1
    i += 1
i = 1
j = 1
while i < (len(world) - 1):
    j = 1
    while j < (len(world[i]) - 1):
        tilings = [(1,1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        val = countAdjTiles(i, j, tileSet.waterL1, tilings)
        if val >= 7 and uniform(0, 0.6) > 0.05: #genPara.worldGen.uniformity/100
            world[i][j] = tileSet.waterL1
        j += 1
    i += 1
prntc("Generated landmass\n")

file = open("world.txt", "w")
finalString = ""
i = 0
j = 0
prnt("Preparing to write to file")
while j < worldHeight:
    i = 0
    while i < worldWidth:
        finalString += world[j][i]
        i += 1
    j += 1
    if j < worldHeight: finalString += "\n"
prntc("Writing to file")
file.write(finalString)
prntc("Written to file, ending\n")