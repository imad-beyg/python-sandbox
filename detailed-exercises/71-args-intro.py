## make flexible functions

def add(a,b):
    return a+b

print(add(4,19))

# *operator
# *args - getts all the arguments as a one tuple

def add_all(*args):
    return sum(args)

print(add_all(55,1,2,3,4,5,6,7,8,9))

