from src.BaseDatos.Conexion import conectar_bd
from src.Models.Usuario import Usuario

def crear_usuario(usuario: Usuario):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO usuario (nombre, correo, contrasena) VALUES (%s, %s, %s)"
    cursor.execute(query, (usuario.nombre, usuario.correo, usuario.contrasena))
    conn.commit()
    conn.close()

def obtener_usuarios():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    resultado = cursor.fetchall()
    conn.close()
    return resultado
