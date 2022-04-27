import random
import prompt


DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def welcome_user():
    print("Welcome to the Brain games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    return name


def get_question_and_answer():
    print(DESCRIPTION)
    attempts = 0
    for attempts in range(3):
        number = random.randint(1, 20)
        print('Question: ', number)
        print('Your answer(yes or no): ')
        answer = input()
        if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
            print('Correct!')
        elif number % 2 == 0 and answer == 'no':
            print("\'no\' is wrong answer ;(. Correct answer was \'yes\'. \nLet\'s try again!")
        elif number % 2 != 0 and answer == 'yes':
            print("\'yes\' is wrong answer ;(. Correct answer was \'no\'. \nLet\'s try again!")
        else:
            print('incorrect answer, try again')

