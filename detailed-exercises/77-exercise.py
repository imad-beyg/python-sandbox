# normal function
def func(names, reverse_str = False):
    
    if reverse_str:
       names =  [name[::-1] for name in names]
    names = [name.capitalize() for name in names]
    return names

# kwargs function
def func_kwargs(names, **kwargs):

    if kwargs.get('reverse_str') == True:
       names =  [name[::-1] for name in names]
    names = [name.capitalize() for name in names]
    return names




names = ['imad', 'alex'] 

print(func(names))
print(func(names, reverse_str = True))

print(func_kwargs(names))
print(func_kwargs(names, reverse_str = True))