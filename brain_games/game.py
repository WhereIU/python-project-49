import prompt

from brain_games.helpers.cli import welcome_user


def conduct_rounds(rule, count_rounds, get_round_values):
    name = welcome_user()
    i = 0

    print(rule)
    while i < count_rounds:
        question, correct_answer = get_round_values()
        print(f"Question: {question}")
        user_answer = (prompt.string("Your answer: ")).strip()
        if user_answer != correct_answer:
            print(
                (
                    f"'{user_answer}' is wrong answer ;(."
                    f"Correct answer was '{correct_answer}'.\n"
                    f"Let's try again, {name}!"
                )
            )
            break
        print("Correct!")
        i += 1
    else:
        print(f"Congratulations, {name}!")
