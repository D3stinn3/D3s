import random

user_input = input('will chelsea win, draw or lose? ')
computer_input = str(random.choice(['win', 'draw', 'lose']))

if computer_input == user_input:
    print('you have won')
else:
    print('you have lost')


def gameplay(chelsea, manchester):
    if (chelsea == 'draw' and manchester == 'draw') or (chelsea == 'win' and manchester == 'lose') \
            or (chelsea == 'lose' and manchester == 'win'):
        return True


if gameplay(computer_input, user_input):
    print('game is working perfectly')
else:
    print('game is not working perfectly')
