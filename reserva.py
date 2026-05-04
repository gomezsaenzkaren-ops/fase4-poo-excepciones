from excepciones import ReservaError

class Reserva:
    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(self.horas)
        except Exception as e:
            self.estado = "Error"
            raise ReservaError("Error al procesar la reserva") from e
        else:
            self.confirmar()
            return costo
        finally:
            print("Proceso de reserva finalizado")
