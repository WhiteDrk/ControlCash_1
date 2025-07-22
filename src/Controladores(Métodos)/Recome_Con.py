from src.BaseDatos.Conexion import conectar_bd
from src.Models.Recomendacion import Recomendacion

def crear_recomendacion(recomendacion: Recomendacion):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO recomendacion (usuario_id, texto, fecha) VALUES (%s, %s, %s)"
    cursor.execute(query, (recomendacion.usuario_id, recomendacion.texto, recomendacion.fecha))
    conn.commit()
    conn.close()

def obtener_recomendaciones(usuario_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recomendacion WHERE usuario_id = %s", (usuario_id,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado
