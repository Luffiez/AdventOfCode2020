from typing import NamedTuple
import math

print("###### ADVENT OF CODE 2020 ######")
print("######        DAY 5        ######\n")

# Load input.txt into a list
with open('Day_5\input.txt', 'r') as f:
    binaries = f.read().splitlines()

class SeatInfo(NamedTuple):
    binary : str
    row : int
    column : int
    id : int

seats = list()

def checkSeatID(id, list): # Check if the seat ID exists in list
   for seat in list:
       if(seat.id == id):
           return True  
   return False

def getSeatID(row, column):
    return (row * 8) + column

def getRow(binary):
    ranges = [0, 127]
    for char in binary:
        if(char == "F"):
            ranges = getLower(ranges)
        elif(char == "B"):
            ranges = getUpper(ranges)

    return ranges[0]
  
def getColumn(binary):
    ranges = [0, 7]
    for char in binary:
        if(char == "L"):
            ranges = getLower(ranges)
        elif(char == "R"):
            ranges = getUpper(ranges)

    return ranges[0]

def getLower(ranges):
    diff = ranges[0] + (ranges[1] - ranges[0]) / 2
    return [ranges[0], math.floor(diff)]

def getUpper(ranges):
    diff = ranges[1] - (ranges[1] - ranges[0]) / 2
    return [math.ceil(diff), ranges[1]]

for binary in binaries:
    row = getRow(binary[:-3])
    column = getColumn(binary[7:])
    seatId = getSeatID(row, column)
    seats.append(SeatInfo(binary, row, column, seatId));
    print("[",binary,"] Row:",row,"Column:", column,"ID:", seatId)

sortedSeats = sorted(seats, key=lambda x: x.id, reverse=False)
largest = sortedSeats[len(sortedSeats)-1].id
smallest = sortedSeats[0].id

print("\nTotal seats:", len(seats))
print( "Smallest Seat ID:", smallest, "Largest Seat ID:", largest)

index = 0
for seat in sortedSeats[:-1]:
    if(sortedSeats[index].id + 1 != sortedSeats[index + 1].id):
        if(not checkSeatID(sortedSeats[index].id + 1, sortedSeats)):
            print("My seat ID is:", sortedSeats[index].id + 1)
            break
    index += 1

print("\n######  BY ERIK RODRIGUEZ  ######")
