'''
### Task #8

✅ Triangle Classifier:


Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.

'''
# sides = list(map(int,input('Enter values with spaces: ').split(' ')))
import pytest
import random

def triangle_checker(a,b,c):
    if a==b==c:
        print(f'triangle is equiletral:{a,b,c}')
        return 'Equiletral'
    elif a==b or b==c or a==c:
        print(f'triangle is isosceles:{a,b,c}')
        return 'Isosceles'
    else:
        print(f'triangle is scalene:{a,b,c}')
        return 'Scalene'

@pytest.mark.loop(5)
def test_triangle():
    a = random.randrange(10,20,step=1)
    b = random.randrange(10, 20, step=1)
    while a==b:
        b = random.randrange(10, 20, step=1)
    c = random.randrange(10, 20, step=1)
    while a==c or b==c:
        c = random.randrange(10, 20, step=1)

    # equiletral check
    assert triangle_checker(a,a,a)=='Equiletral'
    if a!=b:
        assert triangle_checker(a,b,a)=='Isosceles'
        assert triangle_checker(a,a,b)=='Isosceles'
        assert triangle_checker(b,a,a)=='Isosceles'

        assert triangle_checker(a,b,c) == 'Scalene'

'''
command to genarate HTML Reports - 
pytest -v --html=reports\report_name.html Lab_023.py
'''