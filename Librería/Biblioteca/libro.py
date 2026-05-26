class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__estado = "Disponible"
        self.__miembro = None

    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getIsbn(self):
        return self.__isbn
    
    def getEstado(self):
        return self.__estado
    
    def getMiembro(self):
        return self.__miembro
    
    def setEstado(self, estado):
        self.__estado = estado
    
    def setMiembro(self, miembro):
        self.__miembro = miembro




