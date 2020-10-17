from game import player, monteCarlo, game
from mancala import status

iters=500
winner = game(player, monteCarlo, status, iters, True)
print("Ganador: " + str(winner + 1))
