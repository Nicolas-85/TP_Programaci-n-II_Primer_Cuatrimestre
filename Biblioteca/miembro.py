from libro import Libro

class Miembro:
    def __init__(self, dni, nombre):
        self.__dni = dni
        self.__nombre = nombre
        self.__librosPrestados = []

    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def getLibrosPrestados(self):
        return self.__librosPrestados
    
    def agregarLibroPrestado(self, libro):
        self.__librosPrestados.append(libro)

    def quitarLibroPrestado(self, libro):
        self.__librosPrestados.remove(libro)

    def mostrarLibrosPrestados(self):
        if len(self.__librosPrestados)== 0:
            print(f"{self.__nombre} no tiene libros prestados")
        else:
            for libro in self.__librosPrestados:
                print(f" - {libro.getTitulo()} | ISBN: {libro.getIsbn()}")