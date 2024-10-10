# Programa: Prueba_Estante.py
# Objetivo: Interfaz del ejercicio 2
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-10-2024

import Repisa_Lista as Rl
import Repisa_Pila as Rp
import Clase_Libro as Cl
import csv


def leer_archivo(archivo: str) -> Rp.RepisaPila:
    """
    Metodo para leer un archivo y construir una repisa con dichos datos
    :param archivo: El nombre del archivo que se va a leer
    :return: Una Repisa con los datos leidos
    """
    repisa = None
    existe = False  # El archivo no existe
    while not existe:
        try:
            repisa = Rp.RepisaPila()  # Creamos una repisa vacia
            with open(archivo, encoding="UTF8", newline="") as file:
                lector = csv.reader(file)
                lector.__next__()  # Salta la primera linea
                for fila in lector:
                    repisa.push(Cl.Libro(fila[1],  # Titulo
                                         fila[2],  # Autor
                                         fila[2],  # Editorial
                                         int(fila[4])))  # Anio de publicacion
                existe = True
                print(f"El archivo {archivo} se leyo exitosamente!\n")
        except FileNotFoundError:
            print("El archivo no existe!\n")
            archivo = input("Escribe el nombre del archivo CSV: ")
    return repisa


def crear_libro() -> Cl.Libro:
    """
    Metodo para solicitar los datos y crear un libro.
    :return: Un objeto Libro
    """
    titulo = input("Escribe el titulo: ")
    autor = input("Escribe el autor: ")
    editorial = input("Escribe la editorial: ")
    a_publicacion = int(input("Escribe el anio de publicacion: "))
    # Creamos el libro
    libro = Cl.Libro(titulo, autor, editorial, a_publicacion)
    return libro


def menu_ordenar() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar para ordenar un objeto
    de la clase Estante
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Como deseas ordenar:\n'
                        '1. Por titulo\n'
                        '2. Por autor\n'
                        '3. Por editorial\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,3,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn

# Metodos comparadores entre libros. (titulo, autor, editorial)


def titulo(a: Cl.Libro, b: Cl.Libro) -> int:
    """
    Comparador que define como se distinguen 2 libros entre si,
    a partir de su titulo.
    :param a: Libro
    :param b: Libro
    :return: -1 si el titulo del libro a es alfabeticamente menor que
    el titulo de b, 1 en caso contrario y 0 si son titulos identicos.
    """
    if a.titulo < b.titulo:
        return -1
    elif a.titulo > b.titulo:
        return 1
    else:
        return 0


def autor(a: Cl.Libro, b: Cl.Libro) -> int:
    """
    Comparador que define como se distinguen 2 libros entre si,
    a partir de su autor.
    :param a: Libro
    :param b: Libro
    :return: -1 si el autor del libro a es alfabeticamente menor que
    el autor de b, 1 en caso contrario y 0 si son autores identicos.
    """
    if a.autor < b.autor:
        return -1
    elif a.autor > b.autor:
        return 1
    else:
        return 0


def editorial(a: Cl.Libro, b: Cl.Libro) -> int:
    """
    Comparador que define como se distinguen 2 libros entre si,
    a partir de su editorial.
    :param a: Libro
    :param b: Libro
    :return: -1 si la editorial del libro a es alfabeticamente menor que
    la editorial de b, 1 en caso contrario y 0 si son editoriales identicas.
    """
    if a.editorial < b.editorial:
        return -1
    elif a.editorial > b.editorial:
        return 1
    else:
        return 0

# Aqui comienza la interfaz HAY QUE CORREGIRLA PORQUE LA COPIE DE LA TAREA 3


while True:

    print("1. Crear mi estante de 3 repisas")
    print("2. Llenar mi repisa 1")
    print("3. Llenar mi repisa 2")
    print("4. Ordenar los libros en la tercera repisa")
    print("5. Eliminar un libro en la repisa 3")
    print("6. Agregar un libro en la repisa 1")
    print("7. Agregar un libro en la repisa 2")
    print("8. Agregar un libro en la repisa 3")
    print("9. Sacar un libro de la repisa 1")
    print("10. Sacar un libro de la repisa 2")
    print("11. Sacar un libro de la repisa 3")
    print("12. Mostrar repisa 1")
    print("13. Mostrar repisa 2")
    print("14. Mostrar repisa 3")
    print("15. Mostrar estante completo")
    print("16. Guardar en archivo Lista de libros ordenados")
    print("[S]alir")
    accion = input("¿Que deseas hacer?: ").upper()
    if accion not in "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,S" or len(accion) > 2:
        print("No se que deseas hacer!\n")
        continue
    match accion:
        case "1":  # Crear mi estante de 3 repisas
            try:
                print("1. Tamaño estandar")
                print("2. Definido por el usuario")
                opcion = input("Elige una opcion: ")
                if accion not in "1,2" or len(opcion) != 1:
                    print("No se que deseas hacer!\n")
                    continue
                match opcion:
                    case "1":  # Tamaño estandar
                        comparador = input("Especifica el tipo de comparador que utilizaras \n"
                                           "(apellido_nombre, edad, salario_nombre_edad, numero_empleado):")
                        a = Cs.Secuencia(comparador)
                    case "2":  # Definido por el usuario
                        size = int(input("Dame el tamaño del Conjunto: "))
                        comparador = input("Especifica el tipo de comparador que utilizaras \n"
                                           "(apellido_nombre, edad, salario_nombre_edad, numero_empleado):")
                        a = Cs.Secuencia(size, comparador)
            except ValueError:
                print("El comparador no es valido o el tamanio no es un entero positivo.")
                continue
        case "2":  # Agregar un elemento a la Secuencia
            try:
                if a is None:
                    print("Debes crear primero una Secuencia!\n")
                    continue
                else:
                    while True:  # Para agregar repetidamente elementos en la Secuencia
                        while True:  # Para validar que el numero de Empleado sea unico
                            num_emp = int(input("Escribe el id de empleado: "))
                            if num_emp not in id_emp1:
                                id_emp1.add(num_emp)
                                break
                            else:
                                print(f"El numero de empleado {num_emp} ya existe, se debe ingresar otro!\n")
                                continue
                        emp = crear_empleado(num_emp)
                        if emp is not None:
                            a.agregar(emp)
                            print("El elemento se agrego exitosamente!\n")
                        else:
                            print("El elemento no fue agregado!\n")
                        resp = input("Deseas seguir agregando elementos? (s/n): ").lower()
                        if resp == 'n':
                            break
            except ValueError:
                print("Has ingresado valores invalidos.")
                continue
        case "3":  # Agregar un elemento n veces a la Secuencia
            try:
                if a is None:
                    print("Debes crear primero una Secuencia!\n")
                    continue
                else:
                    while True:  # Para agregar repetidamente elementos en la Secuencia
                        while True:  # Para validar que el numero de Empleado sea unico
                            num_emp = int(input("Escribe el id de empleado: "))
                            n_veces = int(input("Escribe cuantas veces lo deseas agregar: "))
                            if num_emp not in id_emp1:
                                id_emp1.add(num_emp)
                                break
                            else:
                                print(f"El numero de empleado {num_emp} ya existe, se debe ingresar otro!\n")
                                continue
                        emp = crear_empleado(num_emp)
                        if emp is not None:
                            a.agregar(emp, n_veces)
                            print(f"El elemento se agrego exitosamente!\n")
                        else:
                            print("El elemento no fue agregado!\n")
                        resp = input("Deseas seguir agregando elementos? (s/n): ").lower()
                        if resp == 'n':
                            break
            except ValueError:
                print("Has ingresado valores invalidos.")
                continue
        case "4":  # Llenar nueva Secuencia desde archivo
            print("Este metodo permite crear una secuencia nueva adecuada al tamanio de datos del archivo que se \n"
                  "introduzca. No importa si ya se habia creado una secuencia anteriormente. El comparador \n"
                  "por default con el que se creara sera por edad.")
            archivo = input("Escribe el nombre del archivo CSV "
                            "(incluyendo la extension del tipo de archivo '.csv'): ")
            a = leer_archivo(archivo)
        case "5":  # Eliminar un elemento de la Secuencia
            try:
                if a is None:
                    print("Debes crear primero una Secuencia!\n")
                    continue
                else:
                    while True:
                        num_emp = int(input("Escribe el id de empleado: "))
                        if num_emp not in id_emp1:
                            print("Ese numero de empleado no existe en la secuencia.")
                            break
                        else:
                            emp = crear_empleado(num_emp)  # necesitas la informacion completa tal cual del empleado
                            if emp is not None:
                                a.eliminar(emp)
                                if not a.contiene(emp):
                                    id_emp1.remove(num_emp)
                                print("El elemento se elimino exitosamente!\n")
                            else:
                                print("El elemento no fue eliminado!\n")
                            resp = input("Deseas seguir eliminando elementos? (s/n): ").lower()
                            if resp == 'n':
                                break
            except ValueError:
                print("Has ingresado valores invalidos.")
                continue
        case "6":  # Eliminar un elemento n veces de la Secuencia
            try:
                if a is None:
                    print("Debes crear primero una Secuencia!\n")
                    continue
                else:
                    while True:
                        num_emp = int(input("Escribe el id de empleado: "))
                        if num_emp not in id_emp1:
                            print("Ese numero de empleado no existe en la secuencia.")
                            break
                        n_veces = int(input("Escribe el numero de veces que lo deseas eliminar: "))
                        emp = crear_empleado(num_emp)  # necesitas informacion completa tal cual del empleado
                        if emp is not None and a.contiene(emp):
                            a.eliminar(emp, n_veces)
                            id_emp1.remove(num_emp)
                            print(f"El elemento se elimino exitosamente!\n")
                        else:
                            print("El elemento no fue eliminado!\n")
                        resp = input("Deseas seguir eliminando elementos? (s/n): ").lower()
                        if resp == 'n':
                            break
            except ValueError:
                print("Has ingresado valores invalidos.")
                continue
        case "7":  # Determinar si una Secuencia contiene un elemento
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                while True:
                    num_emp = int(input("Escribe el id de empleado: "))
                    emp = crear_empleado(num_emp)
                    if emp is not None:
                        if a.contiene(emp):
                            print("El elemento esta contenido!\n")
                        else:
                            print("El elemento no esta contenido!\n")
                    else:
                        print("El elemento no pudo ser buscado!\n")
                    resp = input("Deseas seguir buscando elementos? (s/n): ").lower()
                    if resp == 'n':
                        break
        case "8":  # Determinar el numero de repeticiones de un elemento en la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                while True:
                    num_emp = int(input("Escribe el id de empleado: "))
                    emp = crear_empleado(num_emp)
                    if emp is not None:
                        cuenta = a.repeticiones(emp)
                        print(f"El elemento {emp} esta {cuenta} veces en la Secuencia!\n")
                    else:
                        print("El elemento no puede contabilizarse!\n")
                    resp = input("Deseas seguir buscando elementos? (s/n): ").lower()
                    if resp == 'n':
                        break
        case "9":  # Determinar la Secuencia esta vacia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                if a.esta_vacia():
                    print("La Secuencia esta vacia")
                    continue
                else:
                    print("La Secuencia no esta vacia")
                    continue
        case "10":  # Determinar la cardinalidad de la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                print(f"La cardinalidad de la secuencia es {a.cardinalidad()}")
                continue
        case "11":  # Vaciar la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                a.vaciar()
                print("La Secuencia ha sido vaciada exitosamente!\n")
                continue
        case "12":  # Devolver la Secuencia con elementos unicos
            if a is None:
                print("Debes crear primero una Secuencia!\n")
                continue
            else:
                sec_unico = a.secuencia_unico()
                print(sec_unico)
        case "13":  # 13. Ordenar la Secuencia
            opcion = menu_ordenar()
            while opcion != 'S':
                match opcion:
                    case "1":  # Apellido y nombre
                        a.comparador = apellido_nombre
                        ordenada = a.ordenar()
                        print(ordenada)
                        break
                    case "2":  # Edad
                        a.comparador = edad
                        ordenada = a.ordenar()
                        print(ordenada)
                        break
                    case "3":  # Salario, nombre y edad
                        a.comparador = salario_nombre_edad
                        ordenada = a.ordenar()
                        print(ordenada)
                        break
                    case "4":  # Numero de empleado
                        a.comparador = numero_empleado
                        ordenada = a.ordenar()
                        print(ordenada)
                        break
                    case "S":  # Salir
                        print('Regresando al menu principal')
            opcion = ""
        case "14":  # Mostrar la Secuencia
            if a is None:
                print("Debes crear primero una Secuencia!\n")
            else:
                print(a)
                print()
        case "15":  # Crear una segunda Secuencia desde archivo para poder utilizar __eq__
            print("Este metodo permite crear una segunda secuencia nueva adecuada al tamanio de datos del archivo \n "
                  "que se introduzca. No importa si ya se habia creado una secuencia anteriormente. El comparador \n"
                  "por default con el que se creara sera por edad")
            archivo = input("Escribe el nombre del archivo CSV "
                            "(incluyendo la extension del tipo de archivo '.csv'): ")
            b = leer_archivo(archivo)
        case "16":  # Determinar si dos secuencias son iguales
            if a is None:
                print("Debes crear primero una Secuencia!\n")
            elif b is None:
                print("Debes crear primero una segunda Secuencia!\n")
            else:
                respuesta = a == b  # es un bool
                if respuesta:
                    print(f"Las secuencias son iguales")
                else:
                    print("Las secuencias no son iguales")
        case "S":  # Salir
            print("Hasta luego! :D\n")
            break
