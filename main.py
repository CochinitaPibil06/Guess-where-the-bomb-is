import os
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.lives = 3
        
def showPlayers(jugadores):
    for jugador in jugadores:
        print("Name:", jugador.name)
        print("Lives:", jugador.lives)

jugadores = [Player("Jugador 1"), Player("Jugador 2"), Player("Jugador 3"), Player("Jugador 4")]
showPlayers(jugadores)
