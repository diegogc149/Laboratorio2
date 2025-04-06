class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.total_prestamos = 0
    
    def agregar_libro(self, libro, cantidad):
        libro.biblioteca.append(self)
        libro.agregar_ejemplares(self, cantidad)
        self.catalogo.append(libro)
    
    def prestar_libro(self, libro, usuario):
        if libro.prestar(self, usuario): 
            self.total_prestamos += 1
        else:
            print(f"No quedan ejemplares del libro en la biblioteca {self.nombre}")

    def mostrar_catalogo(self):
        for libro in self.catalogo:
            print(libro.mostrar_info(self))
        
    def préstamos(self):
        return f"Libros totales prestados en {self.nombre}: {self.total_prestamos}"

class Autor:
    def __init__(self,nombre,nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad 
        self.libros = []
    
    def agregar_libros(self,libro):
        self.libros.append(libro)
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | Nacionalidad: {self.nacionalidad}")
        for libro in self.libros:
            print(libro.mostrar_info2())
            

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = 0
        self.ejemplares_pbiblio = {}
        self.biblioteca = []
    
    def agregar_ejemplares(self,biblioteca,cantidad):
        if biblioteca in self.ejemplares_pbiblio:
            self.ejemplares_pbiblio[biblioteca] += cantidad
        else:
            self.ejemplares_pbiblio[biblioteca] = cantidad

    def prestar(self,biblioteca,usuario):
        if biblioteca in self.ejemplares_pbiblio and self.ejemplares_pbiblio[biblioteca] > 0:
            self.ejemplares_pbiblio[biblioteca] -= 1
            print(f"Libro '{self.titulo}' prestado a {usuario} en {biblioteca.nombre}")
            return True
        return False
    
    def devolver(self,biblioteca):
        if biblioteca in self.ejemplares_pbiblio:
            self.ejemplares_pbiblio[biblioteca] += 1
            print(f"Libro '{self.titulo}' devuelto a {biblioteca.nombre}")
    
    def mostrar_info(self,biblioteca):
        cantidad = self.ejemplares_pbiblio.get(biblioteca, 0)
        return f"'{self.titulo}' por {self.autor} | {f'Disponibles: {cantidad}' if cantidad > 0 else 'No quedan ejemplares'} en {biblioteca.nombre}"

    def mostrar_info2(self):
        return f"{self.titulo} por {self.autor}"

biblio1 = Biblioteca("Biblioteca Central")
biblio2 = Biblioteca("Biblioteca Auxiliar")

libro1 = Libro("Cien años de soledad", "García Márquez")
libro2 = Libro("El Aleph", "Borges")

#Se agregan al catálogo
biblio1.agregar_libro(libro1,10)
biblio1.agregar_libro(libro2,5)
biblio2.agregar_libro(libro1,20)
#Muestro el catálogo
print("==========================================================")
biblio1.mostrar_catalogo()
biblio2.mostrar_catalogo()
print("==========================================================")
biblio1.prestar_libro(libro1,"Diego")  
biblio1.prestar_libro(libro2,"Diego")
biblio2.prestar_libro(libro1,"Diego")
biblio1.prestar_libro(libro1,"Diego")  
#Muestra los disponibles de la bilioteca
biblio1.mostrar_catalogo()
biblio2.mostrar_catalogo()
print("==========================================================")
print(biblio1.préstamos())
print("==========================================================")

autor1 = Autor("Gabriel García Márquez","colombiano")
autor1.agregar_libros(libro1)
autor1.mostrar_info()
