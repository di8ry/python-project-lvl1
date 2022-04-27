#!/usr/bin/env python
from brain_games.games.calc import get_calc
from brain_games.games.even import welcome_user


def main():
    welcome_user()
    get_calc()


if __name__ == '__main__':
    main()