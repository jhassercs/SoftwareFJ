from excepciones import ClienteInvalidoError

class Cliente:

    def __init__(self, nombre, edad, correo):

        if not nombre.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacío")

        if edad < 18:
            raise ClienteInvalidoError("La edad debe ser mayor de 18")

        if "@" not in correo:
            raise ClienteInvalidoError("Correo inválido")

        self.__nombre = nombre
        self.__edad = edad
        self.__correo = correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - Edad: {self.__edad}"

    def get_nombre(self):
        return self.__nombre