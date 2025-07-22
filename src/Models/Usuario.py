class Usuario:
    def __init__(self, id_usuario, nombre, correo, contrasena):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena

    def __str__(self):
        return f"Usuario({self._id_usuario}, {self._nombre})"
