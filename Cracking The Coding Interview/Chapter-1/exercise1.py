# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Hints: 
# 44 Try a hash table.
# 117 Could a bit vector be useful?
# 132 Can you solve it in O(N log N) time? What might a solution like that look like?

# advance solution not mine

def all_unique_chars(x):
    return len(set(x)) == len(x)

# My solution

def all_unique_chars(str):
    for i in range(len(str) - 1):
        for j in range(i + 1, len(str)):
            if str[j] == str[i]:
                return False
    return True

# Trying another solution

def all_unique_chars(input):
    seen = set()
    for x in input:
        if x in seen:
            return False
        seen.add(x)
    return True

print(all_unique_chars("abcde"))