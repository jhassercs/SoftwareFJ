from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas=1):
        return self.precio * horas

    def descripcion(self):
        return "Servicio de reserva de sala"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias=1):
        return self.precio * dias

    def descripcion(self):
        return "Servicio de alquiler de equipos"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, sesiones=1):
        return self.precio * sesiones

    def descripcion(self):
        return "Servicio de asesoría especializada"