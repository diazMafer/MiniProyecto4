""""
    Universidad del Valle de Guatemala. Guatemala, 2020. 
    Modelación y Simulación. 
    Ana Lucía Hernández (17138) y Maria Fernanda López (17160). 

    Módulo con las funciones relacionadas a la lógica del juego Mancala. 
"""
import random
import math

status = {
    'board': [
        # Jugador real = P1
        4, 4, 4,  4, 4, 4,  # [0 - 5]
        0,  # Mancala P1 [6]
        # Computadora = P2
        4, 4, 4,  4, 4, 4,  # [7 - 12]
        0,  # P2 [13]
    ],
    'turn': 0,
    'finish': False,
}

def get_score(status):
    for player in range(2):
        mancala = 6 + (7 * player)
        score = status['board'][mancala]
        score += sum(status['board'][mancala - 6: mancala])
        status['board'][mancala] = score
    return status

def get_possibles_moves(player, status):
    possibles_moves = []
    board = status['board']

    start = 0 + (7 * player)
    end = 5 + (7 * player)

    for i in range(start, end + 1):
        if board[i] != 0:
            possibles_moves.append(i)

    return possibles_moves

def make_move(player, move, status):
    board = status['board']
    chips = board[move]  # contar / revisar cuantas piezas hay en el pit
    board[move] = 0  # tomar las piezas del pit

    for i in range(0, chips):
        move = (move + 1) % len(board)
        board[move] = board[move] + 1

    if move != (6 + (7 * player)):  # si no para en una mancala
        status['turn'] = (player + 1) % 2  # pasamos al siguiente jugador
        # revisamos si podemos robar
        if board[move] == 1:  # si es igual a 1 significa que esta vacio
            dif = 6 - move
            mirror_move = 6 + dif
            if board[mirror_move] > 0:  # revisamos si el mirror tiene algo 
                temp = board[mirror_move]
                board[mirror_move] = 0
                temp = temp + board[move]
                board[move] = 0

                board[6 + (7 * player)] += temp

    status['board'] = board
    return status

def make_turn(player, move, status):
    # validamos el move
    status = make_move(player, move, status)
    if (not get_possibles_moves(player, status) or
            not get_possibles_moves((player + 1) % 2, status)):
        
        status['finish'] = True
        get_score(status)
        return status
    return status

