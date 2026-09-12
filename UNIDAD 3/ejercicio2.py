#Credenciales 
usuario_correcto = "alumno"
clave_correcta = "python123"

usuario = ""
clave = ""

intentos = 0
maximo_intento = 3

opcion_menu = ""
opciones = 5


print("/// Acceso a Campus ///")

while intentos < maximo_intento:

    usuario = input("Ingrese usuario compartido: ")
    clave = input("Ingrese clave compartida: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Usuario y Clave Correctos")
        break

    print("Usuario o clave Incorrectos")

    intentos = intentos + 1

    if intentos >= maximo_intento:
            print("Cuenta bloqueada")
            break

#while usuario == usuario_correcto and clave == clave_correcta:
while True:

    opcion_menu = input(" - Elegir opción del Menú (Opciones del 1 - 4): ")


    if opcion_menu.isdigit():

        opcion_menu = int(opcion_menu)

        if opcion_menu >= 1 and opcion_menu <= 4:
            print("Opción Válida")

            if opcion_menu == 1:
                print("1. Ver estado de Inscripción")
                print("Inscripto")

            if opcion_menu == 2:
                print("2. Cambiar Clave")

                nueva_clave = input("Nueva Clave: ")

                if len(nueva_clave) < 6:
                    print("La clave debe tener mínimo 6 caracteres")

                else:
                    confirmacion = input("Confirmar Clave: ")

                    if nueva_clave == confirmacion:
                        clave_correcta = nueva_clave
                        print("Clave Actualizada")
                    else: 
                        print("Claves no coinciden")

            if opcion_menu == 3:
                print("3. Mensaje del Día")
                print("Criatura estúpida, ponete a estudiar")

            if opcion_menu == 4:
                print("Salir")
                break

        else:
            print("Las opciones disponibles son del 1 al 4")
    else:
        print("Debe ingresar un número")

