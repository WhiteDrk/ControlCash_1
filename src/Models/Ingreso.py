class Ingreso:
    def __init__(self, id_ingreso, id_usuario, fuente, monto, fecha):
        self._id_ingreso = id_ingreso
        self._id_usuario = id_usuario
        self._fuente = fuente
        self._monto = monto
        self._fecha = fecha

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        if nuevo_monto < 0:
            raise ValueError("El ingreso no puede ser negativo.")
        self._monto = nuevo_monto

    def __str__(self):
        return f"Ingreso({self._fuente}, ${self._monto})"
