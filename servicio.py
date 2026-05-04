from abc import ABC, abstractmethod
from excepciones import ServicioError

class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        costo = self.costo_base * horas
        return costo + (costo * impuesto) - descuento


class AlquilerEquipo(Servicio):
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        costo = (self.costo_base * horas) + 20
        return costo + (costo * impuesto) - descuento


class Asesoria(Servicio):
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        if horas < 1:
            raise ServicioError("Las horas deben ser mayores a 0")
        costo = (self.costo_base * horas) * 1.2
        return costo + (costo * impuesto) - descuento
