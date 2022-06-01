from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    if number2 == 0:
        return abs(number1)
    remainder = number1 % number2
    if remainder == 0:
        return abs(number2)
    return gcd(number2, remainder)


def get_question_and_answer():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    question = "{} {}".format(number1, number2)
    answer = str(gcd(number1, number2))
    return question, answer
