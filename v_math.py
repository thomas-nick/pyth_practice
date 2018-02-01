"""Linear Algebra Practice"""
c = 3
v = [1, 2, 3, 6]
w = [4, 9, 2, 1]


def vector_add(v, w):
    """vector - addition"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


def scalar_multiply(c, v):
    return[c * v_i for v_i in v]


q = vector_sum(vectors)
z = scalar_multiply(c, v)
x = vector_add(v, w)
y = vector_subtract(v, w)
print(x, y, z, q)
