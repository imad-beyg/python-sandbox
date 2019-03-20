# map function 
 
numbers = [1,2,3,4]
 
 #normal function
def square(a):
    return a**2

#procederal way
new_list = []
for num in numbers:
    new_list.append(square(num))
 
print(new_list)

 #lamda expression
squares = list(map(lambda a:a**2, numbers))
print(squares)
 
# list comp 
squares_new = [i**2 for i in numbers]
print(squares_new)
 

 
names = ['abc', 'abcd', 'abcde']
lengths_map = map(len, names) # on map object you can iterate it once. 
length = list(lengths_map) # its better to convert it in list so that you can iterate more than once

print(lengths_map)
print(length)