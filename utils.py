global str

def print_board(state):
    board = state['board']
    boards = [board[0:7], board[7:14]]
    print('\n Turno de jugador: %d' % (state['turn'] + 1))
    txt = '  '
    for i in range(5, -1, -1):
        txt = txt + str(boards[1][i]) + '  '
    print(txt)

    txt = str(boards[1][6]) + '                  ' + str(boards[0][6])
    print(txt)

    txt = '  '
    for i in range(0, 6):
        txt = txt + str(boards[0][i]) + '  '
    print(txt)
