import random
user_wins = 0
computer_wins = 0
options = ["rock" , "paper" , "scissors"]
while True:
    user_choice = input("Choose rock/paper/scissors or q for quit : ").lower()
    if user_choice == "q":
        break
    elif user_choice in options:

        computer_choice = random.choice(options)
        print(f"Computer chose : {computer_choice}")

        if user_choice == "rock" and computer_choice =="scissors":
            print("You win!🥳")
            user_wins+=1
        elif user_choice == "paper" and computer_choice =="rock":
            print("You win!🥳")
            user_wins+=1
        elif user_choice == "scissors" and computer_choice =="paper":
            print("You win!🥳")
            user_wins+=1
        elif user_choice == computer_choice :
            print("It's a tie!")
        else:
            print("Computer wins!")
            computer_wins+=1
    else:
        print("Invalid choice!")
        continue
print(f"You won {user_wins} times and computer won {computer_wins} times!")
print("Goodbye!")