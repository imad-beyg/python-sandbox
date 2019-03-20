#Challenge
l1 = [1,3,5,7]
l2 = [2,8,9,10]
l  = []

for i in range(0,4):
    l.append((l1[i], l2[i]))

#l = [(1,2), (3,8), (5,9), (7,10)]




# *operator with zip
#convert into two lists

l1, l2 = list(zip(*l)) #unpacking
print(l1,l2)


