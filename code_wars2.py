arr = [78, 56, 232, 12, 11, 43]


def findSmallestInt(arr):
    # Code here
    a = sorted(arr)
    return a[0]


x = findSmallestInt(arr)
print(x)
