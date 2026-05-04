from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from gestor import Gestor
import traceback

def log_evento(mensaje):
    with open("logs.txt", "a") as f:
        f.write("[EVENTO] " + mensaje + "\n")

def log_error(error):
    with open("logs.txt", "a") as f:
        f.write("[ERROR] " + str(error) + "\n")
        f.write(traceback.format_exc() + "\n")

gestor = Gestor()

try:
    c1 = Cliente("Ana", "12345", "ana@mail.com")
    gestor.agregar_cliente(c1)
    log_evento("Cliente Ana agregado")

    c2 = Cliente("Pedro123", "12", "correo")
except Exception as e:
    log_error(e)

s1 = ReservaSala("Sala Juntas", 50)
s2 = AlquilerEquipo("Proyector", 30)
s3 = Asesoria("Asesoria TI", 100)

gestor.agregar_servicio(s1)
gestor.agregar_servicio(s2)
gestor.agregar_servicio(s3)

try:
    r1 = gestor.crear_reserva(c1, s1, 2)
    print("Costo:", r1.procesar())
    log_evento("Reserva sala confirmada")

    r2 = gestor.crear_reserva(c1, s3, 0)
    print("Costo:", r2.procesar())
except Exception as e:
    log_error(e)

try:
    r3 = gestor.crear_reserva(c1, s2, 3)
    r3.cancelar()
    log_evento("Reserva cancelada correctamente")
except Exception as e:
    log_error(e)
