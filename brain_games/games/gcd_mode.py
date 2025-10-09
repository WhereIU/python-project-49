from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.maths import get_gcd

COUNT_ROUNDS = 3
MAX_RANGE = 100
RULE = "Find the greatest common divisor of given numbers."


def get_round_values():
    first_num = randrange(MAX_RANGE)
    second_num = randrange(MAX_RANGE)
    question = f"{first_num} {second_num}"
    correct_answer = str(get_gcd(first_num, second_num))
    return question, correct_answer


def start_game():
    conduct_rounds(RULE, COUNT_ROUNDS, get_round_values)
