import json
try:
    with open('expenses.json','r') as file:
        expenses = json.load(file)
except:
    expenses = []

while True:
    print('\n=====EXPENSE MANAGER=====')
    print('1. Add Expense')
    print('2. View Expense')
    print('3. Show Total')
    print('4. Exit')

    choice = input("Enter your choice : ")
    if choice == '1':
        while True:
            try:
                amount = float(input('Enter amount : '))
                break
            except:
                print('Enter a valid number!')

        category = input('Enter category : ')
        description = input('Enter description : ')
        expense = {
            'amount' : amount,
            'category' : category,
            'description' : description
        }
        expenses.append(expense)
        with open('expenses.json' , 'w') as file:
            json.dump(expenses , file , indent= 4)
        print('Expense Added Successfully!')

    elif choice == '2':
        if len(expenses)==0:
            print('Nothing to show!')
        else:
            print('\n=====Expense List=====')
            for expense in expenses:
                print(f'Amount : {expense['amount']}')
                print(f'Category : {expense['category']}')
                print(f'Description : {expense['description']}')
                print('-----------------------')

    elif choice == '3':
        total = 0
        for expense in expenses:
            total += expense['amount']
        print(f'Total Expense : {total}')

    elif choice == '4':
        print('Goodbye!')
        break