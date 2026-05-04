from reserva import Reserva

class Gestor:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def crear_reserva(self, cliente, servicio, horas):
        reserva = Reserva(cliente, servicio, horas)
        self.reservas.append(reserva)
        return reserva
