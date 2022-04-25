#!/usr/bin/env python
from brain_games.games.even import get_question_and_answer
from brain_games.games.even import welcome_user


def main():
    welcome_user()
    get_question_and_answer()


if __name__ == '__main__':
    main()
