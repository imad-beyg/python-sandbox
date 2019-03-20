# THIS IS CHALLENGE 
 
# define a function take any no of lists containing number 
# [1,2,3] , [4,5,6], [7,8,9]
# return average 
# (1+4+7)/3 , (2,5,8)/3 , (3,6,9)/3 

def list_average(*args):
    new_list = [] 
    for pair in zip(*args):
        new_list.append( sum(pair)/len(pair) )
    return new_list

average_finder = lambda *args : [ sum(pair)/len(pair) for pair in zip(*args) ]

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
print(list_average(l1,l2,l3))
print(average_finder(l1,l2,l3))