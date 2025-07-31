from src.Models.gasto import Gasto
from src.BaseDatos.Conexion_experimento import DatabaseConnection

#Operaciones CRUD

# CREATE
def crear_gasto(gasto: Gasto):
    db = DatabaseConnection()
    query = "INSERT INTO gasto (usuario_id, descripcion, monto, fecha) VALUES (%s, %s, %s, %s)"
    params= (gasto.usuario_id, gasto.descripcion, gasto.monto, gasto.fecha)
    db.execute_commit(query, params)

# READ
def obtener_gastos(usuario_id):
    db = DatabaseConnection()
    query = "SELECT * FROM gasto WHERE usuario_id = %s"
    return db.fetch_all(query, (usuario_id,))

# UPDATE
def actualizar_gasto(gasto_id, nueva_descripcion, nuevo_monto):
    db = DatabaseConnection()
    query = "UPDATE gasto SET descripcion = %s, monto = %s WHERE id = %s"
    params = (nueva_descripcion, nuevo_monto, gasto_id)
    db.execute_commit(query, params)

# DELETE
def eliminar_gasto(gasto_id):
    db = DatabaseConnection()
    query = "DELETE FROM gasto WHERE id = %s"
    db.execute_commit(query, (gasto_id,))

