def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    level = 0
    for i in range(steps):
        if path[i] == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys

# print(countingValleys(8, ['U','D','D','D','U','D','U','U']))
print(countingValleys(12, ['D','D','U','U','D','D','U','D','U','U','U','D']))