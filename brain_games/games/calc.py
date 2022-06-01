from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    OPERATIONS = [('+', add), ('-', sub), ('*', mul)]
    number_1 = randint(1, 20)
    number_2 = randint(1, 20)
    symbol, operation = choice(OPERATIONS)
    question = "{} {} {}".format(number_1, symbol, number_2)
    answer = str(operation(number_1, number_2))
    return question, answer
