import uuid 
class Estudiante:
    def __init__(self,nombre,edad,ciclo):
        self.__nombre = nombre
        self.__edad = edad
        self.__matrícula = False
        self.__ciclo = ciclo
        self.__notas = []
        self.__código = str(uuid.uuid4())[:8]
    
    def activar_matrícula(self):
        self.__matrícula = True
        print(f"Matrícula de {self.__nombre},{self.__código}, activa")
    
    def desactivar_matrícula(self):
        self.__matrícula = False
        print(f"Matrícula de {self.__nombre},{self.__código}, desactivada")
    
    def verificar_matrícula(self):
        if not self.__matrícula:
            print(f"La matrícula de {self.__nombre}, {self.__código} está inactiva")
            return False
        return True
    
    def añadir_nota(self,nota):
        if 0<= nota <= 20 and self.verificar_matrícula() == True:
            self.__notas.append(nota)
        else:
            print("Ingrese una nota válida (Entre 0 y 20)")

    def promedio(self):
        return sum(self.__notas)/len(self.__notas)
    
    def mostrar_notas(self):
        print(f"Notas de {self.__nombre}: {self.__notas}")

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}, Matrícula: {self.__matrícula}, Ciclo:{self.__ciclo}, Código: {self.__código}")

estudiante1 = Estudiante("Diego",17,"Tercero")
estudiante1.mostrar_info()
estudiante1.añadir_nota(20)
estudiante1.activar_matrícula()
estudiante1.mostrar_info()
estudiante1.añadir_nota(20)
estudiante1.añadir_nota(19)
estudiante1.añadir_nota(21)
estudiante1.añadir_nota(18)
estudiante1.añadir_nota(1)
estudiante1.mostrar_notas()
print(f"Promedio:{estudiante1.promedio()}")
