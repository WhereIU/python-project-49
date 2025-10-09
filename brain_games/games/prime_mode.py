from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.maths import is_prime

COUNT_ROUNDS = 3
MAX_NUM = 500
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round_values():
    question = randrange(MAX_NUM + 1)
    correct_answer = "yes" if is_prime(question) else "no"
    return question, correct_answer


def start_game():
    conduct_rounds(RULE, COUNT_ROUNDS, get_round_values)
