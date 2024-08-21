'''
### Task #7

✅ Leap Year Checker:


![img_1.png](img_1.png)


Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.
'''
import pytest
from faker import Faker

def leap_checker(year):
    # year= int(input('Enter the year:'))
    if year% 400 == 0:
        print('year is a leap year')
        return 1
    elif year% 100 == 0:
        print('year is not a leap year')
        return 0
    elif year % 4 == 0:
        print('year is a leap year')
        return 1
    else:
        print('year is not a leap year')
        return 0

@pytest.mark.loop(5)
def test_leap():
    fake = Faker()
    year = int(fake.year())
    print(f'{year}is being tested')
    try:
        assert bool(leap_checker(year)) == True
    except AssertionError as e:
        print(f'Exception occurred:{e}')
        assert bool(leap_checker(year)) == False
'''
way 1 -
pytest --loop=10 test_file.py
way 2  - 
@pytest.mark.loop(5)
'''
# for i in range(10):
#     test_leap()