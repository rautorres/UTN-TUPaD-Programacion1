energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

seleccion_jugada = ""
jugada = 0
forzar_seguidas = 0

print(" ||| Escape Room: La Bóveda ||| ")

nombre_agente = input("Agente, ingrese su nombre: ")

print("Energia = 100")
print("Tiempo = 12")

while not nombre_agente.isalpha():
    print("Error: Su nombre debe ser ingresado solamente mediante letras")
    nombre_agente = input("Agente, ingrese su nombre: ")

#while seleccion_jugada != 3:
while True:

    print(" // Opciones de Jugada // ")
    print("1. Forzar Cerradura (costo: -20 energía, -2 tiempo)")
    print("2. Hackear Panel (costo: -10 energía, -3 tiempo)")
    print("3. Descansar (costo: +15 energía (máx 100), -1 tiempo; con alarma en On -10 energía extra)")

    seleccion_jugada = input("Elija su jugada (1, 2 o 3): ")

    while not seleccion_jugada.isdigit() or int(seleccion_jugada) < 1 or int(seleccion_jugada) > 3:
        print("Error: Debe elegir una opción entre 1 y 3")
        seleccion_jugada = input("Elija su jugada (1, 2 o 3)")

    seleccion_jugada = int(seleccion_jugada)

    if seleccion_jugada == 1:
        print("Forzar Cerradura")

        jugada = 0

        if energia < 40:
            jugada = input("¡Riesgo de alarma! Seleccione 1, 2 o 3: ")
        
            while not jugada.isdigit() or int(jugada) < 1 or int(jugada) > 3:
                print("Error: Debe elegir un número entre 1 y 3")
                jugada = input("¡Riesgo de alarma! Seleccione 1, 2 o 3: ")
        
            jugada = int(jugada)
        
            if jugada == 1:
                print("Intentar forzar cerradura")
        
            elif jugada == 2:
                print("Hackear panel")
                seleccion_jugada = 2
        
            elif jugada == 3:
                print("Huir")
                alarma = True

            if jugada == 2:
                forzar_seguidas = 0
                
                energia -= 10
                tiempo -= 3

                for paso in range(4):
                    print("Paso", paso + 1, "de 4")

                    letra = input("Ingrese una letra: ")

                    while len(letra) != 1 or not letra.isalpha():
                        print("Error: debe ingresar una sola letra.")
                        letra = input("Ingrese una letra: ")

                    codigo_parcial += letra

                print("Código parcial:", codigo_parcial)

                if len(codigo_parcial) >= 8:
                    cerraduras_abiertas += 1
                    codigo_parcial = ""
                    print("¡Código completo! Cerradura abierta.")

        if energia >= 40 or jugada == 1:
            energia -= 20
            tiempo -= 2
            forzar_seguidas += 1

            if forzar_seguidas == 3:
                alarma = True
                print("¡La cerradura se trabó!")
                print("Alarma Activada")

            else:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

    elif seleccion_jugada == 2:
        print("Hackear Panel")
        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        for paso in range(4):
            print("Paso", paso + 1, "de 4")

            letra = input("Ingrese una letra: ")

            while len(letra) != 1 or not letra.isalpha():
                print("Error: debe ingresr una sola letra.")
                letra = input("Ingrese una letra: ")

            codigo_parcial += letra

        print("Código parcial:", codigo_parcial)

        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("¡Código completo! Cerradura abierta.")

    elif seleccion_jugada == 3:
        print("Descansar")
        forzar_seguidas = 0

        energia += 15
        tiempo -= 1

        if energia > 100:
            energia = 100

        if alarma == True:
            energia -= 10

    if cerraduras_abiertas == 3:
        print("¡Felicitaciones! Abriste las 3 cerraduras.")
        break

    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("¡Alarma! La bóveda quedó bloqueada.")
        print("¡Perdiste!")
        break

    if energia <= 0:
        print("¡Perdiste! Te quedaste sin energía.")
        break

    if tiempo <= 0:
        print("¡Perdiste! Se acabó el tiempo.")
        break