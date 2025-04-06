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
            print("No quedan ejemplares del libro en esta biblioteca.")

    def mostrar_catalogo(self):
        for libro in self.catalogo:
            print(libro.mostrar_info(self)) 
        
    def prestamos_totales(self):
        return f"Libros totales prestados en {self.nombre}: {self.total_prestamos}"


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_por_biblioteca = {}  
        self.biblioteca = []
    
    def agregar_ejemplares(self, biblioteca, cantidad):
        if biblioteca in self.ejemplares_por_biblioteca:
            self.ejemplares_por_biblioteca[biblioteca] += cantidad
        else:
            self.ejemplares_por_biblioteca[biblioteca] = cantidad

    def prestar(self, biblioteca, usuario):
        if biblioteca in self.ejemplares_por_biblioteca and self.ejemplares_por_biblioteca[biblioteca] > 0:
            self.ejemplares_por_biblioteca[biblioteca] -= 1
            print(f"Libro '{self.titulo}' prestado a {usuario} en {biblioteca.nombre}")
            return True
        return False
    
    def devolver(self, biblioteca):
        if biblioteca in self.ejemplares_por_biblioteca:
            self.ejemplares_por_biblioteca[biblioteca] += 1
            print(f"Libro '{self.titulo}' devuelto en {biblioteca.nombre}")

    def mostrar_info(self, biblioteca):
        cantidad = self.ejemplares_por_biblioteca.get(biblioteca, 0)
        return f"'{self.titulo}' por {self.autor} | {f'Disponibles: {cantidad}' if cantidad > 0 else 'No quedan ejemplares'} en {biblioteca.nombre}"

# Prueba del sistema:
biblio1 = Biblioteca("Biblioteca Central")
biblio2 = Biblioteca("Biblioteca de Barrio")

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")

biblio1.agregar_libro(libro1, 2)
biblio2.agregar_libro(libro1, 3)

biblio1.mostrar_catalogo()
biblio2.mostrar_catalogo()

biblio1.prestar_libro(libro1, "Juan")
biblio1.mostrar_catalogo()
