user_info = {
    'name' : 'Imad',
    'age' : 24,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}
# check if key exists in dictionary
if 'name' in user_info:
    print('yes')
else:
    print('no')


# check if value exists in dictionary
if 'Imad' in user_info.values():
    print('yes')
else:
    print('no')

# loops in dictionaries

# will print only keys
for i in user_info:
    print(i) 

# will print only values
for i in user_info.values():
    print(i) 

#values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

#keys method
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

#loops with keys and values
for i in user_info:
    print(i) #key
    print(user_info[i]) #value 

#items method
user_items = user_info.items()
# turns dictionary items in tupple sets. 
print(user_items)
print(type(user_items))

#items and for 
for key, value in user_info.items(): # here it does tupple unpacking as .items() returns dictionary with tuples
    print(f"{key} : {value}")
