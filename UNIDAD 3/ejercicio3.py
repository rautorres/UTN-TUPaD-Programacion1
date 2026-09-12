#//VARIABLES
opcion_menu = ""
opciones = 5

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

print(" /// Agenda de Turnos /// ")

nombre_operador = input("Ingrese nombre del Operador: ")

while not nombre_operador.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre_operador = input("Ingrese nombre del Operador: ")

while opcion_menu != 5:

    print(" // Menú // ")
    print("1. Reservar Turno")
    print("2. Cancelar Turno (Ingrese su nombre)")
    print("3. Ver agenda disponible")
    print("4. Resumen General")
    print("5. Cierre de Sesión")

    opcion_menu = input("Seleccione una opción (1 a 5): ")

    while not opcion_menu.isdigit():
        print("Error: debe ingresar un número.")
        opcion_menu = input("Seleccione la opción deseada del menú (Opción 1 a 5): ")

    opcion_menu = int(opcion_menu)

    if opcion_menu == 1:
        print("1. Reservar Turno")
        dia = input("Seleccione el día, 1 = Lunes / 2 = Martes: ")

        while not dia.isdigit():
            print("Error: debe ingresar un número.")
            dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

        dia = int(dia)

        while dia != 1 and dia != 2:
            print("Error: debe seleccionar 1 para Lunes o 2 para Martes.")
            dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

            while not dia.isdigit():
                print("Error: debe ingresar un número.")
                dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

            dia = int(dia)

        nombre_paciente = input("Ingrese nombre del paciente: ")

        while not nombre_paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            nombre_paciente = input("Ingrese nombre del paciente: ")

        if dia == 1:

            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                print("Error: el paciente ya tiene un turno el Lunes.")

            elif lunes1 == "":
                lunes1 = nombre_paciente
                print("Turno reservado correctamente.")

            elif lunes2 == "":
                lunes2 = nombre_paciente
                print("Turno reservado correctamente.")

            elif lunes3 == "":
                lunes3 = nombre_paciente
                print("Turno reservado correctamente.")

            elif lunes4 == "":
                lunes4 = nombre_paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el Lunes.")

        elif dia == 2:

            if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                print("Error: el paciente ya tiene un turno el Martes.")

            elif martes1 == "":
                martes1 = nombre_paciente
                print("Turno reservado correctamente.")

            elif martes2 == "":
                martes2 = nombre_paciente
                print("Turno reservado correctamente.")

            elif martes3 == "":
                martes3 = nombre_paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el Martes.")

        elif opcion_menu == 2:
            print("2. Cancelar Turno")

        elif opcion_menu == 3:
            print("3. Ver agenda disponible")

        elif opcion_menu == 4:
            print("4. Resumen General")

        elif opcion_menu == 5:
            print("5. Cierre de Sesión")

        else:
            print("Error: opción inválida.")


    elif opcion_menu == 2:
        print("2. Cancelar Turno (Ingrese su nombre): ")

        dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

        while not dia.isdigit():
            print("Error: debe ingresar un número.")
            dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

        dia = int(dia)

        while dia != 1 and dia != 2:
            print("Error: debe seleccionar 1 para Lunes o 2 para Martes.")
            dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

        while not dia.isdigit():
            print("Error: debe ingresar un número.")
            dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

        dia = int(dia)

    nombre_paciente = input("Ingrese nombre del paciente: ")

    while not nombre_paciente.isalpha():
        print("Error: el nombre debe contener solo letras.")
        nombre_paciente = input("Ingrese nombre del paciente: ")

    if dia == 1:

        if nombre_paciente == lunes1:
            lunes1 = ""
            print("Turno cancelado correctamente.")

        elif nombre_paciente == lunes2:
            lunes2 = ""
            print("Turno cancelado correctamente.")

        elif nombre_paciente == lunes3:
            lunes3 = ""
            print("Turno cancelado correctamente.")

        elif nombre_paciente == lunes4:
            lunes4 = ""
            print("Turno cancelado correctamente.")

        else:
            print("El paciente no tiene un turno el Lunes.")

    elif dia == 2:

        if nombre_paciente == martes1:
            martes1 = ""
            print("Turno cancelado correctamente.")

        elif nombre_paciente == martes2:
            martes2 = ""
            print("Turno cancelado correctamente.")

        elif nombre_paciente == martes3:
            martes3 = ""
            print("Turno cancelado correctamente.")

        else:
            print("El paciente no tiene un turno el Martes.")

    elif opcion_menu == 3:
        print("3. Ver agenda disponible")

        dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

        while not dia.isdigit():
            print("Error: debe ingresar un número.")
            dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

        dia = int(dia)

        while dia != 1 and dia != 2:
            print("Error: debe seleccionar 1 para Lunes o 2 para Martes.")
            dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

            while not dia.isdigit():
                print("Error: debe ingresar un número.")
                dia = input("Seleccione el día: 1 = Lunes / 2 = Martes: ")

            dia = int(dia)

        if dia == 1:

            print("/// Agenda del Lunes ///")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)

        elif dia == 2:

            print("/// Agenda del Martes ///")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

    elif opcion_menu == 4:
        print("4. Resumen General")

        ocupados_lunes = 0

        if lunes1 != "":
            ocupados_lunes = ocupados_lunes + 1

        if lunes2 != "":
            ocupados_lunes = ocupados_lunes + 1

        if lunes3 != "":
            ocupados_lunes = ocupados_lunes + 1

        if lunes4 != "":
            ocupados_lunes = ocupados_lunes + 1

            ocupados_martes = 0

        if martes1 != "":
            ocupados_martes = ocupados_martes + 1

        if martes2 != "":
            ocupados_martes = ocupados_martes + 1

        if martes3 != "":
            ocupados_martes = ocupados_martes + 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("/// Resumen General ///")
        print("Lunes - Ocupados:", ocupados_lunes)
        print("Lunes - Disponibles:", disponibles_lunes)

        print("Martes - Ocupados:", ocupados_martes)
        print("Martes - Disponibles:", disponibles_martes)

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es Lunes.")

        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos es Martes.")

        else:
            print("Hay empate: ambos días tienen la misma cantidad de turnos.")

    elif opcion_menu == 5:
        print("5. Cierre de Sesión")

    else:
        print("Error: opción inválida.")
