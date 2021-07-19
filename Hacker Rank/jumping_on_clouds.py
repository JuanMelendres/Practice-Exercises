def jumpingOnClouds(steps,c):
    # Write your code here
    current_pos = 0
    jumps = 0
    first_cloud = len(c)-1
    second_cloud = len(c)-2
    while current_pos < second_cloud:
        if c[current_pos+2] == 0:
            current_pos += 2
        else: 
            current_pos += 1
        jumps += 1
    if current_pos != first_cloud:
        jumps += 1
    return jumps

print(jumpingOnClouds(7, [0,0,1,0,0,1,0]))
print(jumpingOnClouds(6, [0,0,0,0,1,0]))