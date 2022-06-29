def mostrar_tablero(tablero):
    for fila in tablero:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print(fila[i], end="\n")
            else:
                print(fila[i], end="  ")


def cambiar_tablero(tablero, posicion, jugador):
    if jugador:
        simbolo = "x"
    else:
        simbolo = "o"

    if posicion == 1:
        if tablero[4][0] == ' ':
            tablero[4][0] = simbolo
            return 0
        else:
            return "Esa posicion ya esta ocupada"
    elif posicion == 2:
        if tablero[4][2] == ' ':
            tablero[4][2] = simbolo
            return 0
        else:
            return "Esa posicion ya esta ocupada"
    elif posicion == 3:
        if tablero[4][4] == ' ':
            tablero[4][4] = simbolo
            return 0
        else:
            return "Esa posicion ya esta ocupada"
    elif posicion == 4:
        if tablero[2][0] == ' ':
            tablero[2][0] = simbolo
            return 0
        else:
            return "Esa posicion ya esta ocupada"
    elif posicion == 5:
        if tablero[2][2] == ' ':
            tablero[2][2] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 6:
        if tablero[2][4] == ' ':
            tablero[2][4] = simbolo
            return 0
        else:
            return "Esa posicion ya esta ocupada"
    elif posicion == 7:
        if tablero[0][0] == ' ':
            tablero[0][0] = simbolo
            return 0
        else:
            return "Esa posicion ya esta ocupada"
    elif posicion == 8:
        if tablero[0][2] == ' ':
            tablero[0][2] = simbolo
            return 0
        else:
            return "Esa posicion ya esta ocupada"
    elif posicion == 9:
        if tablero[0][4] == ' ':
            tablero[0][4] = simbolo
            return 0
        else:
            return "Esa posicion ya esta ocupada"
    else:
        return "Esa posicion no existe"


def ganador(tablero):
    for simbolo in ["x", "o"]:
        fila0 = tablero[0][0] == simbolo and tablero[0][2] == simbolo and tablero[0][4] == simbolo
        fila2 = tablero[2][0] == simbolo and tablero[2][2] == simbolo and tablero[2][4] == simbolo
        fila4 = tablero[4][0] == simbolo and tablero[4][2] == simbolo and tablero[4][4] == simbolo
        columna0 = tablero[0][0] == simbolo and tablero[2][0] == simbolo and tablero[4][0] == simbolo
        columna2 = tablero[0][2] == simbolo and tablero[2][2] == simbolo and tablero[4][2] == simbolo
        columna4 = tablero[0][4] == simbolo and tablero[2][4] == simbolo and tablero[4][4] == simbolo
        diagonal_abajo = tablero[0][0] == simbolo and tablero[2][2] == simbolo and tablero[4][4] == simbolo
        diagonal_arriba = tablero[4][0] == simbolo and tablero[2][2] == simbolo and tablero[0][4] == simbolo

        if fila0 or fila2 or fila4 or columna0 or columna2 or columna4 or diagonal_abajo or diagonal_arriba:
            if simbolo == "x":
                return 1
            elif simbolo == "o":
                return 2
            break


tablero = [
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "]
]
turno1 = True
jugador1 = ""
jugador2 = ""
turno = 0

print("***********************************************")
print("           Bienvenidos a 3 en Raya             ")
print("***********************************************")
print("La posicion de las casillas son las siguientes:")
print("        7 | 8 |9        ")
print("        4 | 5 |6        ")
print("        1 | 2 |3        ")
print("------------- Disfruta del juego ^^ -----------")
while turno < 9:
    if jugador1 == "":
        jugador1 = input("Ingrese un nombre para el jugador 1 (x) ")
        jugador2 = input("Ingrese un nombre para el jugador 2 (o) ")
    else:
        if turno1:
            print("Turno de", jugador1)
        else:
            print("Turno de", jugador2)

        jugada = int(input())

        valor = cambiar_tablero(tablero, jugada, turno1)
        if valor == 0:
            turno1 = not turno1
            turno += 1
            mostrar_tablero(tablero)
            if ganador(tablero) == 1:
                print("---------------------------")
                print(jugador1, "ganó la partida  ")
                break
            elif ganador(tablero) == 2:
                print("---------------------------")
                print(jugador2, "ganó la partida  ")
                break
        else:
            print(valor)

        if turno == 9:
            print("Empate")