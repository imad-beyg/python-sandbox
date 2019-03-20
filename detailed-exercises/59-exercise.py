user = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
favourite_songs = input ("Enter your favourite songs (comma seperated): ").split(',')
favourite_movies = input("Enter your favourite movies (comma seperated): ").split(',')




user['name'] = name
user['age'] = age
user['favourite_movies'] = favourite_movies
user['favourite_songs'] = favourite_songs

print(user)


for key, value in user.items():
    print(f"{key} : {value}")