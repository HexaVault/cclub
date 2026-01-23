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

tileSet.plain = "p"
tileSet.forest = "T"
tileSet.spruce = "S"

prnt("Setting up Biome Map")
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
