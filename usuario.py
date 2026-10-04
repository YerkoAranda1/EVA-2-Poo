import sqlite3
class Usuario:

    def __init__(self,id,nombre,email,contrasena):
        self.id = id
        self.nombre = nombre
        self._email = email
        self._contrasena = contrasena

    @property # Decorador: lo usamos para obtener los datos protegidos, hasheados o privados. 
    def email(self): return self._email
    @property 
    def contrasena(self): return self._contrasena

    def CrearUsuario(self):
        conexion = None
        # Conexion e Insert de la base de datos

        try:
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            sql_insert = """INSERT INTO Usuarios (nombre, email, contrasena)
                            VALUES (?, ?, ?)"""
            cursor.execute(sql_insert, (self.nombre, self._email, self._contrasena))
            conexion.commit()
            print(f"Usuario {self.nombre} creado con Exito.")

        except sqlite3.Error as e:
            print(f"Error al cear usuario {e}")

        finally:
            if conexion:
                conexion.close()

    @classmethod 
    def LeerUsuario(cls):
        conexion = None
        lista_usuario =[]
        #Conexion y Read de la base de datos | Creacion de lista para poder leer la consulta

        try:
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            sql_read = """SELECT id, nombre, email, contrasena FROM Usuarios"""
            cursor.execute(sql_read)
            # Guardamos los resultados en una lista para poder leerla con un for
            resultados = cursor.fetchall()
            for fila in resultados:
                usuario = cls(fila[0], fila[1], fila[2], fila[3])
                lista_usuario.append(usuario)
            return lista_usuario
        
        except sqlite3.Error as e:
            print(f"Error al listar usuarios: {e}")
            return []
        finally:
            if conexion:
                conexion.close()

    def ActualizarUsuario(self, nueva_contrasena):
        conexion = None
        # Conexion y Update de tabla bd

        try:
            conexion = sqlite3.connect("empresa.db")
            cursor = conexion.cursor()
            sql_update = """UPDATE Usuarios SET contrasena = ? WHERE id = ?"""
            cursor.execute(sql_update, (nueva_contrasena, self.id))
            conexion.commit()
            print ("Contraseña actualizada correctamente.")

        except sqlite3.Error as e:
            print(f"Error al actualizar contraseña {e}")
        finally:
            if conexion:
                conexion.close()

    def Login(self):
        print(f"Bienvenido {self.nombre}")
        