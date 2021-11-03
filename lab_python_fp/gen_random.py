from random import randint


def gen_random(quantity, minimum, maximum):
    for i in range(0, quantity):
        yield randint(minimum, maximum)
