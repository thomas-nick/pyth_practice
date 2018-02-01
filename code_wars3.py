numbers = [0, 3, 4, 5]
# x = [i ** 2 for i in a]
# print(x)
# print(sum(x))


def square_sum(numbers):
    # your code here
    x = [i ** 2 for i in numbers]
    return sum(x)


print(square_sum(numbers))
