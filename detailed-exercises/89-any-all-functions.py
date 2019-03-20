# any , all function 
 
numbers1 = [13,1,9,7,10]
numbers2 = [1,2,3,4,5,6]


# new_list = []
# for num in numbers1:
#     if num%2==0:
#         new_list.append(True)
#     else:
#         new_list.append(False)

# print(new_list)

l = [ i%2==0 for i in numbers1 ]

#all function checks all the values are true or not
#if true return true

print(all(l))


#any function checks if atleast one value is true
#if has atleast one true returns true

print(any(l))

