import sqlite3
from usuario import Usuario
from empleado import Empleado
from departamento import Departamento

def preparar_tablas():
    """Crea todas las tablas unificadas en la misma base de datos."""
    conexion = sqlite3.connect("empresa.db")
    cursor = conexion.cursor()
    
    # Tabla Usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    
    # Tabla Empleados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Empleados (
            usuario_id INTEGER PRIMARY KEY,
            direccion TEXT,
            telefono TEXT,
            salario REAL,
            FOREIGN KEY (usuario_id) REFERENCES Usuarios (id) ON DELETE CASCADE
        )
    ''')

    # Tabla Departamentos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()


# ==========================================
# SUBMENÚS
# ==========================================

def menu_usuario():
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Crear nuevo Usuario")
        print("2. Listar todos los Usuarios")
        print("3. Actualizar contraseña (por ID)")
        print("4. Volver al menú principal")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            email = input("Email: ")
            contra = input("Contraseña: ")
            
            nuevo_usuario = Usuario(None, nombre, email, contra)
            nuevo_usuario.CrearUsuario()

        elif opcion == '2':
            lista = Usuario.LeerUsuario()
            if lista:
                print("\n--- USUARIOS EN BASE DE DATOS ---")
                for u in lista:
                    print(f"ID: {u.id} | Nombre: {u.nombre} | Email: {u.email} | Pass: {u.contrasena}")
            else:
                print("No hay usuarios registrados aún.")

        elif opcion == '3':
            try:
                id_modificar = int(input("Ingresa el ID del usuario a modificar: "))
                nueva_pass = input("Ingresa la nueva contraseña: ")
                
                usuario_modificar = Usuario(id_modificar, "", "", "")
                usuario_modificar.ActualizarUsuario(nueva_pass)
            except ValueError:
                print("Error: El ID debe ser numérico.")

        elif opcion == '4':
            break
        else:
            print("Opción inválida.")


def menu_empleado():
    while True:
        print("\n--- GESTIÓN DE EMPLEADOS ---")
        print("1. Crear nuevo Empleado")
        print("2. Listar todos los Empleados")
        print("3. Actualizar salario (por ID)")
        print("4. Volver al menú principal")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            email = input("Email: ")
            contra = input("Contraseña: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            try:
                salario = float(input("Salario: "))
                nuevo_empleado = Empleado(None, nombre, email, contra, direccion, telefono, salario)
                # Asegúrate de que el nombre del método coincida con el de tu clase Empleado
                nuevo_empleado.registroEmpleado() 
            except ValueError:
                print("Error: El salario debe ser numérico.")

        elif opcion == '2':
            lista = Empleado.mostrarEmpleados()
            if lista:
                print("\n--- EMPLEADOS EN BASE DE DATOS ---")
                for e in lista:
                    print(f"ID: {e.id} | Nombre: {e.nombre} | Email: {e.email} | Salario: ${e.salario}")
            else:
                print("No hay empleados registrados aún.")

        elif opcion == '3':
            try:
                id_modificar = int(input("Ingresa el ID del empleado a modificar: "))
                nuevo_salario = float(input("Ingresa el nuevo salario: "))
                
                empleado_modificar = Empleado(id_modificar, "", "", "", "", "", 0)
                empleado_modificar.actualizarSalario(nuevo_salario)
            except ValueError:
                print("Error: El ID y el salario deben ser numéricos.")

        elif opcion == '4':
            break
        else:
            print("Opción inválida.")


def menu_departamento():
    while True:
        print("\n--- GESTIÓN DE DEPARTAMENTOS ---")
        print("1. Crear nuevo Departamento")
        print("2. Listar todos los Departamentos")
        print("3. Actualizar nombre de Departamento")
        print("4. Eliminar Departamento")
        print("5. Volver al menú principal")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del departamento: ")
            nuevo_depto = Departamento(None, nombre)
            nuevo_depto.crearDepto()

        elif opcion == '2':
            lista = Departamento.mostrarDepto()
            if lista:
                print("\n--- DEPARTAMENTOS EN BD ---")
                for d in lista:
                    print(f"ID: {d.id} | Nombre: {d.nombre}")
            else:
                print("No hay departamentos registrados.")

        elif opcion == '3':
            try:
                id_modificar = int(input("Ingresa el ID a modificar: "))
                nuevo_nombre = input("Ingresa el nuevo nombre: ")
                depto_modificar = Departamento(id_modificar, "")
                depto_modificar.actualizarDpto(nuevo_nombre)
            except ValueError:
                print("Error: El ID debe ser numérico.")

        elif opcion == '4':
            try:
                id_eliminar = int(input("Ingresa el ID a eliminar: "))
                depto_eliminar = Departamento(id_eliminar, "")
                depto_eliminar.eliminarDpto()
            except ValueError:
                print("Error: El ID debe ser numérico.")

        elif opcion == '5':
            break
        else:
            print("Opción inválida.")


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def menu_principal():
    preparar_tablas()

    while True:
        print("\n" + "="*35)
        print(" SISTEMA DE GESTIÓN EMPRESARIAL")
        print("="*35)
        print("1. Módulo Usuarios")
        print("2. Módulo Empleados")
        print("3. Módulo Departamentos")
        print("4. Salir del Sistema")
        
        opcion = input("Seleccione el módulo al que desea ingresar: ")
        
        if opcion == '1':
            menu_usuario()
        elif opcion == '2':
            menu_empleado()
        elif opcion == '3':
            menu_departamento()
        elif opcion == '4':
            print("Apagando sistema... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# REPO GITHUB -> https://github.com/YerkoAranda1/EVA-2-Poo

if __name__ == "__main__":
    menu_principal()