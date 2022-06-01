from random import randint
from math import sqrt, ceil

DESCRIPTION = \
    'Answer "yes" if given number is prime.'\
    ' Otherwise answer "no".'


def is_prime(number):
    for i in range(2, ceil(sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(2, 1000)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
