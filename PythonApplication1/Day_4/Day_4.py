from typing import NamedTuple

print("###### ADVENT OF CODE 2020 ######")
print("######        DAY 3        ######\n")

# Load input.txt into a list
with open('Day_4\input.txt', 'r') as f:
    input = f.read().split("\n\n")

reqFields = list(['byr:', 'ecl:', 'eyr:', 'hcl:', 'hgt:', 'iyr:', 'pid:']) # This is the sorted order
validColors = ["amb","blu","brn","gry","grn","hzl","oth"]
validChars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
validPassports = 0

# Please don't look at this function, it's a monster :(
def isValid(passport):
    passport = passport.replace('\n',' ')
    lines = passport.split(" ")
    lines.sort()

    for line in lines:
        if("byr:" in line):
            if(yearCheck(int(line.replace("byr:","")), 1920, 2002)):
                continue
            else:
                return False

        if("ecl:" in line):
            line = line.replace("ecl:","")          
            if (line in validColors):
                continue
            else:
                return False
                    
        if("eyr:" in line):
            if(yearCheck(int(line.replace("eyr:","")), 2020, 2030)):
                continue
            else:
                return False
        
        if("hcl:" in line):
            line = line.replace("hcl:","")
            if("#" in line):
                line = line.replace("#","")
            else:
                return False
            if any(str(char) not in validChars for char in line):
                return False
            else:
                continue

        if("hgt:" in line):
            line = line.replace("hgt:","")
            if("cm" in line):
                line = line.replace("cm", "")
                if(line.isnumeric() == False or int(line) < 150 or int(line) > 193):
                    return False
                else:
                    continue
            elif("in" in line):
                line = line.replace("in", "")
                if(line.isnumeric() == False or int(line) < 59 or int(line) > 76):
                    return False
                else:
                    continue
            else:
                return False
        if("iyr:" in line):
            if(yearCheck(int(line.replace("iyr:","")), 2010, 2020)):
                continue
            else:
                return False

        elif("pid:" in line):
            line = line.replace("pid:","")
            if(line.isnumeric() and len(line) == 9):
                continue
            else:
                return False

        if("cid:" in line):
            continue

    return True

def yearCheck(current, min, max):
    if(len(str(current)) == 4 and current >= min and current <= max):
        return True
    else:
        return False

def hasFields(passport):
    if all(field in passport for field in reqFields): # Check that it has all the required fields.
        return True
    else:
        return False

for passport in input:
    passport = passport.replace('\n',' ')
    if(hasFields(passport) and isValid(passport)):
        validPassports += 1
  
print("Valid Passports in list: ", validPassports)
print("Invalid Passports in list: ", len(input) - validPassports)


print("\n######  BY ERIK RODRIGUEZ  ######")
