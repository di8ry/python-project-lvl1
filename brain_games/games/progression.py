import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start_number = random.randint(1, 5)
    step = random.randint(1, 4)
    progression_range = 20
    progression = list(range(start_number, progression_range, step))
    answer = random.choice(progression)
    hidden_index = random.randrange(0, len(progression))
    answer, progression[hidden_index] = progression[hidden_index], '..'
    question = ' '.join(map(str, progression))
    return question, str(answer)
