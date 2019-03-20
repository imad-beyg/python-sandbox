# list comprehension with if statement 
 
numbers = list(range(1,11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = [2,4,6]

#normal way
nums = []
for i in numbers:
    if i%2 == 0:
        nums.append(i)
print(nums)
 
#list comprehension with if
even_nums = [i for i in numbers if i%2 == 0]
even_num2 = [i for i in range(1,11) if i%2 == 0]
odd_nums = [i for i in range(1,11) if i%2 != 0]

print(even_nums)
print(even_num2)
print(odd_nums)