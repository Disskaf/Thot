# juego
import random

options = ('piedra', 'papel', 'tijera')
computer_wins = 0
user_wins = 0
rounds = 1

while True:
    print('*' * 10)
    print('ROUUND', rounds)
    print(f'USER: {user_wins} vs PC: {computer_wins	}')
    print('*' * 10)

    user_option = input('Piedra, papel o tiera => ').lower()
    computer_option = 'piedra'
    computer_option = random.choice(options)

    if not user_option in options:
        print('Esa opción no es valida')
        continue

    print('Opción del usuario => ', user_option)
    print('Opción del usuario => ', computer_option)

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
    if computer_wins == 2:
        print('El ganador es la computadora')
        break
    if user_wins == 2:
        print('El ganador es el usuario')
        break

    rounds += 1
