

## get method (useful)

user_info = {
    'name' : 'imad',
    'age' : 24,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

print(user_info['name'])
print(user_info.get('name'))
print(user_info.get('names')) # as 'names' key doesn't exist it will return "None"
print(user_info.get('names','key not found')) # as 'names' key doesn't exist it will return "key not found" string


