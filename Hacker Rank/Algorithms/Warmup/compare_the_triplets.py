def compareTriplets(a, b):
    alice = 0
    bob = 0 
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] > b[i]:
                alice += 1
            if a[i] < b[i]:
                bob += 1
        return alice, bob
    return False

print(compareTriplets([5,6,7], [3,6,10]))