import sqlite3
from usuario import Usuario

class Empleado(Usuario):

    def __init__(self, id, nombre, email, contrasena, direccion, telefono, salario):
        super().__init__(id, nombre, email, contrasena)
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.__salario = salario

    @property
    def salario(self): return self.__salario

    def registroEmpleado(self):
        conexion = None
        try:
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            
            # 1. Insertamos los datos generales en la tabla Usuarios
            sql_insert_usuario = """INSERT INTO Usuarios (nombre, email, contrasena) VALUES (?, ?, ?)"""
            cursor.execute(sql_insert_usuario, (self.nombre, self.email, self.contrasena))
            
            # 2. Capturamos el ID autoincremental que se acaba de generar
            usuario_id = cursor.lastrowid
            self.id = usuario_id # Actualizamos el objeto en Python
            
            # 3. Insertamos los datos específicos en la tabla Empleados
            sql_insert_empleado = """INSERT INTO Empleados (usuario_id, direccion, telefono, salario) VALUES (?, ?, ?, ?)"""
            cursor.execute(sql_insert_empleado, (usuario_id, self.direccion, self.telefono, self.salario))
            
            # Si ambas inserciones fueron exitosas, confirmamos los cambios
            conexion.commit()
            print(f"Empleado {self.nombre} creado con éxito.")
            
        except sqlite3.Error as e:
            if conexion:
                conexion.rollback() 
            print(f"Error al crear Empleado: {e}")
            
        finally:
            if conexion:
                conexion.close()

    @classmethod
    def mostrarEmpleados(cls):
        conexion = None
        lista_empleados = []

        try:
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            
            # Unimos ambas tablas donde coincida el ID
            sql_read = """
                SELECT u.id, u.nombre, u.email, u.contrasena, 
                       e.direccion, e.telefono, e.salario 
                FROM Empleados e
                JOIN Usuarios u ON e.usuario_id = u.id
            """
            cursor.execute(sql_read)

            resultados = cursor.fetchall()
            for fila in resultados:
                empleado = cls(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                lista_empleados.append(empleado)
                
            return lista_empleados
            
        except sqlite3.Error as e:
            print(f"Error al listar empleados: {e}")
            return []
            
        finally:
            if conexion:
                conexion.close()

    def actualizarSalario(self,nuevo_salario):
        conexion = None 

        try: 
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            sql_update = """UPDATE Empleados SET salario = ? WHERE id = ?"""
            cursor.execute(sql_update, (nuevo_salario, self.id))
            conexion.commit()
            print("Salario Actualizado correctamente.")

        except sqlite3.Error as e:
            print(f"Error al actualizar salario: {e}")
        finally:
            if conexion:
                conexion.close()


# Yerko Aranda
