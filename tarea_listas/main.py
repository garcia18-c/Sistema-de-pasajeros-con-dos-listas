from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número entero válido.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    datos = [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A"),
    ]
    cargados = 0
    for pasajero in datos:
        if lista.añadir(pasajero):
            cargados += 1
    print(f"  Datos de prueba procesados. Nuevos pasajeros: {cargados}")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por número")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print(" C. Cargar datos de prueba                0. Volver")


def ejecutar_menu(lista, titulo, extras=False):
    while True:
        mostrar_opciones(titulo, extras)
        opcion = input("Opción: ").strip().upper()

        if opcion == "1":
            if lista.añadir(leer_pasajero()):
                print("  Pasajero añadido correctamente.")
        elif opcion == "2":
            lista.listar()
        elif opcion == "3":
            posicion = leer_entero("  Posición donde insertar: ")
            pasajero = leer_pasajero()
            if lista.insertar(posicion, pasajero):
                print("  Pasajero insertado correctamente.")
            else:
                print("  No se pudo insertar: revise la posición, capacidad o número duplicado.")
        elif opcion == "4":
            numero = leer_entero("  Número de pasajero: ")
            posicion = lista.buscar(numero)
            if posicion == -1:
                print("  No existe ese pasajero.")
            else:
                if isinstance(lista, MiLista):
                    pasajero = lista.datos[posicion]
                else:
                    pasajero = lista.pasajeros[posicion]
                print(f"  Encontrado en [{posicion}]: {pasajero}")
        elif opcion == "5":
            numero = leer_entero("  Número de pasajero: ")
            print("  Nota: la búsqueda binaria requiere que la lista esté ordenada por número.")
            posicion = lista.buscar_binaria(numero)
            if posicion == -1:
                print("  No existe ese pasajero (o la lista no está ordenada).")
            else:
                if isinstance(lista, MiLista):
                    pasajero = lista.datos[posicion]
                else:
                    pasajero = lista.pasajeros[posicion]
                print(f"  Encontrado en [{posicion}]: {pasajero}")
        elif opcion == "6":
            numero = leer_entero("  Número del pasajero que desea modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if lista.modificar(numero, destino, asiento):
                print("  Pasajero modificado.")
            else:
                print("  No existe ese pasajero.")
        elif opcion == "7":
            posicion = leer_entero("  Posición que desea eliminar: ")
            eliminado = lista.eliminar_por_posicion(posicion)
            print(f"  Eliminado: {eliminado}" if eliminado else "  Posición no válida.")
        elif opcion == "8":
            numero = leer_entero("  Número de pasajero que desea eliminar: ")
            if lista.eliminar_por_valor(numero):
                print("  Pasajero eliminado.")
            else:
                print("  No existe ese pasajero.")
        elif opcion == "9":
            lista.ordenar_asc()
            print("  Lista ordenada de menor a mayor.")
            lista.listar()
        elif opcion == "10":
            lista.ordenar_desc()
            print("  Lista ordenada de mayor a menor.")
            lista.listar()
        elif opcion == "11":
            lista.reversar()
            print("  Orden de la lista invertido.")
            lista.listar()
        elif opcion == "12":
            copia = lista.copiar()
            print("  Copia creada. Se invertirá la copia para demostrar que el orden original no cambia.")
            copia.reversar()
            print("  COPIA:")
            copia.listar()
            print("  ORIGINAL (sin cambiar su orden):")
            lista.listar()
        elif opcion == "13":
            print(f"  Cantidad de pasajeros: {lista.longitud()}")
        elif opcion == "14" and extras:
            destino = input("  Destino que desea filtrar: ").strip()
            encontrados = lista.filtrar_por_destino(destino)
            if encontrados:
                for pasajero in encontrados:
                    print(f"  {pasajero}")
            else:
                print("  No hay pasajeros para ese destino.")
        elif opcion == "15" and extras:
            encontrados = lista.mayores_de_edad()
            if encontrados:
                for pasajero in encontrados:
                    print(f"  {pasajero}")
            else:
                print("  No hay pasajeros mayores de edad.")
        elif opcion == "C":
            cargar_datos_prueba(lista)
        elif opcion == "0":
            return
        else:
            print("  Opción no válida.")


def menu_lista1():
    ejecutar_menu(lista1, "MENÚ 1 · MiLista")


def menu_lista2():
    ejecutar_menu(lista2, "MENÚ 2 · list de Python", extras=True)


def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            menu_lista1()
        elif opcion == "2":
            menu_lista2()
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
