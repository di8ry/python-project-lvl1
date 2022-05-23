import random


description_calc = 'What is the result of the expression?'


def get_calc():
    print(description_calc)
    for attemps in range(3):
        number_1 = random.randint(1, 20)
        number_2 = random.randint(1, 20)
        operation_list = ["+", "-", "*"]
        operation = random.choice(operation_list)
        if operation == '+':
            right_answer = number_1 + number_2
        elif operation == '-':
            right_answer = number_1 - number_2
        elif operation == '*':
            right_answer = number_1 * number_2
        print('Question:', number_1, operation, number_2)
        print('Your answer: ')
        user_answer = int(input())
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(user_answer, 'is wrong answer ;(. Correct answer was', right_answer, "\nLet's try again")
            break
    print('Game over')
