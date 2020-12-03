from typing import NamedTuple

print("###### ADVENT OF CODE 2020 ######")
print("######        DAY 3        ######\n")

# Load input.txt into a list
with open('Day_3\input.txt', 'r') as f:
    grid = f.read().splitlines()

class Slope(NamedTuple):
    right: int
    down: int

slopes = list()

slopes.append(Slope(1,1))
slopes.append(Slope(3,1))
slopes.append(Slope(5,1))
slopes.append(Slope(7,1))
slopes.append(Slope(1,2))

def getPosRight(row, curRight):
    rowLength = len(row)
    if(curRight >= rowLength):
        offset = curRight - rowLength
        return offset
    return curRight

def check(stepX, stepY):
    trees = 0
    curRight = 0
    for row in grid[::stepY]:
        curRight = getPosRight(row, curRight)
        coordinate = row[curRight]
        if(coordinate == "#"):
            trees += 1
        curRight += stepX
    return trees

print("Number of slopes to check:{}\n".format(len(slopes)))

slopes_multiplied = 0
for slope in slopes:
    trees = check(slope.right, slope.down)
    print("Trees in slope [{},{}] = {}".format(slope.right, slope.down, trees))
    if(slopes_multiplied == 0):
        slopes_multiplied = trees
    else:
        slopes_multiplied *= trees
    
print("\nSlopes multiplied:", slopes_multiplied)

print("\n######  BY ERIK RODRIGUEZ  ######")
