#check more than one condition at a time
age = input("Enter your age : ")
age = int(age)

if age > 0 and age < 25 : 
    print("Enjoy the life")
elif age == 25 :
    print("Golden time")    
else :
    print("Work Harder")   

second_condition = "true"

if age > 25 or second_condition == "false":
    print("Second conition is true")
    