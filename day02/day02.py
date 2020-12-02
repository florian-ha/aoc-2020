with open('day02input.txt') as f:
    inputData = f.read().splitlines()

validPasswords = 0
print("Exercise 1: ")
for x in range(len(inputData)):
    tempCache = inputData[x].split(" ")
    tempNumbers = tempCache[0].split("-")
    tempNumbers = list(map(int, tempNumbers))
    tempLetter = tempCache[1].replace(":", "")
    tempPassword = tempCache[2]
    tempCounter = 0
    for letter in tempPassword:
        if letter == tempLetter:
            tempCounter += 1
    if (tempCounter >= tempNumbers[0]) and (tempCounter <= tempNumbers[1]):
        validPasswords += 1
print(validPasswords)

validPasswords2 = 0
print("Exercise 2: ")
for x in range(len(inputData)):
    validPasswordCount = 0
    tempCache = inputData[x].split(" ")
    tempNumbers = tempCache[0].split("-")
    tempNumbers = list(map(int, tempNumbers))
    tempLetter = tempCache[1].replace(":", "")
    tempPassword = tempCache[2]
    z = 0
    if tempLetter in tempPassword:
        y = 0
        for letter in tempPassword:
            y += 1
            if letter == tempLetter and (y == tempNumbers[0] or y == tempNumbers[1]):
                z += 1
        if z == 1:
            validPasswords2 += 1

print(validPasswords2)
