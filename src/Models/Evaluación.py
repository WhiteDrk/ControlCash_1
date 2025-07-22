class Evaluacion:
    def __init__(self, id_evaluacion, id_usuario, calificacion, fecha):
        self.__id_evaluacion = id_evaluacion
        self.__id_usuario = id_usuario
        self.__calificacion = calificacion
        self.__fecha = fecha

    def get_calificacion(self):
        return self.__calificacion

    def set_calificacion(self, nueva_calificacion):
        if 0 <= nueva_calificacion <= 5:
            self.__calificacion = nueva_calificacion

    def __str__(self):
        return f"Evaluación del {self.__fecha}: {self.__calificacion} estrellas"
