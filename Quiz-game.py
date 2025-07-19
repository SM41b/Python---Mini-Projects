# Quiz Game
print("Welcome to the quiz game!😀")
name = input("Enter your name : ")
play = input("Do you want to play ? ").lower()
if play!="yes":
    print(f"See you next time {name}🤗")
    quit()
else:
    print("Okay ! Let's play...")
score = 0
quiz1 = input("Who is the Father of the Computer? ")
if quiz1.title()=="Charles Babbage":
    print("Correct! 🥳")
    score+=20
else:
    print("Incorrect! 😰")

quiz2 = input("What is the full form of E-Mail? ")
if quiz2.title()=="Electronic Mail":
    print("Correct! 🥳")
    score+=20
else:
    print("Incorrect! 😰")

quiz3 = input("What is the name of the computer language that is directly understood by the computer's CPU?  ")
if quiz3.title()=="Machine Language":
    print("Correct! 🥳")
    score+=20
else:
    print("Incorrect! 😰")

quiz4 = input("What does URL stand for? ")
if quiz4.title()=="Uniform Resource Locator":
    print("Correct! 🥳")
    score+=20
else:
    print("Incorrect! 😰")

quiz5 = input("What is the name of the software that manages the computer's hardware and software?  ")
if quiz5.title()=="Operating System":
    print("Correct! 🥳")
    score+=20
else:
    print("Incorrect! 😰")

print(f"{name} your score is {score}.")

if score == 100:
    print(f"🎉 Outstanding {name} , You're a tech genius!")
elif score >= 60:
    print(f"👍 Good job {name} , You know your basics!")
else:
    print(f"😅 Keep learning {name} and try again!")
