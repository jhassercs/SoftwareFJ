from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva

clientes = []
reservas = []
servicios = []

# Servicios disponibles
servicios.append(ReservaSala("Sala VIP", 50000))
servicios.append(AlquilerEquipo("VideoBeam", 30000))
servicios.append(AsesoriaEspecializada("Programación", 100000))


def guardar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")


while True:

    print("\n===== SOFTWARE FJ =====")
    print("1. Registrar cliente")
    print("2. Ver servicios")
    print("3. Crear reserva")
    print("4. Ver reservas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # REGISTRAR CLIENTE
    if opcion == "1":

        try:

            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            correo = input("Correo: ")

            cliente = Cliente(nombre, edad, correo)

            clientes.append(cliente)

            print("Cliente registrado correctamente")

        except Exception as e:

            print("Error:", e)
            guardar_log(str(e))

    # VER SERVICIOS
    elif opcion == "2":

        try:

            print("\nSERVICIOS DISPONIBLES")

            for i, servicio in enumerate(servicios):

                print(
                    f"{i + 1}. {servicio.descripcion()} "
                    f"- Precio: ${servicio.precio}"
                )

        except Exception as e:

            print("Error:", e)
            guardar_log(str(e))

    # CREAR RESERVA
    elif opcion == "3":

        try:

            if len(clientes) == 0:

                raise Exception(
                    "Debe registrar un cliente primero"
                )

            print("\nCLIENTES")

            for i, cliente in enumerate(clientes):

                print(f"{i + 1}. {cliente.get_nombre()}")

            cliente_index = int(input("Seleccione cliente: ")) - 1

            print("\nSERVICIOS")

            for i, servicio in enumerate(servicios):

                print(f"{i + 1}. {servicio.descripcion()}")

            servicio_index = int(input("Seleccione servicio: ")) - 1

            duracion = int(input("Duración: "))

            reserva = Reserva(
                clientes[cliente_index],
                servicios[servicio_index],
                duracion
            )

            reserva.confirmar()

            reservas.append(reserva)

            print("Reserva creada exitosamente")

        except Exception as e:

            print("Error:", e)
            guardar_log(str(e))

    # VER RESERVAS
    elif opcion == "4":

        try:

            if len(reservas) == 0:

                print("No hay reservas")

            else:

                print("\nLISTA DE RESERVAS")

                for reserva in reservas:

                    print(reserva.mostrar_reserva())

        except Exception as e:

            print("Error:", e)
            guardar_log(str(e))

    # SALIR
    elif opcion == "5":

        print("Saliendo del sistema...")
        break

    else:

        print("Opción inválida")