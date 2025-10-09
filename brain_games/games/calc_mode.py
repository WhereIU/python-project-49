from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.maths import calculate_expression

COUNT_ROUNDS = 3
MAX_NUM = 500
SIGNS = ["+", "-", "*"]
SIGNS_LEN = len(SIGNS)
RULE = "What is the result of the expression?"


def get_round_values():
    first_num = randrange(MAX_NUM + 1)
    sign = SIGNS[randrange(SIGNS_LEN)]
    second_num = randrange(MAX_NUM + 1)
    question = f"{first_num} {sign} {second_num}"
    correct_answer = str(calculate_expression(first_num, sign, second_num))
    return question, correct_answer


def start_game():
    conduct_rounds(RULE, COUNT_ROUNDS, get_round_values)
