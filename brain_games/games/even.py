import random
import prompt


DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    return name


def get_question_and_answer():
    number = random.randint(1, 100)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer
