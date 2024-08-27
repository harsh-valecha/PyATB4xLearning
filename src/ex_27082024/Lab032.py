# function within function

def outer_function():
    var1 = 30

    def inner_function():
        print(var1)

    def inner_function2():
        print(var1)

    inner_function()
    inner_function2()

# outer_function()

shopping_list = ['milk','bread']

def bring_my_food(my_list):
    my_list.append('bhajia')
    return my_list

print(shopping_list)
print(bring_my_food(shopping_list))
print(shopping_list)