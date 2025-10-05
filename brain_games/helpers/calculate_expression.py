def calculate_expression(first_num, sign, second_num):
    match sign:
        case "+":
            return str(first_num + second_num)
        case "-":
            return str(first_num - second_num)
        case "*":
            return str(first_num * second_num)
        case _:
            return "Error"

