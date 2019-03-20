loop_number = int(input("Enter loop length: "))
inital_number = 1
answer = 0

while inital_number <= loop_number:
    answer += inital_number
    inital_number += 1

print(answer)



# problem
# ask user to input a number containing more than one digit 
# example - 1256 
# calculate 1+2+5+6 and print 
 
 
number = input("Enter digit: ")
loop_length = len(number)
inital_loop = 0
answer = 0

while inital_loop < loop_length:
    answer += int(number[inital_loop])
    inital_loop += 1

print(answer)    


name = input("Enter you full name: ")
name = name.lower()
loop_value = 0
temp_value = ""
while loop_value < len(name):
   character = name[loop_value]
   if character not in temp_value :
       temp_value +=character
       print(f" {character} : {name.count(character)}")
   loop_value += 1