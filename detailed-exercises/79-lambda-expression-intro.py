#lambda expression - feature adoped by other languages like java, c++ and other languages
#anonymous function
#new way of writing functions

def add(a,b):
    return a+b

add2 = lambda a,b : a + b

multiply = lambda a,b : a * b

print(add(4,5))
print(add2(4,5))
print(multiply(2,8))

#check names of function in memory
#lambda functions has no name in the memory
print(add)
print(add2)
print(add2)