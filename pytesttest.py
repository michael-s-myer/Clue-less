def product(x, y):
    return x * y


a = 7
b = 2
y = product(a, b)

print y


def test_answer():
    assert product(2, 3) == 6
