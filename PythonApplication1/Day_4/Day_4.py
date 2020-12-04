from typing import NamedTuple

print("###### ADVENT OF CODE 2020 ######")
print("######        DAY 3        ######\n")

# Load input.txt into a list
with open('Day_4\input.txt', 'r') as f:
    input = f.read().split("\n\n")

reqFields = list(["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"])
validPassports = 0

passports = list()

class Passport(NamedTuple):
    byr : str # Birth Year, 4-Digits 1920 - 2002
    iyr : str # Issue Year, 4-Digits 2010 - 2020
    eyr : str # Expiration Year, 4-Digits 2020 - 2030
    hgt : str # Height, A number followed by cm (150 - 193) or in (59 - 76)
    hcl : str # Hair Color, # followed by 6 characters 0-9 or a-f
    ecl : str # Eye Color, exactly one of: amb, blu, gry, grn, hzl, oth
    pid : str # Passport ID, a 9-Digits, including leading zeroes

def isValid(passport):
    passport = passport.replace('\n',' ')
    lines = passport.split(" ")
    byr = between(passport, "byr:", 4)
    iyr = between(passport, "iyr:", 4)
    eyr = between(passport, "eyr:", 4)
    hgt = between(passport, "hgt:", " ")
    hcl = between(passport, "hcl:", 7)
    ecl = between(passport, "ecl:", 3)
    pid = between(passport, "pid:", 9)

def between(value, a, b):
    # Find and validate before-part.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = pos_a + b
    if pos_b == -1: return ""
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]

def hasFields(passport):
    if all(field in passport for field in reqFields): # Check that it has all the required fields.
        return True
    else:
        return False

print("Passports in list: ", len(passports))

for passport in input:
    passport = passport.replace('\n',' ')
    if(hasFields(passport)):
        passports.append(isValid(passport))

#for passport in passports:
#    passport = passport.replace('\n',' ')
#    if (isValid(passport)):
#        validPassports += 1
#        print("OK")
  
print("Valid Passports in list: ", validPassports)

print("\n######  BY ERIK RODRIGUEZ  ######")
