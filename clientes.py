from excepciones import ClienteError

class Cliente:
    def __init__(self, nombre, documento, correo):
        try:
            if not nombre.replace(" ", "").isalpha():
                raise ClienteError("El nombre solo debe contener letras")

            if len(documento) < 5:
                raise ClienteError("El documento debe tener al menos 5 caracteres")

            if "@" not in correo:
                raise ClienteError("El correo no es válido")

            self.__nombre = nombre
            self.__documento = documento
            self.__correo = correo

        except Exception as e:
            raise ClienteError("Error al crear el cliente") from e

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento
