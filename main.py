""""
    Universidad del Valle de Guatemala. Guatemala, 2020. 
    Modelación y Simulación. 
    Ana Lucía Hernández (17138) y Maria Fernanda López (17160). 

    Clase principal y ejecutable del juego. 
"""
from game import player, monteCarlo, game
from mancala import status

iters_arr = [0, 500, 10000]
level = input("Ingrese el número de dificultad que desea: \n\t1. Noob \n\t2. Avanzado \n\t3. Pro\n>")
iters = iters_arr[int(level) -1]
winner = game(player, monteCarlo, status, iters, True)
print("Ganador: " + str(winner + 1))
