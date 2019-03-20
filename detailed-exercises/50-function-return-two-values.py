def func(a, b):
    add = a+b
    multiply = a*b
    return add,multiply # returning a tuple

add, multiply = func(4,7)
print(func(5,2))

