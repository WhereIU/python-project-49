from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.maths import calculate_expression

count_rounds = 3
max_range = 500
signs = ["+", "-", "*"]
signs_len = len(signs)
rule = "What is the result of the expression?"


def get_round_values():
    first_num = randrange(max_range)
    sign = signs[randrange(signs_len)]
    second_num = randrange(max_range)
    question = f"{first_num} {sign} {second_num}"
    correct_answer = str(calculate_expression(first_num, sign, second_num))
    return question, correct_answer


def start_game():
    conduct_rounds(rule, count_rounds, get_round_values)
