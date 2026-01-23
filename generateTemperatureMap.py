from types import SimpleNamespace
import curses
from settings import genPara
from random import randint

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

# 101 characters, to allow for variances from to 0-100 (incl.)
numberList = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"£$%^&*()-_=+[]{};:'@#~,<.>ΓΔΘΛΞΠΣΦΨΩω")
edgeChar = "∎"
unsetTemp = "∘"

prnt("Setting up Temperature Map")
n = 0
world = [[*(edgeChar * worldWidth)]]
i = 0
while i < worldHeight - 2:
    world.append([*(unsetTemp * worldWidth)])
    i += 1
world.append([*(unsetTemp * worldWidth)])
prntc("Finished setting up Temperature Map\n")

# Generate world and borders
prntc("Adding Edges to Tmap")
i = 0
while i < len(world):
    world[i][0] = edgeChar
    world[i][worldWidth - 1] = edgeChar
    i += 1
prntc("Added Edges to Tmap\n")

prntc("Adding random temperature points")
pointLoc = []
def tryGetValidPoint():
    fails = 0
    chosenPoint = (randint(1, worldWidth-1), randint(1, worldHeight-1))
    while fails < 12:
        isFailed = False
        for value in pointLoc:
            if abs(value[0] - chosenPoint[0]) + abs(value[1] - chosenPoint[1]) < genPara.tempPrecip.minimumPointDist:
                isFailed = True
        if not isFailed: return chosenPoint
        chosenPoint = (randint(1, worldWidth-1), randint(1, worldHeight-1))
        fails += 1
    return chosenPoint

i = genPara.tempPrecip.startHot
while i > 0:
    point = tryGetValidPoint()
    nPoint = (point[0], point[1], genPara.tempPrecip.consideredHot)
    pointLoc.append(nPoint)
    i -= 1

i = genPara.tempPrecip.startCold
while i > 0:
    point = tryGetValidPoint()
    nPoint = (point[0], point[1], genPara.tempPrecip.consideredCold)
    pointLoc.append(nPoint)
    i -= 1

i = genPara.tempPrecip.startNeutral
while i > 0:
    point = tryGetValidPoint()
    nPoint = (point[0], point[1], genPara.tempPrecip.consideredNeutral)
    pointLoc.append(nPoint)
    i -= 1

for value in pointLoc:
    world[value[0]][value[1]] = numberList[value[2]]

prntc("Added Temperature Points\n")

prnt("Spreading Temperature \n")

pointsToModify = []
i = 1
j = 1
tempDecided = (0, 0)
foundUnset = True
loop = 1
while foundUnset and loop < 50:
    prntc("Loop " + str(loop))
    loop += 1
    foundUnset = False
    j = 0
    while j < worldHeight - 1:
        i = 0
        while i < worldWidth - 1:
            tempDecided = (0, 0)
            if world[j][i-1] != unsetTemp and world[j][i-1] != edgeChar:
                tempDecided = (tempDecided[0] + numberList.index(world[j][i-1]), tempDecided[1] + 1)
            if world[j][i+1] != unsetTemp and world[j][i+1] != edgeChar:
                tempDecided = (tempDecided[0] + numberList.index(world[j][i+1]), tempDecided[1] + 1)
            if world[j-1][i] != unsetTemp and world[j-1][i] != edgeChar:
                tempDecided = (tempDecided[0] + numberList.index(world[j-1][i]), tempDecided[1] + 1)
            if world[j+1][i] != unsetTemp and world[j+1][i] != edgeChar:   
                tempDecided = (tempDecided[0] + numberList.index(world[j+1][i]), tempDecided[1] + 1)
            if world[j][i] == unsetTemp:
                foundUnset = True
            if tempDecided[1] != 0 and world[j][i] == unsetTemp and world[j][i] != edgeChar:
                tempDecided = tempDecided[0] // tempDecided[1]
                pointsToModify.append((j, i, randint(max(0, tempDecided - genPara.tempPrecip.tempDiff), min(100, tempDecided + genPara.tempPrecip.tempDiff))))
            i += 1
        j += 1

    for value in pointsToModify:
        world[value[0]][value[1]] = numberList[value[2]]


file = open("temp.txt", "w")
finalString = ""
i = 0
j = 0
while j < worldHeight:
    i = 0
    while i < worldWidth:
        finalString += world[j][i]
        i += 1
    j += 1
    prntc("Preparing Line " + str(j) + " of " + str(worldHeight))
    if j < worldHeight: finalString += "\n"
prntc("Writing to file")
file.write(finalString)
prntc("Written to file, ending\n")