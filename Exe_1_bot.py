import random

sweets = 2021
take_max_sweet = 28
player = input('Name player: ')
count_sweet = 0


def player_turn(sweets, take_max_sweet):
    sweet_player = int(input(f'{player} move: '))
    if sweet_player > take_max_sweet:
        print(f'You dont take so much sweets, lose move')
    else:
        print(f'{player} take {sweet_player} sweets')
        sweets -= sweet_player
    print(sweets)
    return sweets


def bot_turn(sweets, take_max_sweet):
    while sweets > 0:
        if sweets < take_max_sweet:
            print('Bot move: ')
            sweet_bot = sweets
            print(f'Bot take {sweet_bot} sweets')
        else:
            print('Bot move: ')
            sweet_bot = random.randint(1, take_max_sweet)
            print(f'Bot take {sweet_bot} sweets')
        sweets -= sweet_bot     
        print(sweets)
        return sweets


def pve_game(sweets, take_max_sweet):
    jreb = random.randint(1, 2)
    while sweets > 1:
        if jreb == 1:
            print(f'{player}')
            sweets = player_turn(sweets, take_max_sweet)
            if sweets > 0:
                jreb = 2
        if jreb == 2:
            print('Bot')
            sweets = bot_turn(sweets, take_max_sweet)
            if sweets > 0:
                jreb = 1
        if sweets < take_max_sweet:
            take_max_sweet = take_max_sweet - (take_max_sweet - sweets)
    if jreb == 1:
        print(f'Win player - {player}')
    if jreb == 2:
        print('Win player - Bot')
pve_game(sweets, take_max_sweet)