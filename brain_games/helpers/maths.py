def is_even(number):
    return number % 2 == 0


def calculate_expression(first_num, sign, second_num):
    match sign:
        case "+":
            return first_num + second_num
        case "-":
            return first_num - second_num
        case "*":
            return first_num * second_num
        case _:
            return "Error"


def get_gcd(first_num, second_num):
    if first_num == second_num:
        return first_num

    sorted_nums = [first_num, second_num]
    sorted_nums.sort()

    if (sorted_nums[1] % sorted_nums[0] == 0):
        return sorted_nums[0]

    for possible_divisor in range(
        int((sorted_nums[1]) ** 0.5 + 1),
        1, -1):
        if (sorted_nums[0] % possible_divisor == 0) and (
            sorted_nums[1] % possible_divisor == 0):
            return possible_divisor

    return 1
