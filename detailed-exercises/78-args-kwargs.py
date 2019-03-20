#args - arguments , ** 

def add(a,b):
    return a + b
 
def new_add(*args):
    # 1,2,3,4
    # (1,2,3,4), # ([])
    #gathers data as tuple
    total = 0
    for num in args:
        total += num
    return total 
 
 
print(new_add(1,2,3))

#good practice  
l = (1,2,3,4) # or l = [1,2,3,4]
print(new_add(*l))
 
#kwargs - keyword arguments , ** 
def func(**kwargs):
    # { 'name':'Imad Beyg', 'age':28 }
    # gather data as dictionary
    print(kwargs) 
    print(type(kwargs))
 
func(name = 'Imad', age = 28)
 
# kwargs , args , normal , default 
# PADK - paramter , args , default , kwargs 
 
def func2(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
 
func2('Imad', 1,2,3, last_name = 'Beyg',a = 1, b = 2)