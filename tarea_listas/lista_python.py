from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Implementa las operaciones usando métodos propios de list."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese número.")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, pasajero in enumerate(self.pasajeros):
            print(f"  [{i}] {pasajero}")

    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese número.")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        posiciones = [
            i for i, pasajero in enumerate(self.pasajeros)
            if pasajero.numero == numero
        ]
        return posiciones[0] if posiciones else -1

    def buscar_binaria(self, numero):
        numeros = [pasajero.numero for pasajero in self.pasajeros]
        posicion = bisect_left(numeros, numero)
        if posicion < len(numeros) and numeros[posicion] == numero:
            return posicion
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)
        if posicion == -1:
            return False
        self.pasajeros[posicion].destino = nuevo_destino
        self.pasajeros[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        cantidad_inicial = len(self.pasajeros)
        self.pasajeros = [
            pasajero for pasajero in self.pasajeros
            if pasajero.numero != numero
        ]
        return len(self.pasajeros) < cantidad_inicial

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda pasajero: pasajero.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda pasajero: pasajero.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):
        return [
            pasajero for pasajero in self.pasajeros
            if pasajero.destino.lower() == destino.lower()
        ]

    def mayores_de_edad(self):
        return [
            pasajero for pasajero in self.pasajeros
            if pasajero.es_mayor_de_edad()
        ]
