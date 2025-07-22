from src.BaseDatos.Conexion import conectar_bd
from src.Models.Ingreso import Ingreso

def crear_ingreso(ingreso: Ingreso):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO ingreso (usuario_id, fuente, monto, fecha) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (ingreso.usuario_id, ingreso.fuente, ingreso.monto, ingreso.fecha))
    conn.commit()
    conn.close()

def obtener_ingresos(usuario_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingreso WHERE usuario_id = %s", (usuario_id,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado
