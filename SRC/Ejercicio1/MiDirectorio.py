# Programa: MiDirectorio.py
# Autor: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Fecha: 17/10/2024
# Version: 2
# Descripcion: Programa que prueba el funcionamiento de la clase Directorio

import claseDirectorio as cDir
import Comparadores as Comp


def menu_principal() -> str:
    """
    Metodo auxiliar que muestra un menu con todas las operaciones implementadas en
    el directorio escolar
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Insertar datos de un nuevo contacto\n'
                       '2. Mostrar información de un contacto\n'
                       '3. Eliminar información de un contacto\n'
                       '4. Actualizar los datos de un contacto \n'
                       "5. Buscar contacto \n"
                       'S. Guardar y Salir \n').upper()
        if opcion not in '1,2,3,4,5,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


def menu_insertar_datos() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al insertar los datos de los contactos
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Agregar Alumno\n'
                       '2. Agregar Profesor\n'
                       '3. Agregar Coordinador\n'
                       'S. Salir \n').upper()
        if opcion not in '1,2,3,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


def menu_buscar() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al buscar los contactos
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Buscar por fecha de cumpleaños\n'
                       '2. Buscar por número de celular\n'
                       'S. Salir \n').upper()
        if opcion not in '1,2,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


def menu_actualizar():
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al actualizar
    un contacto
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Actualizar Alumno\n'
                       '2. Actualizar Profesor\n'
                       '3. Actualizar Coordinador\n'
                       'S. Salir \n').upper()
        if opcion not in '1,2,3,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


def menu_eliminar():
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al eliminar
    un contacto
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Borrar contacto a partir del nombre\n'
                       '2. Borrar contacto a partir del número de celular\n'
                       '3. Borrar contacto a partir del correo electrónico\n'
                       'S. Salir \n').upper()
        if opcion not in '1,2,3,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


def menu_mostrar_info():
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al mostrar información de los contactos
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Mostrar por nombre\n'
                       "2. Mostrar por nombre y rol\n"
                       "3. Mostrar por sueldo\n"
                       "4. Mostrar por correo electronico\n"
                       "5. Mostrar por carrera\n"
                       "6. Mostrar por alumnos o profesores\n"
                       'S. Salir \n').upper()
        if opcion not in '1,2,3,4,5,6,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


directorio = None


if __name__ == "__main__":
    print("Bienvenido al Programa donde se podra administrar los contactos de la escuela\n"
          "a travez de un directorio utilizando listas simplemente ligadas.")

    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Crear un Directorio vacio\n'
                        '2. Cargar contactos desde un archivo csv\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    match opcionn:
        case '1':  # crear directorio vacio
            while True:
                print("1. Edad ascendente")
                print("2. Salario descendente")
                print("3. Salario y nombre")
                print("4. Edad y nombre")
                print("5. Nombre")
                comp = input("Elige el comparador para la Lista Ordenada: ")
                if comp not in "12345" or len(comp) != 1:
                    print("El comparador elegido no es válido!\n")
                    continue
                match comp:
                    case "1":
                        directorio = cDir.Directorio(Comp.edad_ascendente)
                        break
                    case "2":
                        directorio = cDir.Directorio(Comp.salario_descendente)
                        break
                    case "3":
                        directorio = cDir.Directorio(Comp.salario_nombre)
                        break
                    case "4":
                        directorio = cDir.Directorio(Comp.edad_nombre)
                        break
                    case "5":
                        directorio = cDir.Directorio(Comp.nombre_ascendente)
                        break
            print(f'Ya se creo el directorio vacio')
            opcionn = ''
            while opcionn != 'S':
                opcionn = menu_principal()
                match opcionn:
                    case "1":  # '1. Insertar datos de un nuevo contacto\n'
                        while opcionn != 'S':
                            opcionn = menu_insertar_datos()
                            match opcionn:
                                case '1':  # '1. Agregar Alumno\n'
                                    directorio.insertar_nuevo_alumno()
                                case '2':  # '2. Agregar Profesor\n'
                                    directorio.insertar_nuevo_profesor()
                                case '3':  # '3. Agregar Coordinador\n'
                                    directorio.insertar_nuevo_coordinador()
                                case 'S':
                                    print('Regresando al menu principal')
                                    continue
                        opcionn = " "
                    case '2':  # '2. Mostrar información de un contacto\n'
                        while opcionn != 'S':
                            opcionn = menu_mostrar_info()
                            match opcionn:
                                case '1':
                                    nombre = input("Escribe el nombre del contacto que deseas buscar: ")
                                    directorio.mostrar_persona(nombre)
                                case '2':
                                    nombre = input("Escribe el nombre del contacto que deseas buscar: ")
                                    rol = input("Escribe el rol del contacto que deseas buscar: ")
                                    directorio.mostrar_informacion_contacto(nombre, rol)
                                case '3':
                                    sueldo = float(input("Escribe el sueldo del contacto que deseas buscar: "))
                                    directorio.mostrar_contactos_por_sueldo(sueldo)
                                case "4":
                                    email = input("Escribe el correo del contacto que deseas buscar: ")
                                    print(f"Se mostraran si hay, todos los contactos con email {email}: ")
                                    directorio.mostrar_contactos_con_email(email)
                                case '5':
                                    carrera = input("Escribe la carrera relacionada al contacto que deseas buscar: ")
                                    directorio.mostrar_contactos_por_carrera(carrera)
                                case '6':
                                    while True:
                                        try:
                                            eleccion = int(input("Escribe 0 si deseas ver a los alumnos "
                                                                 "o 1 si deseas ver a los profesores: "))
                                            directorio.mostrar_alumnos_o_profesores(eleccion)
                                            break
                                        except ValueError:
                                            print("La opcion debe ser 0 o 1.")
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '3':  # '3. Eliminar información de un contacto\n'
                        while opcionn != 'S':
                            opcionn = menu_eliminar()
                            match opcionn:
                                case '1':
                                    nombre = input("Escribe el nombre del contacto que deseas eliminar: ")
                                    directorio.eliminar_contacto(nombre)
                                case '2':
                                    while True:
                                        try:
                                            celular = int(input("Escribe el número de celular del "
                                                                "contacto que deseas eliminar: "))
                                            directorio.eliminar_cel(celular)
                                            break
                                        except ValueError:
                                            print("El celular debe ser un entero")
                                case '3':
                                    email = input("Escribe el correo electrónico del contacto que deseas eliminar: ")
                                    directorio.eliminar_email(email)
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '4':  # '4. Actualizar los datos de un contacto \n'
                        while opcionn != 'S':
                            opcionn = menu_actualizar()
                            match opcionn:
                                case '1':
                                    directorio.actualizar_alumno()
                                case '2':
                                    directorio.actualizar_profesor()
                                case '3':
                                    directorio.actualizar_coordinador()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '5':  # "5. Buscar contacto \n"
                        while opcionn != 'S':
                            opcionn = menu_buscar()
                            match opcionn:
                                case '1':
                                    while True:
                                        try:
                                            cum = input("Escribe el cumpleaños del contacto que deseas buscar "
                                                        "(dia/mes/anio): ")
                                            directorio.buscar_contacto_cum(cum)
                                            break
                                        except ValueError:
                                            print("Entrada invalida.")

                                case "2":
                                    while True:
                                        try:
                                            cel = int(input(
                                                "Escribe el número de celular del contacto que deseas buscar: "))
                                            directorio.buscar_contacto_celular(cel)
                                            break
                                        except ValueError:
                                            print("El celular debe ser un entero")
                        opcionn = ''
                    case 'S':  # 'S. Guardar y Salir \n').upper()
                        nombre = input('Escribe el nombre del archivo con terminación csv con el que deseas guardar: ')
                        directorio.escritura_csvs(nombre)
                        print(f'El directorio se guardo en el archivo csv "{nombre}"')
                        print("Hasta luego")
        case '2':   # Cargar informacion del directorio
            print('Leer un archivo csv creara un Directorio nuevo.')
            while True:
                print("1. Edad ascendente")
                print("2. Salario descendente")
                print("3. Salario y nombre")
                print("4. Edad y nombre")
                print("5. Nombre")
                comp = input("Elige el comparador para la Lista Ordenada: ")
                if comp not in "12345" or len(comp) != 1:
                    print("El comparador elegido no es válido!\n")
                    continue
                match comp:
                    case "1":
                        directorio = cDir.Directorio(Comp.edad_ascendente)
                        break
                    case "2":
                        directorio = cDir.Directorio(Comp.salario_descendente)
                        break
                    case "3":
                        directorio = cDir.Directorio(Comp.salario_nombre)
                        break
                    case "4":
                        directorio = cDir.Directorio(Comp.edad_nombre)
                        break
                    case "5":
                        directorio = cDir.Directorio(Comp.nombre_ascendente)
                        break
            while True:
                try:
                    nom = input('Escribe el nombre del archivo con terminación .csv que deseas abrir: ')
                    directorio.lectura_csvs(nom)
                    print(directorio)
                    break
                except FileNotFoundError:
                    pass
            opcionn = ''
            while opcionn != 'S':
                opcionn = menu_principal()
                match opcionn:
                    case "1":  # '1. Insertar datos de un nuevo contacto\n'
                        while opcionn != 'S':
                            opcionn = menu_insertar_datos()
                            match opcionn:
                                case '1':  # '1. Agregar Alumno\n'
                                    directorio.insertar_nuevo_alumno()
                                case '2':  # '2. Agregar Profesor\n'
                                    directorio.insertar_nuevo_profesor()
                                case '3':  # '3. Agregar Coordinador\n'
                                    directorio.insertar_nuevo_coordinador()
                                case 'S':
                                    print('Regresando al menu principal')
                                    continue
                        opcionn = " "
                    case '2':  # '2. Mostrar información de un contacto\n'
                        while opcionn != 'S':
                            opcionn = menu_mostrar_info()
                            match opcionn:
                                case '1':
                                    nombre = input("Escribe el nombre del contacto que deseas buscar: ")
                                    directorio.mostrar_persona(nombre)
                                case '2':
                                    nombre = input("Escribe el nombre del contacto que deseas buscar: ")
                                    rol = input("Escribe el rol del contacto que deseas buscar: ")
                                    directorio.mostrar_informacion_contacto(nombre, rol)
                                case '3':
                                    sueldo = float(input("Escribe el sueldo del contacto que deseas buscar: "))
                                    directorio.mostrar_contactos_por_sueldo(sueldo)
                                case "4":
                                    email = input("Escribe el correo del contacto que deseas buscar: ")
                                    print(f"Se mostraran si hay, todos los contactos con email {email}: ")
                                    directorio.mostrar_contactos_con_email(email)
                                case '5':
                                    carrera = input("Escribe la carrera relacionada al contacto que deseas buscar: ")
                                    directorio.mostrar_contactos_por_carrera(carrera)
                                case '6':
                                    while True:
                                        try:
                                            eleccion = int(input("Escribe 0 si deseas ver a los alumnos "
                                                                 "o 1 si deseas ver a los profesores: "))
                                            directorio.mostrar_alumnos_o_profesores(eleccion)
                                            break
                                        except ValueError:
                                            print("La opcion debe ser 0 o 1.")
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '3':  # '3. Eliminar información de un contacto\n'
                        while opcionn != 'S':
                            opcionn = menu_eliminar()
                            match opcionn:
                                case '1':
                                    nombre = input("Escribe el nombre del contacto que deseas eliminar: ")
                                    directorio.eliminar_contacto(nombre)
                                case '2':
                                    while True:
                                        try:
                                            celular = int(input("Escribe el número de celular del "
                                                                "contacto que deseas eliminar: "))
                                            directorio.eliminar_cel(celular)
                                            break
                                        except ValueError:
                                            print("El celular debe ser un entero")
                                case '3':
                                    email = input("Escribe el correo electrónico del contacto que deseas eliminar: ")
                                    directorio.eliminar_email(email)
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '4':  # '4. Actualizar los datos de un contacto \n'
                        while opcionn != 'S':
                            opcionn = menu_actualizar()
                            match opcionn:
                                case '1':
                                    directorio.actualizar_alumno()
                                case '2':
                                    directorio.actualizar_profesor()
                                case '3':
                                    directorio.actualizar_coordinador()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '5':  # "5. Buscar contacto \n"
                        while opcionn != 'S':
                            opcionn = menu_buscar()
                            match opcionn:
                                case '1':
                                    while True:
                                        try:
                                            cum = input("Escribe el cumpleaños del contacto que deseas buscar "
                                                        "(dia/mes/anio): ")
                                            directorio.buscar_contacto_cum(cum)
                                            break
                                        except ValueError:
                                            print("Entrada invalida.")

                                case "2":
                                    while True:
                                        try:
                                            cel = int(input(
                                                "Escribe el número de celular del contacto que deseas buscar: "))
                                            directorio.buscar_contacto_celular(cel)
                                            break
                                        except ValueError:
                                            print("El celular debe ser un entero")

                        opcionn = ''
                    case 'S':  # 'S. Guardar y Salir \n').upper()
                        directorio.escritura_csvs(nom)
                        print(f'El directorio se guardo en el archivo csv "{nom}"')
                        print("Hasta luego")
        case 'S':
            print('Hasta luego.')
