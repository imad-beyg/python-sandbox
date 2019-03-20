from random import randint

# Number guessing game
winner_number = randint(0,10)
user_number = int(input("Guess a number: "))
if user_number == winner_number :
    print("Your answer is correct")
else:
    if user_number < winner_number :
        print("Too Low")
    else:
        print("Too High")
