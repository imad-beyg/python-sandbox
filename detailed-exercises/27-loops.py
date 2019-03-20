loop_number = int(input("Enter loop length: "))
inital_number = 1

print("While Loop")
#while loop
while inital_number <= loop_number:
    print(f"While # {inital_number}")
    inital_number += 1

print("For Loop")
#for loop with range function
for i in range(1,loop_number+1):
    print(f"{i}")

print("For Loop With Range Step")
#for loop with range function and step
for i in range(1,10,2):
    print(f"{i}")

print("For Loop With Negative Range Step")
#for loop with range function
for i in range(10,0,-1):
    print(f"{i}")

print("For Loop & String")
#for loop and string
name="imad"
for i in name:
    print(i)

#infinite loop
while False:
    print("hello world")