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

def continueGame(jugadores):
    # Validar que haya mas de 1 jugador vivo
    totalPlayersAlive = 0
    for jugador in jugadores:
       if validateAlive(jugador):
            totalPlayersAlive += 1
    
    if totalPlayersAlive > 1:
        return True
    else:
        return False

        
def validateAlive(jugador):
    if jugador.lives == 0:
        return False
    else:
        return True
    
def getBomb():
    return random.randint(1, 4)

def clearDisplay():
    os.system("cls" if os.name == "nt" else "clear" )

def getWinner(jugadores):
    for jugador in jugadores:
        if validateAlive(jugador):
            return jugadores.index(jugador)
        
jugadores = [Player("Jugador 1"), Player("Jugador 2"), Player("Jugador 3"), Player("Jugador 4")]

# Init game
currentPlayer = 0
while continueGame(jugadores):
    # Cuando el turno empieza
    showPlayers(jugadores)
    print("Turno del Jugador:", jugadores[currentPlayer].name)
     

    # Desarrollo: Cuando el juego realmente inicia
    bomb = getBomb()
    print(bomb)
    opcions = [1, 2, 3, 4]
    print(opcions)
    option = int(input("Opcion: "))
    if option == bomb:
        jugadores[currentPlayer].lives -= 1
        

    # Cuando el turno acaba
    currentPlayer += 1
    
    

    if currentPlayer > 3:
        currentPlayer = 0
    
    
        

    # Clear display
    clearDisplay()

Winner = getWinner(jugadores)
print("El ganador es...", jugadores[Winner].name)

