from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.maths import is_even

COUNT_ROUNDS = 3
MAX_NUM = 500
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round_values():
    question = randrange(MAX_NUM + 1)
    correct_answer = "yes" if is_even(question) else "no"
    return question, correct_answer


def start_game():
    conduct_rounds(RULE, COUNT_ROUNDS, get_round_values)
