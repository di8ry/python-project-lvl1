import prompt


def run_games(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    print(game.DESCRIPTION)
    raunds_count = 3
    for _ in range(raunds_count):
        question, answer = game.get_question_and_answer()
        print('Question: {}'.format(question))
        print('Your answer: ')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'"
                  .format(user_answer, answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
