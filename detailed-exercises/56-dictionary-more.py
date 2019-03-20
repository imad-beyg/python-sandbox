##fromkeys

#d = {'name' : 'unknown', 'age' : 'unknown'}

#with list
d = dict.fromkeys(['name','age','height'], 'test')
print(d)

#with tuple
d = dict.fromkeys(('name','age','height'), 'test')
print(d)

#with string
d = dict.fromkeys("imad", 'test')
print(d)

##copy
#d1 = d means just copy locations
d1 = d.copy()
print(d1)

##clear

d.clear()
print(d)
