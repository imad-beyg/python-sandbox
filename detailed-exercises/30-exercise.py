from random import randint

random_number = randint(1,10)
total_attempts = 0
wrong_attempt = 0
user_answer = int(input("Guess a number between 1-10: "))

while True:
    total_attempts +=1
    user_answer = int(input("Guess agian between 1-10: "))
    if(user_answer == random_number):
        print(f"You Won in {total_attempts} attempts")
        break
    else:
        wrong_attempt += 1
        if user_answer < random_number:
            print("Too Low Value")
        else :       
            print("Too High Value")