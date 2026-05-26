from facultad import Facultad
from estudiante import Estudiante
from curso import Curso
from excepciones import EstudianteNoEncontradoError, CursoNoEncontradoError, CursoSinCupoError, InscripcionNoEncontradaError

facultad1 = Facultad()

def mostrarMenu():
    print('\n=== SISTEMA DE GESTIÓN DE FACULTAD ===')
    print('1 - Agregar estudiante')
    print('2 - Agregar curso')
    print('3 - Mostrar estudiantes')
    print('4 - Mostrar cursos')
    print('5 - Inscribir estudiante a curso')
    print('6 - Dar de baja estudiante de curso')
    print('0 - Salir')

while True:
    mostrarMenu()
    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        try:
            matricula = input('Matrícula: ')
            if not matricula.isdigit():
                raise ValueError("La matrícula debe ser numérica")
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            carrera = input('Carrera: ')
            estudiante = Estudiante(int(matricula), nombre, apellido, carrera)
            facultad1.agregarEstudiante(estudiante)
            print(f"Estudiante '{nombre} {apellido}' agregado con éxito")
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == '2':
        try:
            nombre = input('Nombre del curso: ')
            codigo = input('Código del curso: ')
            if not codigo.isdigit():
                raise ValueError("El código debe ser numérico")
            profesor = input('Profesor: ')
            capacidad = input('Capacidad máxima: ')
            if not capacidad.isdigit():
                raise ValueError("La capacidad debe ser numérica")
            curso = Curso(nombre, int(codigo), profesor, int(capacidad))
            facultad1.agregarCurso(curso)
            print(f"Curso '{nombre}' agregado con éxito")
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == '3':
        facultad1.mostrarEstudiantes()

    elif opcion == '4':
        facultad1.mostrarCursos()

    elif opcion == '5':
        try:
            matricula = input('Matrícula del estudiante: ')
            codigo = input('Código del curso: ')
            facultad1.inscribirEstudiante(int(codigo), int(matricula))
        except EstudianteNoEncontradoError as e:
            print(f"Error: {e}")
        except CursoNoEncontradoError as e:
            print(f"Error: {e}")
        except CursoSinCupoError as e:
            print(f"Error: {e}")
        except InscripcionNoEncontradaError as e:
            print(f"Error: {e}")

    elif opcion == '6':
        try:
            matricula = input('Matrícula del estudiante: ')
            codigo = input('Código del curso: ')
            facultad1.darDeBaja(int(codigo), int(matricula))
        except EstudianteNoEncontradoError as e:
            print(f"Error: {e}")
        except CursoNoEncontradoError as e:
            print(f"Error: {e}")
        except InscripcionNoEncontradaError as e:
            print(f"Error: {e}")

    elif opcion == '0':
        print('Saliendo...')
        break

    else:
        print('Opción inválida, intentá de nuevo')