# Guessing Game
import random
top_of_range = input("Enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0 , next time!")
        quit()
else:
    print("Please enter a number next time!")
    quit()
random_num = random.randint(1,top_of_range)
guesses = 0
while True:
    guesses+=1
    
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Guess a number!")
        continue
    if user_guess>random_num:
        print("Your guess is higher than the number!")
    elif user_guess == random_num:
        print("Your guess is correct!🎉")
        break
    else:
        print("Your guess is lower than the number!")

print(f"You took {guesses} guesses to win.")