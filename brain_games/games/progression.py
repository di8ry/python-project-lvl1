import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start_number = random.randint(1, 5)
    step = random.randint(1, 4)
    progress = range(start_number, 20, step)
    a = list(progress)
    answer = random.choice(a)
    for i in range(len(a)):
        if a[i] == answer:
            a[i] = ".."
    res = ' '.join(str(e) for e in a)
    return res, str(answer)
