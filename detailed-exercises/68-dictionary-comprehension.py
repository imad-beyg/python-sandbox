# dictionary comprehension 
# with the help of dictionary comprehension we can create of dictionary in one line
 
# create a dictionary of squares from 1 to 10 
squares = {}
for i in range(1,11):
    squares[i] = i**2
print(squares)
 
square2 = {f"square of {i} ":i**2 for i in range(1,11)}
print(square2)
