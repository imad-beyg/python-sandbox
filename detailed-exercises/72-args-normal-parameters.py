def func(name, *args):
    return name, sum(args)


name, add = func('imad',3,4,4,56,6,6)
print(name)
print(add)