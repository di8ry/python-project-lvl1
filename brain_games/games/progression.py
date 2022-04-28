import random


description_prog = 'What number is missing in the progression?'


def progression():
    print(description_prog)
    for attemps in range(3):
        start_number = random.randint(1, 5)
        step = random.randint(1, 4)
        progress = range(start_number, 20, step)
        a = list(progress)
        miss_number = random.choice(a)
        for i in range(len(a)):
            if a[i] == miss_number:
                a[i] = ".."
        print('Question: ', *a)
        user_answer = int(input())
        if user_answer == miss_number:
            print('Correct!')
        else:
            print(user_answer, 'is wrong answer ;(. Correct answer was ', miss_number, "\nLet's try again")




