# num to string 
# define a function 
 
# example 
# input ----->  [True, False , [1,2,3], 1, 1.0, 3] 
# output ------> ['1', '1.0', '3']

def func(input_list):
    return [str(input_item) for input_item in input_list if type(input_item) == int or type(input_item) == float]
    

input_list = [ True, False, 1, 4, ('a',5), [4,6,99],9.67]
print(func(input_list))