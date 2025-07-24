import pymysql

class BDConexion:
    def __init__(self):
        self.__host = 'localhost'
        self.__puerto = 3306
        self.__usuario = 'root'  # Cambiar según tú usuario
        self.__contrasena = 'tu_contraseña'  # Contraseña
        self.__bd = 'control_cash'  # Nombre de tu base de datos
        self.__conexion = None

    def get_conexion(self):
        #Devuelve la conexión actual
        return self.__conexion

    def conectar_db(self):
        #Establece una conexión a la base de datos
        try:
            self.__conexion = pymysql.connect(
                host=self.__host,
                port=self.__puerto,
                user=self.__usuario,
                password=self.__contrasena,
                database=self.__bd
            )
            print("✅ Conexión a la base de datos exitosa.")
        except pymysql.MySQLError as error:
            print(f"❌ Error al conectar a la base de datos: {error}")
        return self.__conexion

    def cerrar_conexion(self):
        #Cierra la conexión a la base de datos
        if self.__conexion:
            try:
                self.__conexion.close()
                print("🔒 Conexión cerrada correctamente.")
            except pymysql.MySQLError as error:
                print(f"❌ Error al cerrar la conexión: {error}")
        return self.__conexion

#Importante cerrar la base de datos después de cada uno de los usos