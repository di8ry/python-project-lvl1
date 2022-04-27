import random


description_gcd = 'Find the greatest common divisor of given numbers.'


def gcd():
    print(description_gcd)
    for attemps in range(3):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        print('Question: ', number_1, number_2)
        print('Your answer: ')
        user_answer = int(input())
        while number_2 > 0:
            number_1, number_2 = number_2, number_1 % number_2
        if user_answer == number_1:
            print('Correct')
        else:
            print(user_answer, 'is wrong answer ;(. Correct answer was ', number_1, "\nLet's try again")





