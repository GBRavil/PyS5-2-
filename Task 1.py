# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

sum = 2021
step = 0
player1 = 'Ivan'
player2 = 'Dima'
sum_player1 = 0
sum_player2 = 0

def take_candys(player):
    t_c = int(input(f'{player}, возьмите не более чем 28 конфет, взял '))
    while t_c < 1 or t_c > 28:
        t_c = int(input(f'{player}, возьмите корректное количество конфет '))
    return t_c 

def p_print (sum_player, player, sum):
    print(f'{player} всего {sum_player} конфет')
    print(f'Осталось конфет {sum}')

def game (sum_player, step, sum, candy):
    
    sum_player += candy
    sum -= candy
    step += 1
    return sum_player, step, sum

flag = random.randint(1, 3)
if flag:
    print(f'Первым ходит {player1}')
else:
    print(f'Первым ходит {player2}')

while sum > 28:
    if flag:
        candy = take_candys(player1)
        sum_player1, step, sum = game (sum_player1, step, sum, candy)
        flag = False
        p_print(sum_player1, player1, sum)
    else:
        candy = take_candys(player2)
        sum_player2, step, sum = game (sum_player2, step, sum, candy)
        flag = True
        p_print(sum_player2, player2, sum)
        print(f'Для выигрыша первый игрок должен взять {random.randrange(1, 28, 2) + sum % 2} конфет')

if flag:
    sum_player1 += sum
    print(f'Выиграл {player1}, т.к. забрал последние {sum} конфет, всего {sum_player1 + sum_player2} конфет')
else:
    sum_player2 += sum
    print(f'Выиграл {player2}, т.к. забрал последние {sum} конфет, всего {sum_player2 + sum_player1} конфет') 