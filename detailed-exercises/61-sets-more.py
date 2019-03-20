s1 = {1,2,3,4}
s2 = {2,4,5,6,7}


if 4 in s1:
    print('present')

for item in s1:
    print(item)


#union
union_set = s1 | s2
print(union_set)

#intersection
intersection_set = s1 & s2
print(intersection_set)