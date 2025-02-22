import random

# Variables 
random_number = 0
rules = 'no'
health = 100
day = 0

# Game name
print (' __________________________________________ ')
print ('|                                          |')
print ('|                PILTARIS                  |')
print ('|                                          |')
print ('|__________________________________________|')
start = input('Do you want to start playing: Y/N ?')

# The player said yes and the game starts
if start == 'Y' or start == 'y':
    player = input("Welcome to the game of life, what is your name: ")
    print('\n')
    print(f'Okay, that\'s a nice name {player}')
    print('What type of companion do you want?')
    print('Dog or Robot?')
    AItype = input('Type D for dog, R for robot: ')
    AI = input('What will be the name of your companion: ')
    print('\n' * 3)
    
    while rules == 'no':
        print('The rules of the game are simple but very important. Here is how it works:')
        print('1. You will have to make choices that will impact the outcome of the story.')
        print('2. For each choice, you will need to pick a number between 0 and 9.')
        print('3. A random number will be drawn between 0 and 9.')
        print('4. The consequences of your choice depend on the comparison between your number and the drawn number:')
        print('5. The game will continue with new choices and challenges until you reach the end of the adventure.')
        print('6. Choose wisely, as each decision will affect your progress and survival.')
        regle = input(f'Did you understand the rules, {player}? Yes or no? ')


    if rules == 'yes':
        print('\n' * 50)
        print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⣀⣀⣀⣀⣀⣀⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣶⣮⡉⠉⠀⠀⠀⠀⠀⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⢚⣫⣵⣾⣿⣛⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠋⣡⡿⢻⣿⣯⣀⠀⠀⠉⢧⠹⣿⣽⣆⠀⠀⠀⢸⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⢁⣴⢿⣿⣷⣏⣿⡿⠻⢷⡀⠀⡜⢠⡿⠀⢻⣷⡀⠀⡏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⠀⠀⠈⠛⠶⣏⡘⣿⠋⠀⠀⠈⣿⢞⣵⠏⠀⠀⠀⠹⣷⡼⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⡤⠚⠛⠯⢏⡶⣤⡀⠀⠈⠙⢮⡁⠒⠂⢉⣠⠟⠁⠀⠀⠀⠀⠀⣿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠚⠉⠁⠀⢀⡼⢥⣄⡀⠀⠀⠈⣻⣿⣷⣄⠀⠀⠙⢦⡴⠟⠁⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⣠⢊⢟⡿⡒⢬⣱⣶⣾⠋⠀⠑⢿⡳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⢀⣀⣴⣁⠎⢮⠞⣴⠟⣩⣿⣍⠢⡀⠀⠀⠙⢭⢦⡀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠋⠀⢀⠔⠊⠉⠁⣼⣁⠀⠉⣳⠞⢁⡴⠟⡡⣪⠷⣜⢦⡀⠀⠈⢫⣻⡄⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡞⠀⢀⡴⠁⠀⠀⠀⢰⠁⠀⢉⡟⣡⡔⠛⠳⡨⠛⡡⢂⠌⢣⡱⡄⠀⠀⣷⢺⡀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠉⠉⠉⠀⢀⠴⠶⣆⡉⠉⡹⢋⠞⢧⡙⢦⡀⠈⠢⡀⠁⢊⡥⢙⣜⡦⠚⢹⣯⡷⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢺⣀⠤⠒⢩⢏⣴⠋⠀⠀⠘⢦⠙⢄⠀⠙⡄⠩⢔⡵⠛⠀⠀⢸⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠚⠁⠀⣀⡸⠋⠀⠑⢄⠀⠀⠀⠱⡈⢣⠀⠸⡖⠁⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⠵⣄⣴⣊⡁⠀⠀⠀⡀⠀⠳⡀⠀⠀⡇⠀⢇⠀⡇⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢉⡸⠟⠁⢀⣸⠀⠀⠀⠀⡇⠀⠀⠘⣆⠸⠧⠤⠞⠚⡇⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡴⠋⠀⠀⢐⡿⠃⠀⠀⢀⡼⠁⠀⠀⡰⠙⣿⠀⠀⠀⢠⠁⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⡿⠃⠀⠀⣞⡠⠄⠚⢿⠋⠀⠀⢀⡼⠅⠤⠃⠀⢀⡴⠃⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡹⠁⠀⠀⠀⣻⡆⢠⡄⣸⣞⡿⠔⠉⠀⠀⠀⢠⠖⠁⠀⢀⡴⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠃⡠⠔⠺⠯⠿⠷⠻⠋⠁⠀⠀⠀⠀⠀⠀⠀⢸⢀⡠⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        ''')
        input (f'{player} : Base 4578 !! do you copy?!')
        print('\n')
        input ('... ... ... ... ...')
        print('\n')
        input (f'{player} : We went through the black hole 2134 but we are not in the right place, we are heading at full speed towards a planet!')
        print('\n')
        if AItype.lower() == 'd':
            input('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀  ⠀⣴⣻⠟⠛⠛⠳⣯⡓⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⢀⣞⡿⠋⠀⠀⠀⠀⠀⠻⣮⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⢴⣿⣭⣭⣟⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠁⠀⠀⠀⠀⡀⠀⠀⠘⢷⡹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣻⠟⠁⠀⠀⠈⠻⢦⡑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣞⡾⠁⠀⠀⠀⠀⢠⡿⠀⠠⠀⠈⢷⡹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣸⣳⠏⠀⠀⠀⠀⠀⠀⠈⠹⣦⡓⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣞⣾⠁⠀⠀⠀⠀⢀⣿⠃⢀⠁⠠⡀⠈⣷⣹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣯⡟⠀⠀⠀⣤⠀⠀⠀⠀⠀⠈⠻⣮⡣⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⣼⠃⠀⠀⠀⠀⠀⣼⡟⢀⠠⠐⠀⢡⠀⠘⣷⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⠃⠀⣴⠀⠹⣷⡀⠀⠀⠀⠀⠀⠈⢷⣜⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠏⠀⠀⠀⠀⠀⢰⣿⠀⠄⠂⠐⡈⠀⢃⠀⢹⣎⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡟⣿⠀⠀⠏⠀⡀⠻⣷⡀⠀⠀⠀⠀⠀⠈⢻⣌⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣏⡿⠀⠀⠀⠀⠀⠀⣸⡟⠀⠰⠀⠂⠡⢀⠸⡀⠈⣿⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣟⡏⠀⣠⠂⠐⠀⡀⠙⣿⡄⠀⠀⠀⠀⠀⠀⠙⣧⡳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠃⠀⠀⠀⠀⠀⠀⣿⠇⡂⠁⠄⡁⠐⠠⠀⢡⠀⠸⣏⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡇⠀⣟⠀⠠⠁⠀⠄⡈⢿⣆⠐⠀⠀⠀⠀⠀⠈⢿⡜⢦⣀⣤⢴⣖⣶⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣿⠀⡇⠈⡐⠀⠌⠐⠠⠘⡆⠀⢿⣼⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡇⠀⡯⠀⢂⠠⠁⠠⠀⠌⢿⣆⠀⠀⠀⠀⠀⠀⣀⣿⣾⡿⠛⠋⠉⠉⢹⡄⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⣠⣐⡀⠁⠌⠠⢁⠀⢣⠀⠸⣏⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡇⠀⢃⠐⠀⠄⠠⠁⡐⠈⡈⣿⡆⠀⠀⢀⣴⠿⠛⠉⢸⡇⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⢟⠛⢻⡧⠐⠈⡐⠠⢀⠂⠆⠀⣿⣽⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡇⠀⠀⠂⢈⠀⢂⠐⠀⢂⠐⢸⣧⠀⠀⠀⠀⠀⠐⠀⢸⡁⠀⠀⠀⠀⠈⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣧⣴⣤⡀⠂⢂⠀⡃⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣿⡇⠀⠀⠡⠀⠂⠄⠂⢡⣾⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠋⠉⠉⣿⡇⠀⠡⠀⢸⠀⠈⣧⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡿⣿⠀⠠⠁⠐⠠⠐⠠⡘⢿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⢈⠐⠠⠈⠀⠀⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⠀⠀⡃⢀⠂⠀⣿⡿⠛⠿⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⢀⠈⠄⠐⡀⠀⢼⡾⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⣿⡇⠀⡇⠀⡀⠂⢹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⢀⣾⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠈⢿⡄⠢⠐⠠⠀⠀⢸⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣧⠀⠰⠀⠠⠐⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣾⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠘⢿⣄⠂⠐⠀⠀⣼⢧⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣿⣿⠀⠘⠄⠐⠀⠌⢠⡿⠀⠀⠀⠀⣀⣤⣦⣶⣤⣴⠏⠀⣀⣤⣴⣶⣶⣶⣦⣤⡀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠜⣿⡀⠈⠀⢠⣿⣿⠁⢀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⣿⣇⠀⠻⡀⠈⠀⣿⠃⠀⠀⢠⣾⣿⣿⡿⢿⣿⠏⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠉⢿⡛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠐⠘⣿⣀⣴⣿⣿⣿⣿⣿⣭⣟⢦⣀⣀⣀⠀⠀
⠀⠀⠀⢻⣻⣆⠀⠱⣀⢩⣿⠀⠀⠀⠠⠟⠋⠁⠀⣰⠃⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡟⠙⣿⣿⠁⠀⢹⣿⡿⠿⣯⡻⡆
⠀⠀⠀⠈⢻⣻⣦⠀⠉⢸⡗⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠈⠛⠿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⣀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡶⠀⣿⣿⡀⠐⠈⢁⠠⠀⣼⣇⡇
⠀⠀⠀⠀⠀⠙⢽⡷⣦⣽⡇⠀⠀⠀⠀⠀⠀⠀⢰⡇⢀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣝⣿⡼⣿⣧⡐⠈⣠⣤⢾⣫⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠙⢻⣿⠇⠀⠀⠀⠀⠀⠀⠀⢸⠇⠘⣧⠀⠀⠀⠀⠀⢀⣾⣧⣄⣀⢀⣀⣠⣾⠋⠀⠀⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣻⡇⠀⠘⢿⣿⣛⡿⠷⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡾⣿⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠈⠳⣶⣤⡴⣾⢿⡹⢮⡝⣯⢻⣽⣿⣿⣄⠀⠀⠀⠀⠀⠀⠉⠓⠦⣤⣄⣀⣀⣠⣤⠿⢻⡞⣷⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣷⣿⠀⠀⠀⠀⠀⣀⡴⠋⠀⠀⠀⠀⠀⠹⣷⡹⣎⢷⡹⢧⣻⣼⠿⣿⣄⠉⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣽⣧⣤⣀⣀⣠⡴⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣯⣞⣭⣻⣟⣷⡀⢀⠛⢿⡄⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣶⣶⣶⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣿⡿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠻⣧⡈⠐⢈⣡⣾⠏⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣯⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢿⣓⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠛⠋⠁⠀⠀⠀⠀⠀⠀⠶⠛⠉⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣺⣿⣿⣻⢦⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣧⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣾⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠛⣯⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣷⡿⠀⠘⠻⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⢿⣸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠀⠖⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⢶⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠒⠒⠒⠖⠶⠦⠤⠤⢤⡤⣤⠤⣤⢤⡤⣤⢤⡤⠤⠤⠤⠴⠶⠒⠒⠒⠒⠊⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
        elif AItype.lower() == 'r':
            input('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠉⠉⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡖⢾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠒⠒⠒⠒⠒⠒⠲⠲⠚⠓⠒⠒⠛⠓⢒⣖⠒⠒⠒⠒⠒⠒⢲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⢠⠖⠋⠉⠷⣄⠀⠀⢠⠖⠉⠉⠑⢦⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠉⢻⠀⠀⠀⠀⣿⣾⣿⣦⡀⢸⠀⠀⢿⣿⣿⣷⡀⢸⠀⠀⠀⠀⢸⠋⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀⣀⠀⠀⠘⢿⣿⢟⣂⠞⠀⠀⠈⠿⣿⣿⣡⠞⠀⠀⠀⠀⢸⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣾⠉⠉⠙⢧⡀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⣠⠞⠉⠉⡙⣇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣻⠀⠀⠀⠀⠙⢦⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⠞⠁⠀⠀⠀⠇⡏⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⡤⣤⣤⣤⣤⣤⣤⣤⣤⣤⢤⠤⠤⠤⠤⢤⣤⣤⣤⣤⣤⣤⡤⢤⣤⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠛⠦⣄⡀⣀⣿⡛⣛⣛⣛⢛⢛⢛⣷⣀⣀⣴⢛⡛⠶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⣿⣩⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⢭⡉⡇⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⣿⣽⠀⠀⣶⡆⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⢠⣇⡇⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠘⢦⣰⣿⣿⠀⢰⡿⡇⣄⠀⠀⠀⠀⣼⣇⣠⠀⠀⢸⣿⣇⡠⠞⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡃⠀⠀⢠⠟⣿⣿⠤⠾⠀⢻⠛⡄⢰⠤⠽⠏⣿⡟⡷⠶⢼⡿⡟⢆⠀⠀⠈⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠛⠦⣴⠏⠀⣿⣼⠀⠀⠀⠀⠀⢻⡞⠀⠀⠀⠻⠇⠀⠀⠀⡇⡇⠈⢷⡴⠚⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠿⢦⣀⡾⠁⠀⠀⣿⢾⣀⣀⣀⣀⣀⣀⣁⣀⣀⣀⣀⣀⣀⣀⣠⣷⡇⠀⠈⠻⣄⡰⠾⠶⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣤⡴⣟⠀⠀⠀⣹⠀⠀⠀⠰⣿⣈⡿⢯⡉⣿⣿⣿⣿⣿⣿⣿⣿⡏⢉⡿⢯⣀⡇⠀⠀⠀⢿⠀⠀⠀⢸⡦⣤⣄⠀⠀⠀
⠀⢀⡴⠋⠀⠁⠹⣤⣀⡤⠏⠀⠀⠀⠐⣿⠹⣄⡼⠟⣿⣿⣿⣿⣿⣿⣿⣿⡶⠻⣶⡴⠿⡇⠀⠀⠀⠘⢦⣀⣠⠞⠃⠀⠈⠳⡀⠀
⢠⡟⠀⢠⡶⣄⠀⠀⢸⠀⠀⠀⠀⠀⠘⢿⣤⣼⣤⣤⣤⣶⣧⣶⣦⣶⣴⣦⣤⣤⣴⣤⣤⡇⠀⠀⠀⠀⠀⣼⠀⠀⣀⠶⣄⠀⠹⡄
⠸⣇⡴⠋⢠⠞⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⣨⡷⠀⢺⣆⢀⠀⠀⠀⢀⡽⠀⠀⠀⠀⠀⠀⠹⣄⠀⠹⣄⠈⢳⣠⠇
⠀⠙⠁⣴⣋⣀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠉⠉⠉⠉⠙⣦⡠⣶⠋⠉⠉⠉⠉⠉⢳⠄⠀⠀⠀⠀⠀⠀⠈⠣⣀⣙⣦⡀⠛⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠖⠖⠲⠒⠒⠿⣇⡀⣨⠗⠒⠒⠒⠒⠲⣯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣤⠤⠤⢴⢶⣶⡟⠂⢙⡦⠤⠤⢤⣤⣤⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠛⠚⠛⠚⠓⠲⢤⡷⠀⣻⠦⠖⠒⠛⠛⠛⠛⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⣺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿⠁⢻⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

    input (f'{AI} : {player} The landing is imminent and will be violent, hold on, landing in 10...')
    print('\n')
    for x in range (9, 0, -1):
            input(f'{x}...')
            print('\n')
    input('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠏⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠈⠙⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⣶⣒⣶⠦⣤⣀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠲⡌⠙⢦⠈⢧⠀
⠀⠀⠀⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡴⢃⡠⠋⣠⠋⠀
⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⢖⣋⡥⢖⣫⠔⠋⠀⠀⠀
⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣩⠭⢵⣒⣻⠭⢖⠏⠁⢀⣀⠀⠀⠀⠀
⠠⠀⠈⠓⠒⠦⠭⠭⠭⣭⠭⠭⠭⠭⠿⠓⠒⠛⠉⠉⠀⠀⣠⠏⠀⠀⠘⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠿⠀⠀⠀⠀⠀⠈⠉⠙⠒⠒⠛⠉⠁⠀⠀⠀⠉⢳⡞⠉⠀⠀⠀⠀⠀
''')
    print('\n' * 10)
    input('''⢠⠀⡀⢀⠀⢠⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⢤⣀⠀⠀⠀⠈⣆⢧⠈⡆⢸⠀⠀⠀⢰⢡⠇⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠀⠀⣯⢀⣨⠃⠀⠀⠀⠸⡜⣄⣣⢸⠀⠀⠀⡜⡌⠀⠀⠀⠀⢀⡜⡁⠀⠀⠀⠀⠀
⠀⠀⠙⢮⡳⢄⠈⠁⠀⢠⠴⠍⣛⣚⣣⢳⢽⡀⣏⣲⣀⢧⡥⠤⠶⢤⣠⢎⠜⠁⠀⠀⠀⠀⠀
⠀⠠⣀⠀⠙⢦⡑⢄⢀⣾⣧⡎⠁⠀⠙⡎⡇⡇⡇⠹⢪⣀⡓⣦⢀⣼⣵⠋⢀⠴⣊⠔⠁⠀⠀
⠀⠀⠈⠑⢦⣀⠙⣲⣝⢭⡚⠃⠀⠀⠀⠸⠸⣹⠁⠀⠀⠀⠉⣹⣪⣎⡸⢞⡵⠊⠁⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣷⢯⣨⠷⣝⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠵⣪⢶⣙⡤⠖⢉⣀⠤⠖⠂
⠀⠀⠀⠀⠀⢀⡞⢠⠾⠓⢮⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢬⣺⡯⢕⢲⠉⣥⣀⡀⠀⠀
⠀⠀⢀⡤⣀⢈⡷⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠘⠀⢱⢾⠘⢇⢴⠁⠀⠀
⠀⠀⢻⣀⡼⢘⣧⢀⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢙⣞⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠀⢿⡀⠈⠧⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⣹⣦⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⢤⡴⢺⡧⣴⡶⢗⡣⠀⡀⠀⠀⠀⡄⠀⢀⣄⠢⣔⡞⣤⠦⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⡤⣖⣯⡗⣪⢽⡻⣅⠀⣜⡜⠀⠀⠀⠸⡜⡌⣮⡣⡙⢗⢏⡽⠁⠰⡏⠙⡆⠀⠀
⠀⠀⣒⡭⠖⣋⡥⣞⣿⡚⠉⠉⢉⢟⣞⣀⣀⣀⠐⢦⢵⠹⡍⢳⡝⢮⡷⢝⢦⡀⠉⠙⠁⠀⠀
⠐⠊⢡⠴⠚⠕⠋⠹⣍⡉⠹⢧⢫⢯⣀⣄⣀⠈⣹⢯⣀⣧⢹⡉⠙⢦⠙⣄⠑⢌⠲⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠧⡴⣳⣃⣸⠦⠴⠖⢾⣥⠞⠛⠘⣆⢳⡀⠈⠳⡈⠳⡄⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⡱⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢣⠀⠀⠉⠀⠈⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠞⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
        # Starting dialogue
    input(f'{player} : Where did I land?')
    print('\n')
    input(f'{player} : {AI} are you there?')
    print('\n')
    input(f'{AI} : Yes, but my processor took a big hit during our landing, we need to find something to repair it so I can work on our ship and return to the base.')
    print('\n')
    input(f'{player} looks at the ship behind him')
    print('\n')
    input(f'{player} : Indeed it is badly damaged, but we will find a solution. Do you know where we are?')
    print('\n')
    input(f'{AI} : Wait, I am analyzing our environment.')
    print('\n')
    input(f'{AI} : ... ... ... ... I think we are on Piltaris.')
    print('\n')
    input(f'{player} : Piltaris! But we were supposed to return to the base, what happened?')
    print('\n')
    input(f'{AI} : I think when we went through the black hole 2134 to return to the base, something must have passed at the same time and damaged our engine, which changed the space-time and modified our destination.')
    print('\n')
    input(f'{player} : Okay, what is the date here?')
    print('\n')
    input(f'{AI} : Here it is March 10, 3688.')
    print('\n')
    input(f'{player} : MARCH 10, 3688?! And on the base?')
    print('\n')
    input(f'{AI} : I can\'t detect the date of the base, but I know that on Piltaris, 1 hour is equivalent to 4 months on the base.')
    print('\n')
    input(f'{player} : Which means if we want to return before next year on the base, we have 1 hour.')
    print('\n')
    input(f'{player} : So let\'s go, let\'s see what we can salvage from our wreck. {AI}, go see what you can salvage.')
    print('\n')
    print(f'{AI} : Alright, I\'m on it.')
    print('\n' * 10)
    
    # First choice of the player
    while True:
        print(f'Here {player}, your first consequential choice, you must choose a number between 0 and 9.')
        num1 = int(input('Which number do you choose? : '))
        if num1 > 9 or num1 < 0:
            print('\n' * 5)
            print('The number must be between 0 and 9, try again.')
            continue
        random_number = random.randint(0, 9)
        if num1 > random_number:
            print('\n' * 5)
            print(f'You chose the number {num1} and it is greater than {random_number} which is the drawn number. CONGRATULATIONS!')
            print('\n')
            input(f'{AI} : I was able to recover a lot of resources, I will be able to repair a part in 15 minutes!')
            print('\n')
            input(f'{player} : Great! We just need to find blue fuel to power the engine.')
            print('\n')
            day += 15
            print (' __________________________________________ ')
            print ('|                 Summary                  |')
            print (f'|Time on Piltaris: {day} minutes           |')
            print (f'|HP: {health}/100                          |')
            print ('|__________________________________________|')
            print('\n')
            break
        elif num1 < random_number:
            print('\n' * 5)
            print(f'You chose the number {num1} and it is less than {random_number} which is the drawn number. TOO BAD!')
            print('\n')
            input(f'{AI} : There is nothing more to salvage, I will have to repair everything, it will take 30 minutes.')
            print('\n')
            input(f'{player} : Go ahead, we have no choice, then we will go look for blue fuel to power the engine.')
            print('\n')
            day += 30
            print (' __________________________________________ ')
            print ('|                 Summary                  |')
            print (f'|Time on Piltaris: {day} minutes           |')
            print (f'|HP: {health}/100                          |')
            print ('|__________________________________________|')
            print('\n')
            break
        elif num1 == random_number:
            print('\n' * 5)
            print(f'You chose the number {num1} and it is equal to {random_number} which is the drawn number. GREAT!')
            print('\n')
            input(f'{AI} : The engine is not too damaged, so I was able to repair it in 5 minutes.')
            print('\n')
            input(f'{player} : Great! We just need to find blue fuel to power the engine.')
            print('\n')
            day += 5
            print (' __________________________________________ ')
            print ('|                 Summary                  |')
            print (f'|Time on Piltaris: {day} minutes           |')
            print (f'|HP: {health}/100                          |')
            print ('|__________________________________________|')
            print('\n')
            break
        else:
            print('\nInvalid action. Choose 1, 2, or 3.')
            continue
    
    input(f'{player} : So, it has been {day} minutes since we are on Piltaris, we need to hurry, analyze the planet to know where there is ...')
    print('\n')
    input('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠴⠒⠒⠒⠒⠒⠒⠒⠉⠉⠉⠁⠀⠀⠀⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡝⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠉⠀⢀⡠⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠈⡟⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠉⠀⠀⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠃⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠚⠁⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠁⢀⡴⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⣠⠖⠋⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠤⠤⠔⠒⠒⠒⠺⣧⠘⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀
⠀⠀⢠⡾⣇⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠖⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠰⡞⢳⡈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⠀⣴⠋⠀⠘⢧⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⢹⠈⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀
⣼⡃⣠⢄⡀⠘⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⢀⣀⣤⣶⣶⣶⣶⣶⣶⣶⣶⣌⣙⣿⡄⠀⢈⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀
⣿⢷⣿⣿⣮⠃⠀⠀⠀⢸⠀⠀⠀⠀⠀⡴⠁⠀⣠⣶⣿⡿⠟⠛⠉⠀⠀⠀⠈⣿⣿⡿⠷⠚⠁⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀
⠘⣿⣿⣿⢻⣷⡀⠀⠀⠘⡇⠀⠀⠀⠀⢠⣦⣾⣿⣫⣥⣶⣶⣦⣤⣄⣀⣠⣾⣿⣿⡇⠀⠀⠀⠀⢀⣤⠤⠀⠀⠀⠀⠀⠀⠀⠈⡟⠀⠀⠀⠀⠀⠀
⠀⠻⣿⣿⡄⢻⣷⡀⠀⠀⣷⠀⠀⠀⢀⣿⣿⣿⣿⣿⡋⠉⠀⠀⠈⠉⣻⣿⣿⣿⣟⡼⠀⠀⠀⣮⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀
⠀⣰⣿⣿⣿⣶⢿⣇⡆⠀⠉⠀⠀⠀⣸⣿⣿⣿⣿⣿⣟⠻⢶⣤⣤⣴⣿⣿⣿⢟⠟⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀
⠀⣿⢇⠻⣿⣿⡼⣿⡷⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣦⣤⣾⣿⣿⡿⣟⠵⠁⣠⠞⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠛⢦⣕⡨⠛⢛⣿⠇⠀⠀⠀⠀⠀⣾⣟⣻⡿⠿⠿⠿⠿⢿⣻⣫⠥⠚⢁⡾⠚⠁⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡄⠀⠈⠉⠒⠒⠈⠀⠀⠀⠀⠀⠀⠈⠁⢈⠉⠁⠀⠀⠀⢈⣉⣤⠤⠒⠉⠀⠀⠀⠀⡰⠋⢰⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⠀⠀⢸⠀⠀⠀⢀⡠⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠴⠒⠉⠀⢠⠀⠀⢸⠒⠒⣫⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⣶⡄⠰⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠚⠋⠁⠀⠀⠀⠀⠀⡇⠀⠀⠘⡇⠘⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣟⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⢰⠃⠀⡉⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⢀⣴⢿⠀⢀⡄⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠰⢦⣠⠶⠶⣤⡀⠀⠀⠀⠀⢿⡆⠀⠀⠀⠀⠀⢀⣠⠴⠞⠉⠀⣼⠀⠈⣇⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡓⣶⡒⠊⠁⠉⠀⠀⠀⢈⡾⠇⠀⠀⠀⡠⠞⠉⠀⠀⠀⠀⢸⠏⡇⠀⠟⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠈⠇⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⣴⣟⣀⡀⠀⠀⠀⠀⠀⠸⢼⢻⡀⠰⡄⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠈⠉⠳⣶⣖⡒⠒⠀⠀⢸⣷⡀⠹⡄⠀⠀⠀⠉⠓⢦⣄⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠈⠱⣍⠀⠀⠀⠀⠁⠳⠀⠹⡄⠀⠀⠀⠀⠘⠀⠉⠓⠢⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠓⠶⠶⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⣄⠱⣄⠀⠀⠀⠀⠀⠀⠀⡎⠀⠈⠰⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⡆⠀⠀⠀⠀⠀⠘⣆⠘⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠓⠁⠀⠀⠀⠀⠀⠀⠘⡦⠀⠈⠛⠢⠤⠤⠀⠀⠀⠀⠀⠀''')
    input('Alien: GLABUR!!!!! GLITARIS PUERATI TYGATI')
    print('\n')
    # Combat between the alien and the player
    print(f'{player} : What is that?! An alien!')
    print('\n')
    input(f'{AI} : Watch out {player}, it seems hostile! Get ready to defend yourself.')
    print('\n')

    input(f'{AI} : {player}, here is how the combat system works. You have three options: (1) Attack, (2) Defend, (3) Run. Choose wisely to survive.')
    alien_health = 50
    while health > 0 and alien_health > 0:
        print(f'{player} : What do you do? (1) Attack (2) Defend (3) Run')
        action = input('Choose an action (1/2/3): ')
        if action == '1':
            player_attack = random.randint(5, 15)
            alien_attack = random.randint(5, 15)
            alien_health -= player_attack
            health -= alien_attack
            print(f'\n{player} attacks the alien and deals {player_attack} damage.')
            print(f'The alien attacks {player} and deals {alien_attack} damage.')
        elif action == '2':
            player_defense = random.randint(5, 10)
            alien_attack = random.randint(5, 15) - player_defense
            if alien_attack < 0:
                alien_attack = 0
            health -= alien_attack
            print(f'\n{player} defends and reduces the damage by {player_defense} points.')
            print(f'The alien attacks {player} and deals {alien_attack} damage.')
        elif action == '3':
            print(f'\n{player} tries to run...')
            escape_chance = random.randint(0, 1)
            if escape_chance == 1:
                print(f'{player} managed to escape!')
                break
            else:
                alien_attack = random.randint(5, 15)
                health -= alien_attack
                print(f'{player} failed to escape. The alien attacks {player} and deals {alien_attack} damage.')
        else:
            print('\nInvalid action. Choose 1, 2, or 3.')
            continue

        print(f'\n{player} : {health} HP remaining')
        print(f'Alien : {alien_health} HP remaining')
        print('\n')

    if health <= 0:
        print(f'{player} was defeated by the alien...')
        print (' __________________________________________ ')
        print ('|                 Summary                  |')
        print (f'|Time on Piltaris: {day} minutes           |')
        print (f'|HP: {health}/100                          |')            
        print ('|__________________________________________|')
        retry = input('Do you want to try again? (yes/no): ')
        if retry.lower() == 'yes':
            exec(open('/e:/Bureau/Codex/terminal_game.py').read())
        else:
            print('Thank you for playing!')
    elif alien_health <= 0:
        print(f'{player} defeated the alien!')
        input(f'{AI} : Well done {player}! We must continue our mission.')
    print('\n' * 50)
    input(f'{AI} : Great {player}, you managed to defeat it but you need to heal, we need to find something to heal you.')
    print('\n')
    input(f'{player} : You are right, I am pretty beat up, it was tough...')
    print('\n')
    input(f'{AI} : Let\'s explore, maybe on our way we will find blue fuel.')
    print('\n')
    input(f'{player} : Let\'s go!')
    print('\n')
    while True:
        print(f'Here {player}, another consequential choice, you must choose a number between 0 and 9.')
        num1 = int(input('Which number do you choose? : '))
        if num1 > 9 or num1 < 0:
            print('\n' * 5)
            print('The number must be between 0 and 9, try again.')
            continue
        random_number = random.randint(0, 9)
        if num1 > random_number:
            print('\n' * 5)
            print(f'The drawn number is {random_number}. CONGRATULATIONS!')
            print('\n')
            input(f'{AI} : We walked for 15 minutes and found something to patch you up and make blue fuel.')
            print('\n')
            input(f'{player} : Great! Now we need to try to make blue fuel.')
            print('\n')
            day += 15
            health += 30
            print (' __________________________________________ ')
            print ('|                 Summary                  |')
            print (f'|Time on Piltaris: {day} minutes           |')
            print (f'|HP: {health}/100                          |')
            print ('|__________________________________________|')
            print('\n')
        elif num1 < random_number:
            print('\n' * 5)
            print(f'The drawn number is {random_number}. TOO BAD!')
            print('\n')
            input(f'{AI} : We walked for 30 minutes and only found something to make blue fuel, we will see about your condition later...')
            print('\n')
            input(f'{player} : We will do that in the lab, now let\'s make blue fuel.')
            print('\n')
            day += 45
            print (' __________________________________________ ')
            print ('|                 Summary                  |')
            print (f'|Time on Piltaris: {day} minutes           |')
            print (f'|HP: {health}/100                          |')
            print ('|__________________________________________|')
            print('\n')
        elif num1 == random_number:
            print('\n' * 5)
            print(f'The drawn number is {random_number}. GREAT!')
            print('\n')
            input(f'{AI} : We are lucky, it took 5 minutes and we found something to make blue fuel and a potion for your health.')
            print('\n')
            input(f'{player} : Great! We just need to find blue fuel to power the engine.')
            print('\n')
            day += 5
            health += 40
            print (' __________________________________________ ')
            print ('|                 Summary                  |')
            print (f'|Time on Piltaris: {day} minutes           |')
            print (f'|HP: {health}/100                          |')
            print ('|__________________________________________|')
            print('\n')
        break
    input(f'{AI} : I will take care of making the blue fuel now.')
    print('\n')
    while True:
        print(f'{AI} : I will try to make the blue fuel. Choose a number between 0 and 9 to determine the result.')
        num2 = int(input('Which number do you choose? : '))
        if num2 > 9 or num2 < 0:
            print('\n' * 5)
            print('The number must be between 0 and 9, try again.')
            continue
        random_number = random.randint(0, 9)
        if num2 > random_number:
            print('\n' * 5)
            print(f'The drawn number is {random_number}. CONGRATULATIONS! I managed to make the blue fuel in 15 minutes.')
            day += 15
            print (' __________________________________________ ')
            print ('|                 Summary                  |')
            print (f'|Time on Piltaris: {day} minutes           |')
            print (f'|HP: {health}/100                          |')
            print ('|__________________________________________|')
            print('\n')
        elif num2 < random_number:
            print('\n' * 5)
            print(f'The drawn number is {random_number}. TOO BAD! I failed and it took me 30 minutes.')
            day += 30
            print (' __________________________________________ ')
            print ('|                 Summary                  |')
            print (f'|Time on Piltaris: {day} minutes           |')
            print (f'|HP: {health}/100                          |')
            print ('|__________________________________________|')
            print('\n')
        elif num2 == random_number:
            print('\n' * 5)
            print(f'The drawn number is {random_number}. GREAT! I made the blue fuel perfectly in 5 minutes.')
            day += 5
            print (' __________________________________________ ')
            print ('|                 Summary                  |')
            print (f'|Time on Piltaris: {day} minutes           |')
            print (f'|HP: {health}/100                          |')
            print ('|__________________________________________|')
            print('\n')
        break
    input(f'{AI} : The blue fuel is ready, we can now power the engine and return to the base.')
    print('\n')
    input(f'{player} : Awesome! Let\'s go!')
    print('\n')
    input('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣴⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⢶⣾⣿⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⠟⢋⡡⠖⠉⠀⢸⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠛⢉⡠⠾⢷⡉⠀⠀⠀⠀⠌⢹⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠟⢁⡴⠚⠁⠀⠀⢀⣽⠿⣄⡀⠰⠀⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⢀⠔⠁⠀⠀⠀⢀⣴⡿⠋⠀⠀⠈⠉⠛⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠄⠊⢙⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⢀⡔⠁⠀⠀⠀⢀⣴⣿⡟⠁⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠔⠊⠀⠀⠀⣏⢋⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠃⣠⠋⠀⠀⠀⠀⣴⣿⣿⠏⠀⠀⠀⠀⠀⢀⣄⡼⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠔⠁⠀⠀⠀⠀⠀⠈⠻⠯⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⢁⡼⠁⢀⣴⡶⠿⣿⣿⡿⠃⠀⠀⠀⠀⠀⣠⣾⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⢡⠞⠀⢠⣿⠋⠀⠀⠈⣿⡇⠀⠀⠀⠀⢀⣼⡿⣱⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣷⠋⠀⠀⠘⣿⣦⣀⣀⣠⣿⠃⠀⠀⠀⣴⣿⣿⣵⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⣿⡃⠀⠀⠀⢠⣿⡿⠾⠛⠋⠁⠀⠀⣠⣾⣿⣿⣟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡋⣻⣄⠀⢰⠿⠋⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠋⠘⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⢤⣀⠀⣿⢦⣼⡿⣇⢱⡃⠈⢳⣄⡀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠋⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣱⠤⠞⣻⣿⣶⣿⡇⠘⢯⢙⡦⣏⠀⢉⡷⠦⢤⣴⣿⣟⡿⠋⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠿⢯⣉⣹⠟⠁⢀⣾⣿⣿⣿⣇⢳⣤⣄⠙⠧⣄⣹⠯⣤⢴⣯⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⣼⣿⣿⣻⣿⡿⠛⢩⡟⢦⣀⣀⣩⣽⣿⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀⣴⣿⠏⠀⣼⠟⠀⢠⣾⣿⣷⣾⣿⣿⡯⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⢀⠀⠀⠀⠀⠀⠀⢠⠟⡟⠀⢀⡎⠘⠟⠀⣼⠏⢀⣴⡿⠿⢻⣹⣯⣿⣿⣿⡚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀
⠈⡄⠀⠀⠀⠀⢰⣯⣴⡇⠀⡸⠀⠀⠀⣼⣏⣴⠿⠉⠀⣀⣼⣿⣿⡿⠃⣯⡙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⡄⠀⠀⠀⠀⠀⢸⠀⢀⡇⠀⠀⣸⣛⠟⠉⠠⠶⠿⢿⠟⠋⠁⠀⣸⡇⠉⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢠⡅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢄⠀⠀⠀⢠⡟⠀⣸⠀⠀⠀⠛⠁⠀⠀⠀⢀⡴⠋⠀⠀⢀⣴⡁⢷⠀⠀⠀⠀⠀⠠⢦⣄⡤⢤⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠣⡀⠀⣾⡇⢠⠇⠀⠀⠀⠀⠀⢀⡠⠖⠉⠀⢀⡠⣶⠋⠀⢳⣼⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠢⣼⠁⡞⠀⠀⠀⣀⠤⠚⠉⢀⣠⠴⢺⣉⡼⠃⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⢀⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣜⡸⠁⢀⠴⠊⣁⣤⣶⠟⠉⠀⠀⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡿⢁⣔⡥⠖⠻⢍⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⡷⠛⠁⠀⠀⠀⠀⠀⠉⠉⠒⠒⠒⠒⠒⠒⠒⠂⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    print('\n' * 50)
    input('YOU HAVE FINISHED PILTARIS')
    base_time =  day / 60
    input(f'With {health} health and in {day} minutes, which is equivalent to {base_time} years on the base, congratulations you can try to do better if you want')
elif start == 'N' or start == 'n':
    input('Good Bye :)')
