import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 0
MAX_OPERAND = 10
TOTAL_PROBLEMS = 5


def generate_problem():
    left = random.randint(MIN_OPERAND , MAX_OPERAND)
    right = random.randint(MIN_OPERAND , MAX_OPERAND)
    operator = random.choice(OPERATORS)

    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(exp)
    return exp , answer

input("Press enter to start!")
print("---------------------")
start_time = time.time()
wrong = 0
for i in range(TOTAL_PROBLEMS):

    exp , answer = generate_problem()
    while True:
        guess = input(f"Problem #{i+1} : {exp} = ")
        if guess == str(answer):
            break
        wrong+=1
end_time = time.time()
total_time = round(end_time - start_time , 2)
print("---------------------")
print(f"Well done! You finished in {total_time} seconds.")