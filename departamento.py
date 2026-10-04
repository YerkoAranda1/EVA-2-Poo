import sqlite3

class Departamento:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def crearDepto(self):
        conexion = None

        try:
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            sql_insert = """INSERT INTO Departamentos (nombre) VALUES (?)"""
            cursor.execute(sql_insert, (self.nombre,))
            conexion.commit()
            print(f"Departamento {self.nombre} creado con exito.")

        except sqlite3.Error as e:
            print(f"Error al crear departamento: {e}")

        finally:
            if conexion:
                conexion.close()

    @classmethod
    def mostrarDepto(cls):
        conexion = None
        lista_dpto = []

        try:
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            sql_read = """SELECT id, nombre FROM Departamentos"""
            cursor.execute(sql_read)

            resultados = cursor.fetchall()
            for fila in resultados:
                depto = cls(fila[0], fila[1])
                lista_dpto.append(depto)
            return lista_dpto

        except sqlite3.Error as e:
            print(f"Error al listar departamentos: {e}")
            return []
        finally:
            if conexion:
                conexion.close()

    def actualizarDpto(self, nuevo_nombre):
        conexion = None

        try:
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            sql_update = """UPDATE Departamentos SET nombre = ? WHERE id = ?"""
            cursor.execute(sql_update, (nuevo_nombre, self.id))
            conexion.commit()
            print("Departamento actulizado correctamente.")

        except sqlite3.Error as e:
            print(f"Error al actualizar departamento: {e}")
        finally:
            if conexion:
                conexion.close()

    def eliminarDpto(self):
        conexion = None

        try:
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            sql_delete = """DELETE FROM Departamentos WHERE id = ?"""
            cursor.execute(sql_delete, (self.id,))
            conexion.commit()
            print(f"Departamento {self.nombre} eliminado correctamente.")

        except sqlite3.Error as e:
            print(f"Error al eliminar el departamento: {e}")
        finally:
            if conexion:
                conexion.close()

# Yerko Aranda