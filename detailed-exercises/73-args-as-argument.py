def func(*args):
    print(args)
    total = 0
    for i in args:
        total += i
    return total

numbers_list = [12,334,45,23,13,4,2]
numbers_tuple = (12,45,23,13,4,2)

print(func(*numbers_list)) # * unpacks list or tuple
print(func(*numbers_tuple)) # * unpacks list or tuple