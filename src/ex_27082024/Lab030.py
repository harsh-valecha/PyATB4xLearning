def make_pizza(*topping,base):
    print(topping,base)


# make_pizza('mushroom','tomato' , base='thin crust')

# rule - args should be first parameter , then keyword args

# function scope
global_b= 12 # almost work like global variable

def f():
    a = 10 # local variable
    print(a)
    print(global_b)

f()
print(global_b) # global variable available every where


