def sockMerchant(n, ar):
    # Write your code here
    socks = dict()
    pairs = 0
    for i in ar:
        if i in socks:
            socks[i] = socks[i] + 1
        if i not in socks:
            socks[i] = 1
        if socks[i] % 2 == 0:
            pairs += 1
    return pairs

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))