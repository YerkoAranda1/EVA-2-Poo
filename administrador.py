from usuario import Usuario

class Administrador(Usuario):

    def __init__(self, id, nombre, email, password):
        super().__init__(id, nombre, email, password)

    def asignarEmpleadoDpto(self):
        pass

    def asignarEmpleadoProy(self):
        pass

    def generarInforme(self):
        print("Informe Generado")