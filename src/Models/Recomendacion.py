class Recomendacion:
    def __init__(self, id_recomendacion, id_usuario, mensaje, tipo):
        self.__id_recomendacion = id_recomendacion
        self.__id_usuario = id_usuario
        self.__mensaje = mensaje
        self.__tipo = tipo  # Ejemplo: 'Ahorro', 'Gasto', 'Deuda'

    def get_mensaje(self):
        return self.__mensaje

    def get_tipo(self):
        return self.__tipo

    def __str__(self):
        return f"[{self.__tipo}] Recomendación: {self.__mensaje}"
