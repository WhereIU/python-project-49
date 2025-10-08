from random import randrange

from brain_games.game import conduct_rounds
from brain_games.helpers.collections import get_hiden_coll, get_progression

count_rounds = 3
min_progression_len = 5
max_progression_len = 10
max_range = 200
rule = "What number is missing in the progression?"


# -
def get_round_values():
    start_num = randrange(-max_range, max_range)
    range_num = randrange(-max_range, max_range)
    progression_len = randrange(min_progression_len, max_progression_len + 1)
    progression = get_progression(start_num, range_num, progression_len)
    missing_num_index = randrange(progression_len + 1)
    hiden_progression = get_hiden_coll(progression, missing_num_index)
    question = f"{' '.join([str(elem) for elem in hiden_progression])}"
    correct_answer = str(progression[missing_num_index])
    return question, correct_answer


def start_game():
    conduct_rounds(rule, count_rounds, get_round_values)
