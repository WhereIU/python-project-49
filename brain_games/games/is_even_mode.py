from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.maths import is_even

count_rounds = 3
max_range = 500
rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round_values():
    question = randrange(max_range)
    correct_answer = "yes" if is_even(question) else "no"
    return question, correct_answer


def start_game():
    conduct_rounds(rule, count_rounds, get_round_values)
