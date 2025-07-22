from src.BaseDatos.Conexion import conectar_bd
from src.Models.gasto import Gasto

def crear_gasto(gasto: Gasto):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO gasto (usuario_id, descripcion, monto, fecha) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (gasto.usuario_id, gasto.descripcion, gasto.monto, gasto.fecha))
    conn.commit()
    conn.close()

def obtener_gastos(usuario_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "SELECT * FROM gasto WHERE usuario_id = %s"
    cursor.execute(query, (usuario_id,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado
