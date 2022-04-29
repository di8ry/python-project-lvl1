import random

describe_prime = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def prime():
    print(describe_prime)
    for attemps in range(3):
        a = random.randint(1, 30)
        print('Question: ', a)
        print('Your answer(yes or no): ')
        user_answer = input()
        k = 0
        for i in range(2, a // 2 + 1):
            if (a % i == 0):
                k = k + 1
        if (k <= 0) and user_answer == 'yes':
            print("Correct!")
        elif (k > 0) and user_answer == 'no':
            print('Correct!')
        else:
            print("Wrong answer, try again!")
