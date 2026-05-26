class Estudiante:
    def __init__(self, matricula, nombre, apellido, carrera):
        self.__matricula = matricula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__cursos = []

    def getMatricula(self):
        return self.__matricula

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getCarrera(self):
        return self.__carrera

    def getCursos(self):
        return self.__cursos

    def agregarCurso(self, curso):
        self.__cursos.append(curso)

    def quitarCurso(self, curso):
        self.__cursos.remove(curso)

    def mostrarCursos(self):
        if len(self.__cursos) == 0:
            print(f"  {self.__nombre} {self.__apellido} no está inscripto en ningún curso")
        else:
            for curso in self.__cursos:
                print(f"  - {curso.getNombre()} | Código: {curso.getCodigo()}")