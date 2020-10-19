""""
    Universidad del Valle de Guatemala. Guatemala, 2020. 
    Modelación y Simulación. 
    Ana Lucía Hernández (17138) y Maria Fernanda López (17160). 

    Módulo con las funciones relacionadas a la parte aleatoria (Montecarlo) del jugador 2 (computadora). 
"""
import random
from mancala import *
from utils import print_board
import copy

def game(player1, player2, status, iters, shows=False):
    while not status['finish']:
        turn = status['turn']
        if shows:
            print_board(status)
        if turn == 0:
            # jugador real
            status = player1(status, 0)
        elif turn == 1:
            # implementacion de mancala / computadora
            status = player2(status, 1, iters)
    board = status['board']
    score = [board[6], board[13]]
    return score.index(max(score))

def player(status, player, iters=0):
    choose = -1
    p = get_possibles_moves(player, status)
    while choose not in p:
        choose = input('Elija una opcion: ')
        choose = -1 if choose == '' else int(choose)
        status = make_turn(player, choose, status)
    return status

def monteCarlo(status, player, iters):
    results = [0]*14
    ocurrances = [1]*14
    possible = get_possibles_moves(player, status)
    for i in range(iters):
        choice = random.choice(possible)
        ns = copy.deepcopy(status)
        make_turn(player, choice, ns)
        ocurrances[choice] += 1
        results[choice] += game(randomPlayer, randomPlayer, ns, iters) == player
    win_percents = [i / j for i, j in zip(results, ocurrances)]
    move = win_percents.index(max(win_percents))
    return make_turn(player, move, status)

def randomPlayer(status, player, iters=0):
    possible = get_possibles_moves(player, status)
    choose = random.choice(possible)
    return make_turn(player, choose, status)

def randomGame(status):
    while not status['finish']:
        status = randomPlayer(status, status['turn'])
    board = status['board']
    score = [board[6], board[13]]
    return score.index(max(score))
