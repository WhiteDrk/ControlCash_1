class Notificacion:
    def __init__(self, id_notificacion, id_usuario, mensaje, fecha):
        self.__id_notificacion = id_notificacion
        self.__id_usuario = id_usuario
        self.__mensaje = mensaje
        self.__fecha = fecha

    def get_mensaje(self):
        return self.__mensaje

    def __str__(self):
        return f"[{self.__fecha}] Notificación: {self.__mensaje}"
