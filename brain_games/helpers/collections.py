def get_progression(start, offset, progression_len):
    return list(
        [start + offset * index for index in range(progression_len + 1)]
    )


def get_hiden_coll(coll, index, replacer='..'):
    new_coll = [*coll]
    new_coll[index] = replacer
    return new_coll