"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive)

"""
import random
from random import randrange

def rand7():
    return  random.choice([2 + randrange(1, 6),  randrange(1, 6)])
print(rand7())
