
print("###### ADVENT OF CODE 2020 ######")
print("######        DAY 1        ######\n")

# Load input.txt as an int list
with open('Day_1\input.txt', 'r') as f:
    entries = [int(x) for x in f.read().splitlines()]

sumGoal = 2020
done = False

# returns the sum of all entries in list multiplied
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  

# checks if input-list has a sum of sumGoal, then prints the multiplication result
def check(list):
    if sum(list) == sumGoal:
        print("Following entries have the sum of ", sumGoal)
        for entry in list:
            print(entry)
        result = multiply(list)
        print("Following entries multiplied equals: ", result, "\n")
        return True
    else:
        return False


print("######        PART 1       ######")
for x in entries:
    for y in entries:
        if check([x,y]):
            done = True
            break
    if done:
        break    

done = False
print("######        PART 2       ######")
for x in entries:
    for y in entries:
        for z in entries:
            if check([x, y, z]):
                done = True
                break
        if done:
            break  
    if done:
        break  

print("######  BY ERIK RODRIGUEZ  ######")