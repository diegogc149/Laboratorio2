from abc import ABC, abstractmethod

class Coche:

    def __init__(self , marca , modelo , año ):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__encendido = False

    def arrancar(self):
        self.__encendido = True
        print(f"El coche {self.__marca} { self.__modelo} inició su movimiento")
    
    def detener(self):
        self.__encendido = False
        print(f"El coche {self.__marca} {self.__modelo} se ha detenido")
        
    def mover_izquierda(self):
        if self.__encendido == True:
            print(f"El coche {self.__marca} {self.__modelo} ha cambiado de dirección a la izquierda.")
        else:
            print(f"El coche {self.__marca} { self.__modelo} no está encendido.")

    def mover_derecha(self):
        if self.__encendido == True:
            print(f"El coche {self.__marca} {self.__modelo} ha cambiado de dirección a la derecha")
        else:
            print(f"El coche {self.__marca} {self.__modelo} no está encendido")

    def mostrar_información(self):
        print(f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}")

coche1 = Coche("Toyota","Hilux",2025)
coche2 = Coche("Chevrolet","Onix LTZ",2015)


coche1.mover_derecha()
coche2.mover_izquierda()
coche2.arrancar()
coche1.arrancar()
coche1.mover_izquierda()
coche2.mover_derecha()
coche1.detener()
coche2.detener()
coche2.mostrar_información()


