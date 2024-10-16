# Programa: Prueba_Estante.py
# Objetivo: Interfaz del ejercicio 2
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-10-2024

import Repisa_Lista as Rl
import Repisa_Pila as Rp
import Estante as Es
import Clase_Libro as Cl
import Comparadores_Libros as Cdl
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
                    repisa.push(Cl.Libro(fila[0],  # Titulo
                                         fila[1],  # Autor
                                         fila[2],  # Editorial
                                         int(fila[3])))  # Anio de publicacion
                existe = True
                print(f"El archivo {archivo} se leyo exitosamente!\n")
        except FileNotFoundError:
            print("El archivo no existe!\n")
            archivo = input("Escribe el nombre del archivo CSV: ")
        except OSError:
            print("No es una entrada valida\n")
            break
    return repisa

def escritura_csvs(l: Es.Estante):
    """
    Metodo que guarda la información de la tercer repisa (la ordenada)
    de un estante de libros ordenados en un archivo csv,
    para ello se utilizara los iteradores de la lista.
    """
    if isinstance(l, Es.Estante):
        nombre = 'Libros_Ordenados'
        f = open(nombre, 'w')
        encabezado = 'Titulo,Autor,Editorial,Anio\n'
        f.write(encabezado)
        for libro in l.repisa3:
            if libro is not None:
                cadena = ''
                for atributo in libro:
                    cadena += str(atributo) + ','
                cadena = cadena[:-1] + '\n'
                f.write(cadena)
        f.close()
        print(f'Se ha guardado la informacion en el archivo "{nombre}.csv"\n')
    else:
        raise TypeError("El argumento debe ser un objeto RespisaLista")

def crear_libro() -> Cl.Libro:
    """
    Metodo para solicitar los datos y crear un libro.
    :return: Un objeto Libro
    """
    while True:
        titulo = input("Escribe el titulo: ")
        autor = input("Escribe el autor: ")
        editorial = input("Escribe la editorial: ")
        a_publicacion = int(input("Escribe el anio de publicacion: "))
        # Creamos el libro
        libro = Cl.Libro(titulo, autor, editorial, a_publicacion)
        if isinstance(titulo, str) and isinstance(autor, str) and isinstance(editorial, str) and \
            isinstance(a_publicacion, int):
            return libro
        else:
            print("No son datos validos")


def menu_ordenar() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar para ordenar un objeto
    de la clase Estante
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input("Como deseas ordenar:\n"
                        "1. Por titulo\n"
                        "2. Por autor\n"
                        "3. Por editorial\n"
                        "S. Salir \n").upper()
        if opcionn not in "1,2,3,S" or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn

estante = None
# Aqui comienza la interfaz
while True:

    print("1. Crear mi estante de 3 repisas")
    print("2. Llenar mi repisa 1 desde un archivo CSV")
    print("3. Llenar mi repisa 2 desde un archivo CSV")
    print("4. Ordenar los libros en la tercer repisa (considera que si",
          "la tercer repisa tenia libros, estos se borrarán)")
    print("5. Agregar un libro en la repisa 1")
    print("6. Agregar un libro en la repisa 2")
    print("7. Vaciar repisa 1")
    print("8. Vaciar repisa 2")
    print("9. Vaciar repisa 3")
    print("10. Vaciar estante")
    print("11. Mostrar repisa 1")
    print("12. Mostrar repisa 2")
    print("13. Mostrar repisa 3")
    print("14. Mostrar estante completo")
    print("15. Guardar en archivo Lista de libros ordenados")
    print("[S]alir")
    accion = input("¿Que deseas hacer?: ").upper()
    if accion not in "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,S" or len(accion) > 2:
        print("No se que deseas hacer!\n")
        continue
    match accion:
        case "1":  # Crear mi estante de 3 repisas
            estante = Es.Estante()
            print("Se ha creado el estante")
        case "2":  # Llenar la repisa 1 del estante desde archivo
            if estante is None:
                print("Debes crear primero un Estante!\n")
                continue
            else:
                archivo = input("Escribe el nombre del archivo CSV "
                                "(incluyendo la extension del tipo de archivo '.csv'): ")
                estante.repisa1 = leer_archivo(archivo)
        case "3":  # Llenar la repisa 2 del estante desde archivo
            if estante is None:
                print("Debes crear primero un Estante!\n")
                continue
            else:
                archivo = input("Escribe el nombre del archivo CSV "
                                "(incluyendo la extension del tipo de archivo '.csv'): ")
                estante.repisa2 = leer_archivo(archivo)
        case "4":   # Ordenar los libros en la tercer repisa
            if estante is None:
                print("Deber crear primero un Estante")
            else:
                match menu_ordenar():
                    case "1":
                        estante.ordenar_en_repisa3(Cdl.titulo)
                        print("Se han ordenado por titulo los libros de la repisa 1 y 2 en la repisa 3")
                    case '2':
                        estante.ordenar_en_repisa3(Cdl.editorial)
                        print("Se han ordenado por editorial los libros de la repisa 1 y 2 en la repisa 3")
                    case '3':
                        estante.ordenar_en_repisa3(Cdl.autor)
                        print("Se han ordenado por autor los libros de la repisa 1 y 2 en la repisa 3")
        case "5":  # Agregar un libro a la repisa 1
            try:
                if estante is None:
                    print("Debes crear primero un Estante!\n")
                    continue
                else:
                    while True:  # Para agregar repetidamente elementos al estante
                        libro = crear_libro()
                        estante.repisa1.push(libro)
                        resp = input("Deseas seguir agregando elementos? (s/n): ").lower()
                        if resp == 'n':
                            break
            except ValueError:
                print("Has ingresado valores invalidos.\n")
                continue
        case "6":  # Agregar un libro a la repisa 2
            try:
                if estante is None:
                    print("Debes crear primero un Estante!\n")
                    continue
                else:
                    while True:  # Para agregar repetidamente elementos al estante
                        libro = crear_libro()
                        estante.repisa2.push(libro)
                        resp = input("Deseas seguir agregando elementos? (s/n): ").lower()
                        if resp == 'n':
                            break
            except ValueError:
                print("Has ingresado valores invalidos.\n")
                continue
        case "7":  # Vaciar la repisa 1
            if estante is None:
                print("Debes crear primero un Estante")
            else:
                estante.repisa1.vaciar()
                print("Se ha vaciado la repisa 1")
        case "8":  # Vaciar la repisa 2
            if estante is None:
                print("Debes crear primero un Estante")
            else:
                estante.repisa2.vaciar()
                print("Se ha vaciado la repisa 2")
        case "9": # Vaciar la repisa 3
            if estante is None:
                print("Debes crear primero un Estante")
            else:
                estante.repisa3.vaciar()
                print("Se ha vaciado la repisa 3")
        case "10": # Vaciar el estante
            if estante is None:
                print("Debes crear primero un Estante")
            else:
                estante = Es.Estante()
        case "11":  # Mostrar la repisa 1
            if estante is None:
                print("Debes crear primero el Estante!\n")
            else:
                print("Repisa 1: \n", estante.repisa1)
        case "12":  # Mostrar la repisa 2
            if estante is None:
                print("Debes crear primero el Estante!\n")
            else:
                print("Repisa 2: \n", estante.repisa2)
        case "13":  # Mostrar la repisa 3
            if estante is None:
                print("Debes crear primero el Estante!\n")
            else:
                print("Repisa 3: ", estante.repisa3)
        case "14":  # Mostrar el estante
            if estante is None:
                print("Debes crear primero el Estante!\n")
            else:
                print(estante)
        case "15": # Guardar en un archivo la lista de libros ordenados
            if estante is None:
                print("Debes crear primero el Estante!\n")
            else:
                escritura_csvs(estante)
        case "S":  # Salir
            print("Hasta luego! :D\n")
            break
