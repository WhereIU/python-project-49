from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.maths import get_gcd

count_rounds = 3
max_range = 100
rule = "Find the greatest common divisor of given numbers."


def get_round_values():
    first_num = randrange(max_range)
    second_num = randrange(max_range)
    question = f"{first_num} {second_num}"
    correct_answer = str(get_gcd(first_num, second_num))
    return question, correct_answer


def start_game():
    conduct_rounds(rule, count_rounds, get_round_values)
