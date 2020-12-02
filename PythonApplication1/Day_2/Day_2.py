from typing import NamedTuple

print("###### ADVENT OF CODE 2020 ######")
print("######        DAY 2        ######\n")

# Load input.txt into a list
with open('Day_2\input.txt', 'r') as f:
    passwords = f.read().splitlines()

validPartOne = list()
validPartTwo = list()

# A NamedTuple used to store the split values of a password and its policies.
# This allows for easy access and all variables stored under one reference
class Password(NamedTuple):
    min: int
    max: int
    letter: str
    value: str

# Format recieved from input-file: [1-4 n: nnnn]
# Split the input based on " ", "-" and ":", then create a new Password and populate the values.
def split(password):
    x = password.split(" ")     # x = [1-4, n:, nnnn]
    values = x[0].split("-")    # values = [1, 4]
    letter = x[1].split(":")    # letter = [n]
    pwd = Password(values[0], values[1], letter[0], x[2]) # x[2] = 'nnnn'
    return pwd

# loop-through all characters of the passwords value, if it equals the key-character, increase the letters-counter
# after the loop, if the letters-counter is within bounds of the min-max from the policy, return true. Else, return false
def checkPartOne(password):
    letters = 0
    for char in password.value:
        if(char == password.letter):
            letters += 1
    if(int(letters) >= int(password.min) and int(letters) <= int(password.max)):
        return True
    else:
        return False

# Checks if lowest value exists in the password-value and if the highest value exists in the password-value.
# If it exists in only ONE of them, return true. Else, return false
def checkPartTwo(password):
    letterA = str(password.value[int(password.min) - 1]) == str(password.letter)
    letterB = str(password.value[int(password.max) - 1]) == str(password.letter)
    if(letterA and not letterB):
        return True
    elif(letterB and not letterA):
        return True
    else:
        return False

print("######        PART 1       ######")
for x in passwords:
    password = split(x)
    if(checkPartOne(password)):
        validPartOne.append(password)
print("Number of valid passwords:", len(validPartOne), "\n")

print("######        PART 2       ######")
for x in passwords:
    password = split(x)
    if(checkPartTwo(password)):
        validPartTwo.append(password)
print("Number of valid passwords:", len(validPartTwo), "\n")

print("######  BY ERIK RODRIGUEZ  ######")
