# Piedra Papel o Tijera

import random

rondas = 0
opciones = ("piedra", "papel", "tijera")
puntaje_jugador = 0
puntaje_computadora = 0
ultima_partida = 6

while rondas < ultima_partida:
    rondas += 1
    print(f'----------Ronda {rondas}----------')
    opciones_usuario = input("Elija una opcion => ").lower()
    
    if opciones_usuario not in opciones:
        print("La opcion escrita no es valida")
        continue
    
    opciones_computadora = random.choice(opciones)
    
    if opciones_computadora == opciones_usuario:
        print("¡Empate!")
        print(f"Puntaje => Usuario: {puntaje_jugador} vs Computadora: {puntaje_computadora}")
    elif opciones_usuario == "piedra":
        if opciones_computadora == "tijera":
            puntaje_jugador += 1
            print("Gano el jugador")
            print(f"La opcion elegida del jugador  {opciones_usuario} le gana a la opcion de la computadora {opciones_computadora}")
            print(f"Puntaje => Usuario: {puntaje_jugador} vs Computadora: {puntaje_computadora}")             
        else:
            puntaje_computadora += 1
            print("Gano la computadora")
            print(f"La opcion elegida de la computadora {opciones_computadora} le gana a la opcion del jugador {opciones_usuario}")
            print(f"Puntaje => Usuario: {puntaje_jugador} vs Computadora: {puntaje_computadora}")
            
    elif opciones_usuario == "tijera":
        if opciones_computadora == "papel":
            puntaje_jugador += 1
            print("Gano el jugador")
            print(f"La opcion elegida del jugador {opciones_usuario} le gana a la opcion de la computadora {opciones_computadora}")
            print(f"Puntaje => Usuario: {puntaje_jugador} vs Computadora: {puntaje_computadora}")
        else:
            puntaje_computadora += 1
            print("Gano la computadora")
            print(f"La opcion elegida de la computador{opciones_computadora} le gana a la opcion del jugador {opciones_usuario}")
            print(f"Puntaje => Usuario: {puntaje_jugador} vs Computadora: {puntaje_computadora}")

    elif opciones_usuario == "papel":
        if opciones_computadora == "piedra":
            puntaje_jugador += 1
            print("Gano el jugador")
            print(f"La opcion elegida del jugador {opciones_usuario} le gana a la opcion de la computadora {opciones_computadora}")
            print(f"Puntaje => Usuario: {puntaje_jugador} vs Computadora: {puntaje_computadora}")
        else:
            puntaje_computadora += 1
            print("Gano la computadora")
            print(f"La opcion elegida de la computadora {opciones_computadora} le gana a la opcion del jugador '{opciones_usuario}'")
            print(f"Puntaje => Usuario: {puntaje_jugador} vs Computadora: {puntaje_computadora}")

    if (puntaje_jugador == 3 and puntaje_computadora < 3) or (puntaje_computadora == 3 and puntaje_jugador < 3):
        break