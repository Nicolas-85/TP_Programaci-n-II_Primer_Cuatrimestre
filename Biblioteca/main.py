from biblioteca import Biblioteca
from libro import Libro
from miembro import Miembro
from excepciones import LibroNoEncontradoError, LibroNoDisponibleError, MiembroNoEncontradoError

biblioteca1 = Biblioteca()

def mostrarMenu():
    print('\n=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===')
    print('1 - Agregar libro')
    print('2 - Agregar miembro')
    print('3 - Mostrar libros')
    print('4 - Mostrar miembros')
    print('5 - Prestar libro')
    print('6 - Devolver libro')
    print('0 - Salir')

while True:
    mostrarMenu()
    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        try:
            titulo = input('Título: ')
            autor = input('Autor: ')
            isbn = input('ISBN: ')
            if not isbn.isdigit():
                raise ValueError("El ISBN debe ser numérico")
            libro = Libro(titulo, autor, int(isbn))
            biblioteca1.agregarLibro(libro)
            print(f"Libro '{titulo}' agregado con éxito")
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == '2':
        try:
            dni = input('DNI: ')
            nombre = input('Nombre: ')
            if not dni.isdigit():
                raise ValueError("El DNI debe ser numérico")
            miembro = Miembro(int(dni), nombre)
            biblioteca1.agregarMiembro(miembro)
            print(f"Miembro '{nombre}' agregado con éxito")
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == '3':
        biblioteca1.mostrarLibros()

    elif opcion == '4':
        biblioteca1.mostrarMiembros()

    elif opcion == '5':
        try:
            dni = input('DNI del miembro: ')
            isbn = input('ISBN del libro a prestar: ')
            biblioteca1.prestarLibro(int(isbn), int(dni))
        except LibroNoEncontradoError as e:
            print(f"Error: {e}")
        except MiembroNoEncontradoError as e:
            print(f"Error: {e}")
        except LibroNoDisponibleError as e:
            print(f"Error: {e}")

    elif opcion == '6':
        try:
            isbn = input('ISBN del libro a devolver: ')
            dni = input('DNI del miembro: ')
            biblioteca1.devolverLibroPrestado(int(isbn), int(dni))
        except LibroNoEncontradoError as e:
            print(f"Error: {e}")
        except MiembroNoEncontradoError as e:
            print(f"Error: {e}")
        except LibroNoDisponibleError as e:
            print(f"Error: {e}")

    elif opcion == '0':
        print('Saliendo...')
        break

    else:
        print('Opción inválida, intentá de nuevo')