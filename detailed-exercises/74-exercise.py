# define a function 
# input 
 
# num , iterable(tuple , list)containing numbers as args
 
# example 
# nums = [1,2,3]
# to_power(3,*nums)
 
# output 
# list ---> [1, 8, 27]
 
# if user didn't pass any args then give a user a message 'hey you didn't pass
# args 
 
# else
# return list 
 
# NOTE - USE list comprehension



def to_power(num, *args):
    if args:
        return [arg**num for arg in args]
    else:
        return "Input error"

nums = [ number for number in range(1,11)]
#nums = []
print(to_power(3,*nums))