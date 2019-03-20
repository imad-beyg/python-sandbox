# dictionary comprehension with if statement 
 
numbers = {1:1, 2:2, 3:3 ,4:4}
squares = {}

#normal way
for key in range(1,11):
    if key%2 == 0:
        squares[key] = key**2
print(squares)
 
#dictionary comprehension with if
squares2 = {key:key**2 for key in range(1,11) if key%2 == 0}
print(squares2)


even_odd = {key: 'even' if key%2 == 0 else 'odd' for key in range(1,11)}
print(even_odd)


