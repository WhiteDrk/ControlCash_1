from src.BaseDatos.Conexion import conectar_bd
from src.Models.Notificación import Notificacion

def crear_notificacion(notificacion: Notificacion):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO notificacion (usuario_id, mensaje, fecha) VALUES (%s, %s, %s)"
    cursor.execute(query, (notificacion.usuario_id, notificacion.mensaje, notificacion.fecha))
    conn.commit()
    conn.close()

def obtener_notificaciones(usuario_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notificacion WHERE usuario_id = %s", (usuario_id,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

