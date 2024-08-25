
# Task #10 -
# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24
#
# running tests -
# pytest -v src\ex_24082024\Lab027.py
#


import pytest
import math
import random
# factorial usng for loop
def factorial_for(num):
    if num==0:
        return 1
    val = 1
    for i in range(1,num+1):
        val*=i
    return val

def factorial_while(num):
    if num==0:
        return 1
    i = 1
    while(num>0):
        i*=num
        num-=1
    return i

def factorial_recursion(num):
    print(f'{num} is being tested')
    if num==1 or num==0:
        return 1
    else:
        return num * factorial_recursion(num-1)




@pytest.mark.loop(10)
# unit testing for the methods
def test_factorial_for():
    val = random.randint(0,1023)
    assert math.factorial(val)==factorial_for(val)


@pytest.mark.loop(100)
def test_factorial_while():
    val = random.randint(0,1023)
    assert math.factorial(val)==factorial_while(val)

print(factorial_recursion(0))

@pytest.mark.loop(100)
def test_factorial_recursion():
    val = random.randint(0,1023)
    try:
        assert math.factorial(val)==factorial_recursion(val)
    except Exception as e:
        print(e)