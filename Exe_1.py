#   Создайте программу для игры с конфетами человек против человека.
#   Условие задачи: На столе  лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#   Первый ход определяется жеребевкой. За один ход можно забрать не более 28 конфет. Все конфеты оппонента достаются
#   сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#   а) Добавить в игру бота
#   б) Наделите бота интелектом

import random


sweets = 2021
take_max_sweet = 28
player_1 = input('Name player 1: ')
player_2 = input('Name player 2: ')
count_sweet = 0

def player_1_turn(sweets, take_max_sweet):
    sweet_player_1 = int(input(f'{player_1} move: '))
    if sweet_player_1 > take_max_sweet:
        print(f'You dont take so much sweets, lose move')
    else:
        print(f'{player_1} take {sweet_player_1} sweets')
        sweets -= sweet_player_1
    print(sweets)
    return sweets


def player_2_turn(sweets, take_max_sweet):
    sweet_player_2 = int(input(f'{player_2} move: '))
    if sweet_player_2 > take_max_sweet:
        print(f'You dont take so much sweets, lose move')
    else:
        print(f'{player_2} take {sweet_player_2} sweets')
        sweets -= sweet_player_2
    print(sweets)
    return sweets


def pvp_game(sweets, take_max_sweet):
    jreb = random.randint(1, 2)
    while sweets > 1:
        if jreb == 1:
            print(f'{player_1}')
            sweets = player_1_turn(sweets, take_max_sweet)
            if sweets > 0:
                jreb = 2
        if jreb == 2:
            print(f'{player_2}')
            sweets = player_2_turn(sweets, take_max_sweet)
            if sweets > 0:
                jreb = 1
        #if sweets < take_max_sweet:
        #    take_max_sweet = take_max_sweet - (take_max_sweet - sweets)
    if jreb == 1:
        print(f'Win player - {player_1}')
    if jreb == 2:
        print(f'Win player - {player_2}')
pvp_game(sweets, take_max_sweet)