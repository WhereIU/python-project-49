from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.collections import get_hiden_coll, get_progression

COUNT_ROUNDS = 3
MIN_PROGRESSION_LEN = 5
MAX_PROGRESSION_LEN = 10
MAX_NUM = 200
RULE = "What number is missing in the progression?"


# -
def get_round_values():
    start_num = randrange(-MAX_NUM, MAX_NUM + 1)
    range_num = randrange(-MAX_NUM, MAX_NUM + 1)
    progression_len = randrange(MIN_PROGRESSION_LEN, MAX_PROGRESSION_LEN + 1)
    progression = get_progression(start_num, range_num, progression_len)
    missing_num_index = randrange(progression_len + 1)
    hiden_progression = get_hiden_coll(progression, missing_num_index)
    question = f"{' '.join([str(elem) for elem in hiden_progression])}"
    correct_answer = str(progression[missing_num_index])
    return question, correct_answer


def start_game():
    conduct_rounds(RULE, COUNT_ROUNDS, get_round_values)
