# Programa: MiDirectorio.py
# Autor: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Fecha: 09/09/2024
# Version: 1
# Descripcion: Programa que prueba el funcionamiento de la clase Directorio

import claseDirectorio as cDir


def menu_principal() -> str:
    """
    Metodo auxiliar que muestra un menu con todas las operaciones implementadas en
    el directorio escolar
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Insertar datos de un nuevo contacto\n'
                        '2. Mostrar información de un contacto\n'
                        '3. Eliminar información de un contacto\n'
                        '4. Actualizar los datos de un contacto \n'
                        "5. Buscar contacto \n"
                        'S. Guardar y Salir \n').upper()
        if opcionn not in '1,2,3,4,5,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn


def menu_insertar_datos() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al insertar los datos de los contactos
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Agregar Alumno\n'
                        '2. Agregar Profesor\n'
                        '3. Agregar Coordinador\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,3,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn

def menu_buscar() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al buscar los contactos
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Buscar por fecha de cumpleaños\n'
                        '2. Buscar por número de celular\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn


def menu_actualizar():
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al actualizar
    un contacto
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Actualizar Alumno\n'
                        '2. Actualizar Profesor\n'
                        '3. Actualizar Coordinador\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,3,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn


def menu_eliminar():
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al eliminar
    un contacto
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Borrar contacto a partir del nombre\n'
                        '2. Borrar contacto a partir del número de celular\n'
                        '3. Borrar contacto a partir del correo electrónico\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,3,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn


def menu_mostrar_info():
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al mostrar información de los contactos
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Mostrar por nombre\n'
                        "2. Mostrar por nombre y rol\n"
                        "3. Mostrar por sueldo\n"
                        "4. Mostrar por correo electronico\n"
                        "5. Mostrar por carrera\n"
                        "6. Mostrar por alumnos o profesores\n"
                        'S. Salir \n').upper()
        if opcionn not in '1,2,3,4,5,6,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn


if __name__ == "__main__":
    print("Bienvenido al Directorio, donde se podra administrar los contactos de la escuela")
    directorio = cDir.Directorio()
    print(f'Ya se creo el directorio vacio')

    while True:
        opcionn = input('Que deseas hacer:\n'
                       '1. Cargar información del directorio\n'
                       '2. Crear información nueva del directorio\n'
                       'S. Salir \n').upper()
        if opcionn not in '1,2,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    match opcionn:
        case '1':
            print('Leer un archivo csv creara un directorio nuevo con la capacidad necesaria que dependera del csv.')
            directorio.lectura_csvs()
            print(directorio)
            opcionn = ''
            while opcionn != 'S':
                opcionn = menu_principal()
                match opcionn:
                    case "1":
                        while opcionn != 'S':
                            opcionn = menu_insertar_datos()
                            match opcionn:
                                case '1':
                                    directorio.insertar_nuevo_alumno()
                                case '2':
                                    directorio.insertar_nuevo_profesor()
                                case '3':
                                    directorio.insertar_nuevo_coordinador()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = " "
                    case '2':
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
                                    print("Se mostraran si hay, todos los contactos con email: ")
                                    directorio.mostrar_contactos_con_email()
                                case '5':
                                    carrera = input("Escribe la carrera relacionada al contacto que deseas buscar: ")
                                    directorio.mostrar_contactos_por_carrera(carrera)
                                case '6':
                                    eleccion = int(input("Escribe 0 si deseas ver a los alumnos "
                                                         "o 1 si deseas ver a los profesores: "))
                                    directorio.mostrar_alumnos_o_profesores(eleccion)
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '3':
                        while opcionn != 'S':
                            opcionn = menu_eliminar()
                            match opcionn:
                                case '1':
                                    nombre = input("Escribe el nombre del contacto que deseas eliminar: ")
                                    directorio.eliminar_contacto(nombre)
                                case '2':
                                    celular = int(input("Escribe el número de celular del "
                                                        "contacto que deseas eliminar: "))
                                    directorio.eliminar_cel(celular)
                                case '3':
                                    email = input("Escribe el correo electrónico del contacto que deseas eliminar: ")
                                    directorio.eliminar_email(email)
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '4':
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
                    case '5':
                      while opcionn != 'S':
                          opcionn = menu_buscar()
                          match opcionn:
                              case '1':
                                  cum = input("Escribe el cumpleaños del contacto que deseas buscar: ")
                                  directorio.buscar_contacto_cum(cum)
                              case "2":
                                  cel = int(input("Escribe el número de celular del contacto que deseas buscar: "))
                                  directorio.buscar_contacto_celular(cel)
                      opcionn = ''
                    case 'S':
                        # dir.guardar_Archivo() no tenemos este metodo
                        print("Hasta luego")
        case '2':
            opcionn = ''
            while opcionn != 'S':
                opcionn = menu_principal()
                match opcionn:
                    case "1":
                        while opcionn != 'S':
                            opcionn = menu_insertar_datos()
                            match opcionn:
                                case '1':
                                    directorio.insertar_nuevo_alumno()
                                case '2':
                                    directorio.insertar_nuevo_profesor()
                                case '3':
                                    directorio.insertar_nuevo_coordinador()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = " "
                    case '2':
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
                                    print("Se mostraran si hay, todos los contactos con email: ")
                                    directorio.mostrar_contactos_con_email()
                                case '5':
                                    carrera = input("Escribe la carrera relacionada al contacto que deseas buscar: ")
                                    directorio.mostrar_contactos_por_carrera(carrera)
                                case '6':
                                    eleccion = int(input("Escribe 0 si deseas ver a los alumnos "
                                                         "o 1 si deseas ver a los profesores: "))
                                    directorio.mostrar_alumnos_o_profesores(eleccion)
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '3':
                        while opcionn != 'S':
                            opcionn = menu_eliminar()
                            match opcionn:
                                case '1':
                                    nombre = input("Escribe el nombre del contacto que deseas eliminar: ")
                                    directorio.eliminar_contacto(nombre)
                                case '2':
                                    celular = int(input("Escribe el número de celular del "
                                                        "contacto que deseas eliminar: "))
                                    directorio.eliminar_cel(celular)
                                case '3':
                                    email = input("Escribe el correo electrónico del contacto que deseas eliminar: ")
                                    directorio.eliminar_email(email)
                                case 'S':
                                    print('Regresando al menu principal')
                        opcionn = ''
                    case '4':
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
                    case '5':
                      while opcionn != 'S':
                          opcionn = menu_buscar()
                          match opcionn:
                              case '1':
                                  cum = input("Escribe el cumpleaños del contacto que deseas buscar: ")
                                  directorio.buscar_contacto_cum(cum)
                              case "2":
                                  cel = int(input("Escribe el número de celular del contacto que deseas buscar: "))
                                  directorio.buscar_contacto_celular(cel)
                      opcionn = ''
                    case 'S':
                        # dir.guardar_Archivo() no tenemos este metodo
                        print("Hasta luego")
        case 'S':
            print('Hasta luego')