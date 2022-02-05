def calc_sum(a, b):
    return a + b


def calc_multiple(a, b):
    return a * b


def calc_subtract(a, b):
    return a - b


def calc_division(a, b):
    if b == 0:
        return 0

    return a / b


def calc_absolute(a):
    if a < 0:
        return 0 - a
    return a


def calc_odd_even(a):
    if a % 2 == 0:
        return 'even'
    return 'odd'
