import prompt
from random import randrange
from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        question = randrange(500)    
        correct_answer = 'yes' if is_even(question) else 'no'
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print((
				f"'{user_answer}' is wrong answer ;(."
				f"Correct answer was '{correct_answer}'.\n"
				f"Let's try again, {name}!"
			))
            break
        print('Correct!')
        i += 1
    else:
        print(f'Congratulations, {name}!')
