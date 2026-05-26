from estudiante import Estudiante
from curso import Curso
from excepciones import EstudianteNoEncontradoError, CursoNoEncontradoError, CursoSinCupoError, InscripcionNoEncontradaError

class Facultad:
    def __init__(self):
        self.__estudiantes = []
        self.__cursos = []

    def agregarEstudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    def agregarCurso(self, curso):
        self.__cursos.append(curso)

    def buscarEstudiante(self, matricula):
        for estudiante in self.__estudiantes:
            if estudiante.getMatricula() == matricula:
                return estudiante
        raise EstudianteNoEncontradoError(f"No existe un estudiante con matrícula: {matricula}")

    def buscarCurso(self, codigo):
        for curso in self.__cursos:
            if curso.getCodigo() == codigo:
                return curso
        raise CursoNoEncontradoError(f"No existe un curso con código: {codigo}")

    def inscribirEstudiante(self, codigo, matricula):
        curso = self.buscarCurso(codigo)
        estudiante = self.buscarEstudiante(matricula)
        if curso.getCuposDisponibles() == 0:
            raise CursoSinCupoError(f"El curso '{curso.getNombre()}' no tiene cupos disponibles")
        if estudiante in curso.getEstudiantesInscriptos():
            raise InscripcionNoEncontradaError(f"{estudiante.getNombre()} ya está inscripto en '{curso.getNombre()}'")
        curso.agregarEstudiante(estudiante)
        estudiante.agregarCurso(curso)
        print(f"{estudiante.getNombre()} {estudiante.getApellido()} inscripto en '{curso.getNombre()}' con éxito")

    def darDeBaja(self, codigo, matricula):
        curso = self.buscarCurso(codigo)
        estudiante = self.buscarEstudiante(matricula)
        if estudiante not in curso.getEstudiantesInscriptos():
            raise InscripcionNoEncontradaError(f"{estudiante.getNombre()} no está inscripto en '{curso.getNombre()}'")
        curso.quitarEstudiante(estudiante)
        estudiante.quitarCurso(curso)
        print(f"{estudiante.getNombre()} {estudiante.getApellido()} dado de baja de '{curso.getNombre()}' con éxito")

    def mostrarCursos(self):
        if len(self.__cursos) == 0:
            print("No hay cursos registrados")
        else:
            for curso in self.__cursos:
                print(f"Curso: {curso.getNombre()} | Código: {curso.getCodigo()} | Profesor: {curso.getProfesor()} | Inscriptos: {len(curso.getEstudiantesInscriptos())} | Cupos disponibles: {curso.getCuposDisponibles()}")
                curso.mostrarEstudiantes()

    def mostrarEstudiantes(self):
        if len(self.__estudiantes) == 0:
            print("No hay estudiantes registrados")
        else:
            for estudiante in self.__estudiantes:
                print(f"Nombre: {estudiante.getNombre()} {estudiante.getApellido()} | Matrícula: {estudiante.getMatricula()} | Carrera: {estudiante.getCarrera()}")
                estudiante.mostrarCursos()