import prompt


def run_games(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    print(game.DESCRIPTION)
    for _ in range(3):
        question, answer = game.get_question_and_answer()
        print('Question: {}'.format(question))
        print('Your answer: ')
        user_answer = input()
        if user_answer == answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'"
                  .format(user_answer, answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
