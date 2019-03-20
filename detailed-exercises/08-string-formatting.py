name = "imad"
age = 26
print("hello " + name + " your age is " + str(age))  # ugly syntax
# string formatting
# python 2
# python 3
# python 3.6 (best)
 
print("hello {} your age is {} ".format(name, age + 2)) # python 3
 
# 3.6 and onwards
print(f"hello {name} your age is {age + 2}")  # clean - use "f"