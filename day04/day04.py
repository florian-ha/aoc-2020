inputData = open("day04input.txt").read().split('\n\n')

passportFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validPwCounter = 0
for passport in inputData:
    if all(x in passport for x in passportFields):
        validPwCounter += 1

print("Exercise 1:", validPwCounter, "valid passports!")
