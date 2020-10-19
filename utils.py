""""
    Universidad del Valle de Guatemala. Guatemala, 2020. 
    Modelación y Simulación. 
    Ana Lucía Hernández (17138) y Maria Fernanda López (17160). 

    Módulo con las funciones para UI del juego. 
"""
def print_board(state):
    board = state['board']
    boards = [board[0:7], board[7:14]]
    print('\n Turno de jugador: %d' % (state['turn'] + 1))
    txt = ("-")*29 + '\n  | '
    for i in range(5, -1, -1):
        txt = txt + str(boards[1][i]) + ' | '
    print(txt)
    txt = str(boards[1][6]) + ' | ' + ("-"*20) +'  | ' + str(boards[0][6])
    print(txt)
    txt = '  | '
    for i in range(0, 6):   
        txt = txt + str(boards[0][i]) + ' | '
    print(txt)
    print("-"*29)
    print(" [ " + " | ".join(str(i) for i in range(6)) + " ] ")
