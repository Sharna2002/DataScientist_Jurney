from functools import partial

def power(base,exp):
    return base**exp
square = partial(power, e = 2)

print(square(8))