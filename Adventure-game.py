name = input("Enter your name: ")

while True:
    play = input("Do you want to play? 🤗 (yes/no): ").lower()
    if play == "yes":
        print("Game starts in 3... 2... 1 ...")
    elif play == "no":
        break
    else:
        print("Invalid choice!")
        continue

    path1 = input("\nYou are struggling on a muddy road! 😣 You can go either left or right.\nWhich way do you choose? (left/right): ").lower()

    if path1 == "left":
        path2 = input("\nYou go left and come across a river and a jungle. 🌊🌴\nYou can swim across the river 🏊‍♀️ or walk through the jungle 🎍.\nWhich way do you choose? (swim/walk): ").lower()
        if path2 == "swim":
            print(f"\nYou swam across 🏊‍♀️ the river and got strangled by an octopus 🐙.\nYOU LOST {name}! 😪")
            break
        elif path2 == "walk":
            print(f"\nYou walked through the jungle 🎍 and got slapped by an orangutan 🦧.\nYOU LOST {name}! 😪")
            break
        else:
            print(f"\nInvalid choice 🙄. YOU LOST {name}! 😵")
            break

    elif path1 == "right":
        path3 = input("\nYou go right and come across a bridge and a deserted temple. 🛤🛕\nYou can cross the bridge or walk to the temple.\nWhich way do you choose? (cross/walk): ").lower()
        if path3 == "cross":
            print(f"\nYou cross halfway through the bridge, the bridge wobbles, and you fall.\nYOU LOST {name}! 😪")
            break
        elif path3 == "walk":
            path4 = input("\nYou walk to the temple and find a shabby stranger 🥴!\nYou can talk to him or ignore him.\nWhich do you choose? (talk/ignore): ").lower()
            if path4 == "ignore":
                print(f"\nYou ignore the stranger, he gets angry 👿 and burns you to ashes 🔥.\nYOU LOST {name}! 😪")
                break
            elif path4 == "talk":
                print(f"\nYou talk to the stranger, he gets pleased 😊 and teleports you home.\nYOU WIN {name}!! 🥳🥳🥳")
                break
            else:
                print(f"\nInvalid choice 🙄. YOU LOST {name}! 😵")
                break
        else:
            print(f"\nInvalid choice 🙄. YOU LOST {name}! 😵")
            break
    else:
        print(f"\nInvalid choice 🙄. YOU LOST {name}! 😵")
        break

print("\nGOODBYE! 👋")
