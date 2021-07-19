def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zeros = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zeros += 1
    print("{0:.6f}".format(positive/len(arr)))
    print("{0:.6f}".format(negative/len(arr)))
    print("{0:.6f}".format(zeros/len(arr)))

plusMinus([1,-2,3,0,-1,2,0])