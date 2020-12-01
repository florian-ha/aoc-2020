with open('day01input.txt') as f:
    day1input = f.read().splitlines()
day1input = list(map(int, day1input))

aufgabe1done = False
aufgabe2done = False

# Looks for 2 numbers which when added together are 2020 and returns them multiplied
print("Exercise 1: ")
for x in range(len(day1input)):
    for y in range(len(day1input)):
        if (day1input[x] + day1input[y]) == 2020:
            print(day1input[x] * day1input[y])
            aufgabe1done = True
        if aufgabe1done:
            break

# Looks for 3 numbers which when added together are 2020 and returns them multiplied
print("Exercise 2: ")
for x in range(len(day1input)):
    for y in range(len(day1input)):
        for z in range(len(day1input)):
            if (day1input[x] + day1input[y] + day1input[z]) == 2020:
                print(day1input[x] * day1input[y] * day1input[z])
                aufgabe2done = True
            if aufgabe2done:
                break
