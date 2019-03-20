# iterator vs iterables 
 
numbers = [1,2,3,4] # , tuples, string --- iterables 
squares = map(lambda a:a**2, numbers) # iterator 
 

numbers_iter = iter(numbers)
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter)) # will give an error

for i in numbers:
    print(i)


print(next(squares))
