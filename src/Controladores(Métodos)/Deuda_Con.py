from src.BaseDatos.Conexion import conectar_bd
from src.Models.Deuda import Deuda

def crear_deuda(deuda: Deuda):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO deuda (usuario_id, acreedor, monto, fecha_vencimiento, pagado) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (deuda.usuario_id, deuda.acreedor, deuda.monto, deuda.fecha_vencimiento, deuda.pagado))
    conn.commit()
    conn.close()

def obtener_deudas(usuario_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM deuda WHERE usuario_id = %s", (usuario_id,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado
