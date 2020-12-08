print("###### ADVENT OF CODE 2020 ######")
print("######        DAY 6        ######\n")

# Load input.txt into a list
with open('Day_6\input.txt', 'r') as f:
    groups = f.read().split("\n\n")

questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def getYesInGroup(group):
    numberOfYes = 0
    members = group.split("\n")
    
    for char in questions:
        answers = 0
        for member in members:
            if(char in member):
                answers += 1
                continue
        if(answers == len(members)):
            numberOfYes += 1
    print(members, "=", numberOfYes)
    return numberOfYes

totalSum = 0
for group in groups:
    numberOfYes = getYesInGroup(group)
    totalSum += numberOfYes
    print(numberOfYes)

print("The sum of all 'yes' in all groups is:", totalSum)
print("\n######  BY ERIK RODRIGUEZ  ######")
