'''

### Task #9

✅ FizzBuzz Test:

Write a program that prints numbers from 1 to 100. # Loop For

However, for multiples of 3, print "Fizz" instead of the number, and

for multiples of 5, print "Buzz."

For numbers that are multiples of both 3 and 5, print "FizzBuzz."
'''

import pytest
import random

def fizzbuzz(num):
    if num%3==0:
        if num%5==0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    elif num%5==0:
        return 'Buzz'
    else:
        return num



@pytest.mark.loop(20)
def test_fizzbuzz():
    num = random.randrange(100)
    print(f'{num} is being tested')
    if num%3==0 and num%5==0:
        assert fizzbuzz(num)=='FizzBuzz'
        print(f'{num} is FizzBuzz')
    elif num%3==0:
        assert fizzbuzz(num)=='Fizz'
        print(f'{num} is Fizz')
    elif num%5==0:
        assert fizzbuzz(num)=='Buzz'
        print(f'{num} is Buzz')
    else:
        assert fizzbuzz(num)==num
        print(f'{num} is num')

