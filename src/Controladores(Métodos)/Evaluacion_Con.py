from src.BaseDatos.Conexion import conectar_bd
from src.Models.Evaluación import Evaluacion

def crear_evaluacion(evaluacion: Evaluacion):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO evaluacion (usuario_id, puntuacion, fecha) VALUES (%s, %s, %s)"
    cursor.execute(query, (evaluacion.usuario_id, evaluacion.puntuacion, evaluacion.fecha))
    conn.commit()
    conn.close()

def obtener_evaluaciones(usuario_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM evaluacion WHERE usuario_id = %s", (usuario_id,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado
