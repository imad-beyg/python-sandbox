name, age = input("Enter your name and age (comma seperated) : ").split(",")
age = int(age)
if name[0].lower() == "a" and age > 10 :
    print("You can watch coco movie")
else :
    print("Sorry ! You can't see movie")