import sqlite3
from departamento import Departamento

def preparar_tabla():
    """Crea la tabla Departamentos con ID AUTOINCREMENTAL"""
    conexion = sqlite3.connect("empresa.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

def menu_departamento():
    preparar_tabla()

    while True:
        print("\n--- PRUEBA CRUD DEPARTAMENTOS ---")
        print("1. Crear nuevo Departamento")
        print("2. Listar todos los Departamentos")
        print("3. Actualizar nombre de Departamento")
        print("4. Eliminar Departamento")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del departamento: ")
            
            # Instanciamos con None en el ID
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
                id_modificar = int(input("Ingresa el ID del departamento a modificar: "))
                nuevo_nombre = input("Ingresa el nuevo nombre: ")
                
                # Objeto temporal para el UPDATE
                depto_modificar = Departamento(id_modificar, "")
                depto_modificar.actualizarDpto(nuevo_nombre)
                
            except ValueError:
                print("❌ Error: El ID debe ser numérico.")

        elif opcion == '4':
            try:
                id_eliminar = int(input("Ingresa el ID del departamento a eliminar: "))
                
                # Objeto temporal para el DELETE
                depto_eliminar = Departamento(id_eliminar, "")
                depto_eliminar.eliminarDpto()
                
            except ValueError:
                print("❌ Error: El ID debe ser numérico.")

        elif opcion == '5':
            print("Cerrando prueba...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_departamento()