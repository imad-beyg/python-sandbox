# set data type
# unordered collection of unique items 
# cannot store list or dictionary in sets
 
s = {1,2,3}
s = {1,1.1, 2.3, 'string'}
 


# remove duplicates from list using set

l = [1,2,3,4,5,5,5,5,6,7,7,8]
s2 = list(set(l))
#print(s2)



# add data to set
s.add(3)
s.add(4)
s.add(5)
s.add(4)


#remove data from set - gives error if item doesn't exist
s.remove(3)

#discard data from set- doesn't give error if item doesn't exist
s.discard(5)

#copy set
s1 = s.copy()

#clear set
s.clear()


print(s1)
print(s)