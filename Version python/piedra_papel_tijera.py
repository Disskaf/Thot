# juego
user_option = input('Piedra, papel o tiera => ')
computer_option = 'piedra'

if user_option == computer_option:
    print('Empate')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra gana a tijera')
        print('user gano')
    else:
        print('Papel gana a Piedra')
        print('Computer gano')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel gana a Piedra')
        print('user gano')
    else:
        print('Tijera gana a Papel')
        print('Computer gano')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('Tijera gana a Papel')
        print('user gano')
    else:
        print('Piedra gana a tijera')
        print('Computer gano')
