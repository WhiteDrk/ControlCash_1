class Gasto:
    def __init__(self, id_gasto, id_usuario, descripcion, monto, fecha):
        self._id_gasto = id_gasto
        self._id_usuario = id_usuario
        self._descripcion = descripcion
        self._monto = monto
        self._fecha = fecha

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        if nuevo_monto < 0:
            raise ValueError("El gasto no puede ser negativo.")
        self._monto = nuevo_monto

    def __str__(self):
        return f"Gasto({self._descripcion}, ${self._monto})"
