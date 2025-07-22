class Deuda:
    def __init__(self, id_deuda, id_usuario, descripcion, monto, fecha_limite):
        self.__id_deuda = id_deuda
        self.__id_usuario = id_usuario
        self.__descripcion = descripcion
        self.__monto = monto
        self.__fecha_limite = fecha_limite

    def get_monto(self):
        return self.__monto

    def set_monto(self, nuevo_monto):
        if nuevo_monto >= 0:
            self.__monto = nuevo_monto

    def __str__(self):
        return f"Deuda: {self.__descripcion} - {self.__monto} a pagar antes de {self.__fecha_limite}"

