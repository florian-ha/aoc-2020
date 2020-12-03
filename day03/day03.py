with open('day03input.txt') as f:
    inputData = f.read().splitlines()

# Function takes in right and down as parameters 
def treeTraverse(right, down):
    y = 0
    tree_count = 0
    for x in range(len(inputData)):
        if (x % down) == 0:
            temp_line = inputData[x]
            if y >= len(temp_line):
                y -= len(temp_line)
            if temp_line[y] == '#':
                tree_count += 1
            y += right

    return tree_count


print("Exercise 1: ")
print(treeTraverse(3, 1))

allSlopeMult = treeTraverse(3, 1) * treeTraverse(5, 1) * treeTraverse(7, 1) * treeTraverse(1, 2) * treeTraverse(1, 1)
print("Exercise 2: ")
print(allSlopeMult)
