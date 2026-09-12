print("--- BIENVENIDO A LA ARENA ---")

# Nombre del Gladiador
nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")


# Estadísticas iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3

ataque_jugador = 15
ataque_enemigo = 12

turno_jugador = True


print()
print("=== INICIO DEL COMBATE ===")


# Ciclo de combate
while vida_jugador > 0 and vida_enemigo > 0:

    print()
    print(nombre, "(HP:", vida_jugador, ") vs Enemigo (HP:", vida_enemigo, ") | Pociones:", pociones)

    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    # Validación de la opción
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)


    # ATAQUE PESADO
    if opcion == 1:

        if vida_enemigo < 20:
            daño = ataque_jugador * 1.5
            print("¡Golpe crítico!")
        else:
            daño = ataque_jugador

        vida_enemigo -= daño

        print("¡Atacaste al enemigo por", daño, "puntos de daño!")


    # RÁFAGA VELOZ
    elif opcion == 2:

        print(">> ¡Inicias una ráfaga de golpes!")

        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")


    # CURAR
    elif opcion == 3:

        if pociones > 0:
            vida_jugador += 30
            pociones -= 1

            print("¡Usaste una poción y recuperaste 30 puntos de vida!")

        else:
            print("¡No quedan pociones!")


    # ATAQUE DEL ENEMIGO
    if vida_enemigo > 0:
        vida_jugador -= ataque_enemigo
        print(">> ¡El enemigo contraataca por 12 puntos!")


# FIN DEL JUEGO
print()

if vida_jugador > 0:
    print("¡VICTORIA!", nombre, "ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
