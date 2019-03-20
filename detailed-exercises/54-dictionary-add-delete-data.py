user_info = {
    'name' : 'imad',
    'age' : 24,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}
# add new key and its value
user_info['marital_status'] = "married"
print(user_info) 

#pop method
poped_item = user_info.pop('marital_status')
print(poped_item) 
print(user_info) 


#popitem method
poped_item = user_info.popitem()
print(poped_item)
print(user_info) 


