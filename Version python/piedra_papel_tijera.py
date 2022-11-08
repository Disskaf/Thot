# juego
import random


def choice_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Piedra, papel o tiera => ').lower()

    if not user_option in options:
        print('Esa opción no es valida')
        return None, None

    computer_option = random.choice(options)

    print('Opción del usuario => ', user_option)
    print('Opción del usuario => ', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('user gano')
            user_wins += 1
        else:
            print('Papel gana a Piedra')
            print('Computer gano')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a Piedra')
            print('user gano')
            user_wins += 1
        else:
            print('Tijera gana a Papel')
            print('Computer gano')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a Papel')
            print('user gano')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('Computer gano')
            computer_wins += 1
    return user_wins, computer_wins


def winner(user_wins, computer_wins):
    if computer_wins == 2:
        print('El ganador es la computadora')
        exit()

    if user_wins == 2:
        print('El ganador es el usuario')
        exit()


def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1

    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print(f'USER: {user_wins} vs PC: {computer_wins	}')
        print('*' * 10)

        user_option, computer_option = choice_options()
        user_wins, computer_wins = check_rules(
            user_option, computer_option, user_wins, computer_wins)
        winner(user_wins, computer_wins)
        rounds += 1


run_game()
