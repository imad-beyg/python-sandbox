#add data into list
fruits = []
print(fruits)
fruits.append("apples")
fruits.append("mangoes")
fruits.append("grapes")
print(fruits)
fruits.insert(0, 'papaya')
print(fruits)
vegetables = ['lady finger', 'bringial']
print(fruits+vegetables) # concatinate two lists 
fruits.extend(vegetables) # adds values of vegetable list
#fruits.append(vegetables) # adds whole vegetable list
print(fruits)


#delete data from list uisng - pop method
fruits.pop() # delete last element from list

#delete data from list uisng - del operator
del fruits[0]

#delete data from list uisng - remove method
fruits.remove('grapes')

print(fruits)
