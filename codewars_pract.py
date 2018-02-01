# #seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
# Given an array, find the int that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# test.describe("Example")
# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

def find_it(seq):
    for i in seq:
        z = seq.count(i)
    #print(x.count(i), i)
    if z % 2 != 0:
        return i

# it's ugly but it works.
