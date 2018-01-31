"""Linear Algebra Practice"""


def vector_add(v, w):
    """vector - addition"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]


v = [1, 2, 3, 6]
w = [4, 9, 2, 1]

x = vector_add(v, w)
y = vector_subtract(v, w)
print(x, y)
