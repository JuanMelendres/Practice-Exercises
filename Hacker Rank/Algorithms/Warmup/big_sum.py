def aVeryBigSum(ar):
    # Write your code here
    total = 0
    for num in ar:
        total += num
    return total

print(aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005]))