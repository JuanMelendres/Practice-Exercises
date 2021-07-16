def sockMerchant(n, ar):
    pears = 0
    color = set()
    for num in ar:
        if num not in color:
            color.add(num)
        else:
            pears += 1
    return pears

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))