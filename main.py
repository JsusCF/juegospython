from random import randint

respuesta = "si"
puntajejugador = 0
puntajecomputadora = 0
while respuesta == "si":
    print("********************************")
    print("      Piedra Papel Tijera       ")
    print("********************************")
    jugador = input("Escribe tu jugada: Piedra, Papel o Tijera: ")

    eleccion = ["piedra", "papel", "tijera"]
    computadora = eleccion[randint(0, 2)]
    print("La computadora elige:", computadora)

    if computadora == jugador:
        print("Hay un empate")
    elif computadora == "piedra" and jugador == "tijera":
        print("La computadora gana. La piedra le gana a tijera ")
        puntajecomputadora += 1
    elif computadora == "piedra" and jugador == "papel":
        print("Tu ganas. El papel le gana a la piedra ")
        puntajejugador += 1
    elif computadora == "tijera" and jugador == "piedra":
        print("Tu ganas. La piedra le gana a tijera ")
        puntajejugador += 1
    elif computadora == "tijera" and jugador == "papel":
        print("La computadora gana. La tijera le gana al papel ")
        puntajecomputadora += 1
    elif computadora == "papel" and jugador == "tijera":
        print("Tu ganas. La tijera le gana al papel ")
        puntajejugador += 1
    elif computadora == "papel" and jugador == "piedra":
        print("La computadora gana. El papel le gana a la piedra ")
        puntajecomputadora += 1
    print("el puntaje del jugador es:", puntajejugador)
    print("El puntaje de la computadora es:", puntajecomputadora)
    print("Desea Continuar Si - No")
    respuesta = input()