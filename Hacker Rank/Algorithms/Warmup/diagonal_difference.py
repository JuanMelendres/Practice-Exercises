def diagonalDifference(arr):
    # Write your code here
    diagonal_left = sum([r[i] for i, r in enumerate(arr)])
    diagonal_right = sum([r[-i - 1] for i, r in enumerate(arr)])
    return abs(diagonal_left - diagonal_right)
    
print(diagonalDifference([
    [1,2,3], 
    [5,4,6],
    [7,8,9]]))