from libro import Libro
from miembro import Miembro
from excepciones import LibroNoEncontradoError, LibroNoDisponibleError, MiembroNoEncontradoError 


class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__miembros = []

    def agregarLibro(self, libro):
        self.__libros.append(libro)
    
    def agregarMiembro(self, miembro):
        self.__miembros.append(miembro)

    def buscarLibro(self, isbn):
        for libro in self.__libros:
            if libro.getIsbn() == isbn:
                return libro
        raise LibroNoEncontradoError(f"No existe un libro con ISBN: {isbn}")

    def buscarMiembro(self, dni):
        for miembro in self.__miembros:
            if miembro.getDni() == dni:
                return miembro
        raise MiembroNoEncontradoError(f"No existe un miembro con DNI {dni}")
    
    def mostrarLibros(self):
        if len(self.__libros) == 0:
            print("No hay libros registrados")
        else:
            for libro in self.__libros:
                if libro.getEstado() == 'Disponible':
                    print(f"Título: {libro.getTitulo()} | Autor: {libro.getAutor()} | ISBN: {libro.getIsbn()} | Estado: {libro.getEstado()}")
                else: 
                    print(f"Título: {libro.getTitulo()} | Autor: {libro.getAutor()} | ISBN: {libro.getIsbn()} | Estado: {libro.getEstado()} |Prestado a: {libro.getMiembro().getNombre()}")

    def mostrarMiembros(self):
        if len(self.__miembros) == 0:
            print("No existen miembros registrados")
        else:
            for miembro in self.__miembros:
                print(f"Nombre: {miembro.getNombre()} | Dni: {miembro.getDni()}")
                miembro.mostrarLibrosPrestados()

    def prestarLibro(self, isbn, dni):
        libro = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)
        if libro.getEstado() == 'Prestado':
            raise LibroNoEncontradoError(f"Libro: {libro.getTitulo()}, se encuentra prestado a: {libro.getMiembro().getNombre()}")
        libro.setEstado('Prestado')
        libro.setMiembro(miembro)
        miembro.agregarLibroPrestado(libro)        
        print(f"El libro: {libro.getTitulo()}, fue prestado a: {miembro.getNombre()}, con éxito.")
            
    def devolverLibroPrestado(self, isbn, dni):
        libro = self.buscarLibro(isbn)
        miembro = self.buscarMiembro(dni)
        if libro.getEstado() == "Disponible":
            raise LibroNoDisponibleError(f"Libro: {libro.getTitulo()} no está prestado actualmente")
        libro.setEstado("Disponible")
        libro.setMiembro(None)
        miembro.quitarLibroPrestado(libro)
        print(f"Libro '{libro.getTitulo()}' devuelto con éxito")

    