import os
import random
import time

#Declara el jugador
class Player:
    #Inicialisacion del jugador
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.alive = True
        
        #Modtrsr jugsdores
def showPlayers(jugadores):
    for jugador in jugadores:
        print("[.«]Name:", jugador.name)
        print("[♥«]Lives:", jugador.lives)

#Se valida que haya mas de un jugador vivo
def continueGame(jugadores):
    # Validar que haya mas de 1 jugador vivo
    totalPlayersAlive = 0
    for jugador in jugadores:
       if validateAlive(jugador):
            totalPlayersAlive += 1
    #Si hay mas de un jugador el juego continua
    if totalPlayersAlive > 1:
        return True
    else:
        return False

#Se valida que el jugador siga vivo      
def validateAlive(jugador):
    if jugador.lives == 0:
        return False
    else:
        return True

#se optiene la posicion de la bomba
def getBomb():
    return random.randint(1, 4)

#Se limpia la pantalla
def clearDisplay():
    os.system("cls" if os.name == "nt" else "clear" )

#se optiene el ultimo jugador con vida
def getWinner(jugadores):
    for jugador in jugadores:
        if validateAlive(jugador):
            return jugadores.index(jugador)

# se declaran los jugadores
jugadores = [Player("Jugador 1"), Player("Jugador 2"), Player("Jugador 3"), Player("Jugador 4")]

# Init game
currentPlayer = 0
while continueGame(jugadores):
    #se valida que el jugador correspondiente siga con vida
    if validateAlive(jugadores[currentPlayer]):

        # Cuando el turno empieza
        showPlayers(jugadores)
        print("Turno del Jugador:", jugadores[currentPlayer].name, "«")
        print("-(1)- -(2)- -(3)- -(4)- «select")    
        print("]-#-[ ]-#-[ ]-#-[ ]-#-[    «one")
        print("[ _ ]_[ _ ]_[ _ ]_[ _ ]________")
       



        # Desarrollo: Cuando el juego realmente inicia
        bomb = getBomb()
        opcions = [1, 2, 3, 4]
    
        option = int(input("Opcion: "))
        if option == bomb:
                print(jugadores[currentPlayer].name,": -♥")
                print("¡¡WARNING!!")
                time.sleep(2)
                jugadores[currentPlayer].lives -= 1
            


    # Cuando el turno acaba
    currentPlayer += 1
    
    #Reseteando los turnos
    if currentPlayer > 3:
        currentPlayer = 0

    # Clear display
    clearDisplay()
#acaba juego

#Mostrar ganador
Winner = getWinner(jugadores)
print(" * ._____. * ")
print(" (-( (1) )-)")
print(" *  [ * ]   ")
print(" **  )-(  *  ")
print("___.[___].___")
print("El ganador es...", jugadores[Winner].name)

