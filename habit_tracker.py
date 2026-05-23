import json
try :
    with open('habits.json' , 'r') as file:
        habits = json.load(file)

except:
    habits = {}

while True:
    print('\n=====HABIT TRACKER=====')
    print('1. Add Habit')
    print('2. View Habits')
    print('3. Complete Habit')
    print('4. Exit')

    choice = input('Enter your choice : ')

    if(choice == '1'):
        habit = input('Enter habit name : ')
        habits[habit] = False
        print('Habit added successfully!\n')

    elif(choice == '2'):
        if not habits:
            print('No habits found!\n')
            
        else:
            print('Your habits : \n')
            for habit , status in habits.items():
                if status:
                    print(f'{habit} : Completed')
                else:
                    print(f'{habit} : Not Completed')

    elif(choice == '3'):
        habit_name = input('Enter habit name : ')
        if habit_name in habits:
            habits[habit_name] = True
            print(f'{habit_name} completed successfully!')
        else:
            print(f'{habit_name} not found!')

    elif(choice == '4'):

        with open('habits.json' , 'w') as file:
            json.dump(habits , file)
        print('Data Saved!')
        print('Goodbye!')
        break

    else:
        print('Invalid choice')