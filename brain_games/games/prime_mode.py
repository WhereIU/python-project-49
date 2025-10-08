from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.maths import is_prime

count_rounds = 3
max_range = 500
rule = 'nswer "yes" if given number is prime. Otherwise answer "no".'


def get_round_values():
    question = randrange(max_range)
    correct_answer = "yes" if is_prime(question) else "no"
    return question, correct_answer


def start_game():
    conduct_rounds(rule, count_rounds, get_round_values)
