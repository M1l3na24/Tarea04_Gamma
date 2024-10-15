# Programa: claseDirectorio.py
# Objetivo: Programa que define la clase Directorio
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-09-2024

import numpy as np
import copy
import csv
import clasePersona as cP
import claseAlumno as cA
import claseProfesor as cPr
import claseCoordinador as cC
import Nodo as n


class Directorio:
    def __init__(self, tamanio=1):
        """
        Constructor que permite crear el objeto Directorio (escolar) que sera
        un arreglo que contendra arreglos(informacion de contacto).
        Se construye como un directorio nuevo: vacio por default
        :param: tamanio:int - es un parametro opcional que construye el directorio del
        tamanio 1 si no se especifica y de tamanio = tamanio si se especifica.
        """
        # Crear un directorio vacio
        self.__centinela = n.Nodo(None)  # Nodo centinela vacío
        self.__numeros_cuenta = set()
        self.__numeros_profesor = set()
        self.__numeros_empleado = set()
        # num_personas es un indice que me permite saber cual es el tamaño de mi directorio actual
        self.__num_personas = 0

    # Insertar datos de un nuevo contacto (alumno, profesor o coordinador).
    def insertar_nuevo_alumno(self):
        """
        Metodo para agregar un alumno en el arreglo de directorio, para ello
        se pedira cada uno de los campos. El numero de cuenta no debe de estar ya en el
        arreglo de numeros de cuenta de alumnos.
        """
        while True:
            try:
                num_cuenta = int(input('Escribe el numero de cuenta de alumno: '))
                if num_cuenta not in self.__numeros_cuenta:
                    self.__numeros_cuenta.add(num_cuenta)
                    break
                else:
                    print(f"El numero de cuenta {num_cuenta} ya existe, escribe otro")
                    continue
            except ValueError:
                print('El numero de cuenta del alumno, tiene que ser un entero')
        nombre = input('Escribe el nombre completo del alumno: ')
        # la fecha de cumpleanios debe ser dia/mes/anio
        cumpleanios = input('Escribe la fecha de cumpleanios del alumno (dia/mes/anio): ')
        correo = input('Escribe el correo del alumno: ')
        carrera = input('Escribe la carrera del alumno: ')
        materias = input('Escribe las materias del alumno separadas por comas: ')

        while True:
            try:
                celular = int(input('Escribe el celular del alumno: '))
                break
            except ValueError:
                print('El celular del alumno tiene que ser un entero')
        while True:
            try:
                semestre = int(input('Escribe el semestre del alumno: '))
                break
            except ValueError:
                print('El semestre del alumno, tiene que ser un entero')
        nuevo_alumno = cA.Alumno(nombre, celular, cumpleanios, correo, num_cuenta, carrera, materias.split(), semestre)
        self.__agregar_a_lista(nuevo_alumno)
        print('Alumno agregado\n')

    def insertar_nuevo_profesor(self):
        """
        Metodo para agregar un profesor en el arreglo de directorio, para ello
        se pedira cada uno de los campos. El numero de profesor no debe de estar ya en el
        arreglo de numero de profesores.
        """
        while True:
            try:
                num_profesor = int(input('Escribe el numero de Profesor: '))
                if num_profesor not in self.__numeros_profesor:
                    self.__numeros_cuenta.add(num_profesor)
                    break
                else:
                    print(f"El numero de profesor {num_profesor} ya existe, escribe otro")
                    continue
            except ValueError:
                print('El numero de profesor, tiene que ser un entero')
        nombre = input('Escribe el nombre completo del profesor: ')
        # la fecha de cumpleanios debe ser dia/mes/anio
        cumpleanios = input('Escribe la fecha de cumpleanios del profesor (dia/mes/anio): ')
        correo = input('Escribe el correo del profesor: ')
        dept = input('Escribe el departamento de adscripcion del profesor: ')
        carrera = input('Escribe la carrera en la que imparte materias el profesor: ')

        grupos = input('Escribe los grupos del profesor separados por comas: ')
        sueldo = float(input('Escribe el sueldo del profesor: '))

        while True:
            try:
                celular = int(input('Escribe el celular del profesor: '))
                break
            except ValueError:
                print('El celular del profesor tiene que ser un entero')
        while True:
            try:
                tel_oficina = int(input('Escribe el telefono de oficina del profesor: '))
                break
            except ValueError:
                print('El telefono de oficina del profesor, tiene que ser un entero')
        nuevo_profesor = cPr.Profesor(nombre, celular, cumpleanios, correo, num_profesor, tel_oficina, sueldo, dept,
                                      carrera, grupos.split(','))
        self.__agregar_a_lista(nuevo_profesor)
        print('Profesor agregado\n')

    def insertar_nuevo_coordinador(self):
        """
        Metodo para agregar un Coordinador en el arreglo de directorio, para ello
        se pedira cada uno de los campos. El numero de empleado no debe de estar ya en el
        arreglo de numero de empleados.
        """
        while True:
            try:
                num_empleado = int(input('Escribe el numero de Empleado: '))
                if num_empleado not in self.__numeros_empleado:
                    self.__numeros_cuenta.add(num_empleado)
                    break
                else:
                    print(f"El numero de empleado {num_empleado} ya existe, escribe otro")
                    continue
            except ValueError:
                print('El numero de empleado, tiene que ser un entero')
        nombre = input('Escribe el nombre completo del Coordinador: ')
        # la fecha de cumpleanios debe ser dia/mes/anio
        cumpleanios = input('Escribe la fecha de cumpleanios del Coordinador (dia/mes/anio): ')
        correo = input('Escribe el correo del Coordinador: ')
        dept = input('Escribe el departamento de adscripcion del Coordinador: ')
        carrera_coor = input('Escribe la carrera que coordina: ')
        sueldo = float(input('Escribe el sueldo del Coordinador: '))
        while True:
            try:
                celular = int(input('Escribe el celular del Coordinador: '))
                break
            except ValueError:
                print('El celular del Coordinador tiene que ser un entero')
        while True:
            try:
                tel_oficina = int(input('Escribe el telefono de oficina del Coordinador: '))
                break
            except ValueError:
                print('El telefono de oficina del Coordinador, tiene que ser un entero')
        nuevo_coordinador = cC.Coordinador(nombre, celular, cumpleanios, correo, num_empleado, tel_oficina, sueldo,
                                           dept, carrera_coor)
        self.__agregar_a_lista(nuevo_coordinador)
        print('Coordinador agregado\n')

    def __agregar_a_lista(self, persona):
        """
        Método privado para agregar una persona a la lista ligada.
        :param persona: objeto de tipo Alumno, Profesor o Coordinador.
        """
        nuevo_nodo = n.Nodo(persona)  # Crear un nuevo nodo con la persona
        actual = self.__centinela
        # Asegurarnos de que el nodo centinela está correctamente inicializado
        if actual is None:
            self.__centinela = nuevo_nodo
        else:
            # Recorrer hasta encontrar el último nodo
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

        self.__num_personas += 1

    def buscar_indice(self, nombre_completo) -> int:
        """
        Método auxiliar que busca una persona en la lista de directorio, dado el nombre completo.
        :param nombre_completo: El nombre completo a buscar en el directorio.
        :return: índice (basado en la posición relativa en la lista) si se encuentra, -1 si no.
        """
        actual = self.__centinela.siguiente
        indice = 0
        while actual is not None:
            if actual.dato.nombre_completo == nombre_completo:
                return indice
            actual = actual.siguiente
            indice += 1
        raise ValueError('No se encuentra en el directorio')

    def esta_vacio(self) -> bool:
        """
        Metodo que verifica si esta vacia la lista del directorio
        :return: True si no hay elementos en la lista, False si hay al menos uno.
        """
        return self.__num_personas == 0

    def mostrar_persona(self, nombre):
        """
        Metodo __str__ que define como mostrar una persona dentro del directorio.
        La representa a traves de los elementos en el array.
        :param nombre: persona a mostrar
        :return: cadena: Str - La representacion de la persona en el directorio
        :rtype: Str
        """
        if self.esta_vacio():
            print("No hay contactos.")
            return

        actual = self.__centinela.siguiente
        alumnos = ''
        profesores = ''
        coordinadores = ''

        while actual is not None:
            if actual.dato.nombre_completo == nombre:
                if isinstance(actual.dato, cA.Alumno):
                    alumnos += str(actual.dato) + '\n'
                elif isinstance(actual.dato, cPr.Profesor):
                    profesores += str(actual.dato) + '\n'
                elif isinstance(actual.dato, cC.Coordinador):
                    coordinadores += str(actual.dato) + '\n'
            actual = actual.siguiente

        if alumnos or profesores or coordinadores:
            print('\nALUMNOS:\n' + alumnos + "\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores)
        else:
            print(f"No se encontró a la persona con el nombre {nombre}.")

    # Extra: lectura/escritura de archivos CSV

    def tamanio_csv(self, archivo_csv):
        """
        Metodo extra necesario para saber de que tamanio sera el directorio
        :param: archivo_csv - nombre del archivo al que se le contara las lineas
        :return: n - numero lineas del csv
        """
        with open(archivo_csv, "r") as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',')
            n = sum(1 for _ in lector_csv)
        return n

    def lectura_csvs(self):
        """
        Metodo que carga/abre la informacion de un archivo en nuestro arreglo de directorio,
        dependiendo del tipo de persona, se utilizara el constructor correspodiente.
        """
        while True:
            nombre_archivo = input('Escribe el nombre del archivo con terminación csv, que deseas abrir: ')
            try:
                with open(nombre_archivo, 'r') as archivo:
                    lector_csv = csv.reader(archivo)
                    for linea in lector_csv:
                        if linea[0] == 'A':
                            nuevo_alumno = cA.Alumno(linea[1], int(linea[2]), linea[3], linea[4], int(linea[5]),
                                                     linea[6], linea[7].split(), int(linea[8]))
                            self.__agregar_a_lista(nuevo_alumno)
                            self.__numeros_cuenta.add(int(linea[5]))
                        elif linea[0] == 'P':
                            nuevo_profesor = cPr.Profesor(linea[1], int(linea[2]), linea[3], linea[4], int(linea[5]),
                                                          int(linea[6]), float(linea[7]), linea[8], linea[9],
                                                          linea[10].split())
                            self.__agregar_a_lista(nuevo_profesor)
                            self.__numeros_cuenta.add(int(linea[5]))
                        elif linea[0] == 'C':
                            nuevo_coordinador = cC.Coordinador(linea[1], int(linea[2]), linea[3], linea[4],
                                                               int(linea[5]), int(linea[6]), float(linea[7]), linea[8],
                                                               linea[9])
                            self.__agregar_a_lista(nuevo_coordinador)
                            self.__numeros_cuenta.add(int(linea[5]))
                print("Archivo cargado correctamente.")
                break
            except FileNotFoundError:
                print(f"El archivo {nombre_archivo} no existe")

    def escritura_csvs(self):
        """
        Metodo que guarda la información del arreglo de directorio, en un archivo csv
        para ello se utilizara los iteradores de cada tipo de persona
        """
        nombre_archivo = input('Escribe el nombre del archivo con terminación csv con el que deseas guardar: ')
        with open(nombre_archivo, 'w') as archivo:
            actual = self.__centinela.siguiente
            while actual is not None:
                persona = actual.dato
                per = ''
                for atributo in persona.__dict__.values():
                    per += str(atributo) + ','
                per = per[:-1] + '\n'  # Quitamos la última coma y añadimos un salto de línea
                archivo.write(per)
                actual = actual.siguiente
        print(f"Archivo {nombre_archivo} guardado correctamente.")

    # En esta clase el metodo de ordenamiento que utilizamos fue Quick Sort

    def __particion(self, inicio, fin, comparador) -> int:
        """
        Esta funcion organiza los elementos del directorio de manera que todos los elementos
        menores o iguales al pivote estan a la izquierda y todos los elementos mayores estan
        a la derecha. El pivote se coloca en su posicion correcta.
        :param inicio: La posición inicial
        :param fin: La posicion final
        :param comparador: El comparador con el que se desea hacer el ordenamiento
        :return: La posicion correcta del pivote
        :rtype: int
        """
        actual = self.__centinela.siguiente
        for _ in range(inicio):
            actual = actual.siguiente

        pivote = actual.dato
        left = inicio + 1
        right = fin
        while True:
            while left <= right:
                nodo_left = self.obtener_nodo(left)
                if comparador(nodo_left.dato, pivote) > 0:
                    break
                left += 1
            while comparador(self.obtener_nodo(right).dato, pivote) > 0 and right >= left:
                right -= 1
            if right < left:
                break
            else:
                # Intercambiamos los nodos izquierdo y derecho
                self.intercambiar_nodos(left, right)
        # Movemos el pivote a su posición correcta
        self.intercambiar_nodos(inicio, right)
        return right

    def obtener_nodo(self, posicion: int):
        """
        Método que obtiene el nodo en una posición específica de la lista simplemente ligada.
        :param posicion: La posición del nodo que se desea obtener (basada en índice 0).
        :return: El nodo encontrado en la posición indicada o None si no existe.
        """
        actual = self.__centinela.siguiente  # El primer nodo después del centinela
        indice_actual = 0

        # Recorremos la lista hasta llegar a la posición deseada o al final
        while actual is not None and indice_actual < posicion:
            actual = actual.siguiente
            indice_actual += 1

        # Si el nodo existe en la posición, lo retornamos
        if actual is not None and indice_actual == posicion:
            return actual
        else:
            return None  # Retornamos None si la posición no es válida

    def intercambiar_nodos(self, particion, nodo1, nodo2):
        """
        Método que intercambia dos nodos en una partición de la lista simplemente ligada.
        :param particion: La partición donde se encuentran los nodos.
        :param nodo1: Primer nodo a intercambiar.
        :param nodo2: Segundo nodo a intercambiar.
        """
        if nodo1 == nodo2:
            return  # Si los nodos son iguales, no hacemos nada

        # Buscamos los nodos predecesores de nodo1 y nodo2 en la partición
        anterior_nodo1, anterior_nodo2 = None, None
        actual = self.__particion[particion]  # Comenzamos en el centinela de la partición
        while actual.siguiente is not None:
            if actual.siguiente == nodo1:
                anterior_nodo1 = actual
            elif actual.siguiente == nodo2:
                anterior_nodo2 = actual
            actual = actual.siguiente

        if anterior_nodo1 is None or anterior_nodo2 is None:
            return  # Si alguno de los nodos no fue encontrado, no hacemos nada

        # Intercambiamos los nodos
        if anterior_nodo1.siguiente == nodo1 and anterior_nodo2.siguiente == nodo2:
            # Si los nodos son adyacentes, manejamos los enlaces de manera especial
            if nodo1.siguiente == nodo2:
                # Si nodo1 está justo antes de nodo2
                nodo1.siguiente = nodo2.siguiente
                nodo2.siguiente = nodo1
                anterior_nodo1.siguiente = nodo2
            else:
                # Si nodo2 está justo antes de nodo1
                nodo2.siguiente = nodo1.siguiente
                nodo1.siguiente = nodo2
                anterior_nodo2.siguiente = nodo1
        else:
            # Si los nodos no son adyacentes
            temp = nodo1.siguiente
            nodo1.siguiente = nodo2.siguiente
            nodo2.siguiente = temp
            anterior_nodo1.siguiente = nodo2
            anterior_nodo2.siguiente = nodo1

    # Quick sort
    def ordenar_directorio(self, inicio, fin, comparador):
        """
        Esta funcion aplica recursivamente el algoritmo Quick Sort a los subarreglos definidos por el pivote.
        :param inicio: La posicion inicial
        :param fin: La posicion final
        :param comparador: El comparador con el que se desea hacer el ordenamiento
        :return: Arreglo de contactos ordenado
        """
        if inicio < fin:
            posicion_part = self.__particion(inicio, fin, comparador)
            self.ordenar_directorio(inicio, posicion_part - 1, comparador)
            self.ordenar_directorio(posicion_part + 1, fin, comparador)

# Tipos de comparadores: Ordenar alfabeticamente
    def __compare_strings(self, str1: str, str2: str) -> int:
        """
        Metodo privado para comparar dos cadenas y devolver su relacion de orden en terminos de un int
        :param str1: Primera cadena a comparar
        :param str2: Segunda cadena a comparar
        :return: -1 si str1 lexicograficamente es menor que str2, 0 si son iguales, 1 en otro caso
        """
        if str1 < str2:
            return -1
        elif str1 > str2:
            return 1
        else:
            return 0

    def nombre_comparador(self, a: cP.Persona.nombre_completo, b: cP.Persona.nombre_completo):
        """
        Metodo para determinar la relacion de los Contactos con respecto al nombre.
        :param a: El nombre del primer Contacto a comparar
        :param b: El nombre del segundo Contacto a comparar
        :return: Valor positivo si el nombre de a es mayor que b, negativo si el nombre de
                 b es mayo que a. Si es el mismo nombre, regresa un 0.
        """
        dif_nombre = self.__compare_strings(a, b)
        return dif_nombre

    def mostrar_informacion_contacto(self, nombre, rol):
        """
        Muestra la informacion completa de un contacto, dado su nombre y rol.
        La informacion se muestra agrupada por categoria (alumno, profesor o coordinador).
        Los contactos se muestran ordenados.
        :param nombre:str -el nombre completo del contacto
        :param rol - tipo de objeto
        :return un string con la informacion completa del contacto con esas caracteristicas.
        """
        self.ordenar_directorio(0, self.__num_personas-1, self.nombre_comparador)
        # Determinar la clase de la persona según el rol
        if rol == 'alumno':
            rol_clase = cA.Alumno
        elif rol == 'profesor':
            rol_clase = cPr.Profesor
        elif rol == 'coordinador':
            rol_clase = cC.Coordinador
        else:
            print('No es una entrada válida')
            return

        # Buscar y mostrar el contacto
        actual = self.__centinela.siguiente
        encontrado = False
        while actual is not None:
            if actual.dato.nombre_completo == nombre and isinstance(actual.dato, rol_clase):
                print(actual.dato)
                encontrado = True
                break
            actual = actual.siguiente

        if not encontrado:
            print('No existe un contacto con esas características')

    def eliminar_contacto(self, nombre):
        """
        Elimina los datos de un contacto a partir del nombre.
        """
        self.ordenar_directorio(0, self.__num_personas-1, self.nombre_comparador)
        actual = self.__centinela.siguiente
        previo = self.__centinela  # El nodo previo al actual
        encontrado = False

        while actual is not None:
            if actual.dato.nombre_completo == nombre:  # Encontramos el contacto
                # Eliminamos el nodo al saltar la referencia
                previo.siguiente = actual.siguiente
                self.__num_personas -= 1  # Actualizamos el contador
                encontrado = True
                print(f"El contacto con el nombre: '{nombre}' ha sido eliminado.")
                break
            previo = actual
            actual = actual.siguiente

        if not encontrado:
            print(f"No se encontró contacto con el nombre completo: {nombre}")
    def menu_actualizar_alumno(self) -> str:
        """
        Metodo auxiliar, que muestra en pantalla las opciones para actualizar un Alumno
        :return: opcion: Int - La opcion deseada para actualizar
        :rtype: Str
        """
        while True:
            opcion = input('Que deseas actualizar:\n'
                           '1. Nombre Completo\n'
                           '2. Celular\n'
                           '3. Fecha Cumpleanios\n'
                           '4. Email\n'
                           '5. Num. Cuenta\n'
                           '6. Carrera \n'
                           '7. Materias\n'
                           '8. Semestre\n'
                           'S. Salir \n').upper()
            if opcion not in '1,2,3,4,5,6,7,8,S' or len(opcion) != 1:
                print("Opcion invalida.")
                continue
            else:
                break
        return opcion

    def menu_actualizar_profesor(self) -> str:
        """
        Metodo auxiliar, que muestra en pantalla las opciones para actualizar un Profesor
        :return: opcion: Int - La opcion deseada para actualizar
        :rtype: Str
        """
        while True:
            opcion = input('Que deseas actualizar:\n'
                           '1. Nombre Completo\n'
                           '2. Celular\n'
                           '3. Fecha Cumpleanios\n'
                           '4. Email\n'
                           '5. Num. Profesor\n'
                           '6. Tel. Oficina \n'
                           '7. Sueldo\n'
                           '8. Dept. Adscripcion\n'
                           '9. Carrera donde imparte materias\n'
                           '10. Grupos\n'
                           'S. Salir \n').upper()
            if opcion not in '1,2,3,4,5,6,7,8,9,10,S' or len(opcion) != 1:
                print("Opcion invalida.")
                continue
            else:
                break
        return opcion

    def menu_actualizar_coordinador(self) -> str:
        """
        Metodo auxiliar, que muestra en pantalla las opciones para actualizar un Profesor
        :return: opcion: Int - La opcion deseada para actualizar
        :rtype: Str
        """
        while True:
            opcion = input('Que deseas actualizar:\n'
                           '1. Nombre Completo\n'
                           '2. Celular\n'
                           '3. Fecha Cumpleanios\n'
                           '4. Email\n'
                           '5. Num. Empleado\n'
                           '6. Tel. Oficina \n'
                           '7. Sueldo\n'
                           '8. Dept. Adscripcion\n'
                           '9. Carrera que coordina\n'
                           'S. Salir \n').upper()
            if opcion not in '1,2,3,4,5,6,7,8,9,S' or len(opcion) != 1:
                print("Opcion invalida.")
                continue
            else:
                break
        return opcion

    def actualizar_alumno(self):
        """
        Metodo para actualizar un contacto del tipo allumno, si se encuentra el nombre completo del alumno
        desplegara un menu para saber que valor actualizar. Si no imprimira un mensaje.
        """
        nom_completo = input('Escribe el nombre completo del alumno: ')
        particion = 0  # Ajustar si los alumnos están en una partición específica
        indice = self.buscar_indice(nom_completo, particion)
        if indice == -1:
            print(f"No se encuentra el alumno con nombre completo {nom_completo}")
        else:
            alumno = self.obtener_nodo(particion, indice)
            if isinstance(alumno, cA.Alumno) and not isinstance(alumno, cPr.Profesor):
                print(alumno)
                opcion = ''
                while opcion != 'S':
                    opcion = self.menu_actualizar_alumno()

                    match opcion:
                        case "1":
                            nuevonombre = input('Escribe el nuevo nombre del Alumno a actualizar: ')
                            alumno._Persona__nombre_completo = nuevonombre
                            print('Nombre Actualizado \n')
                            opcion = ''

                        case "2":
                            nuevocelular = int(input('Escribe la nuevo celular del alumno: '))
                            alumno._Persona__celular = nuevocelular
                            print('Celular Actualizado \n')
                            opcion = ''

                        case "3":
                            nuevocumple = int(input('Escribe el nuevo cumpleanios del alumno: '))
                            alumno._Persona__fecha_cumpleanios = nuevocumple
                            print('Cumpleanios Actualizado \n')
                            opcion = ''

                        case "4":
                            nuevoemail = input('Escribe el nuevo email del alumno: ')
                            alumno._Persona__email = nuevoemail
                            print('Email Actualizado \n')
                            opcion = ''

                        case "5":
                            while True:
                                try:
                                    nuevonumcuenta = int(input('Escribe el nuevo numero de cuenta del alumno: '))
                                    break
                                except ValueError:
                                    print('El numero de cuenta del alumno, tiene que ser un entero')
                            self.__numeros_cuenta.remove(alumno.num_cuenta)
                            alumno.__num_cuenta = nuevonumcuenta
                            self.__numeros_cuenta.add(alumno.num_cuenta)
                            print('Numero de Cuenta Actualizado \n')
                            opcion = ''

                        case "6":
                            nueva_carrera = input('Escribe la nueva carrera del alumno: ')
                            alumno.__carrera = nueva_carrera
                            print('Carrera  Actualizada \n')
                            opcion = ''

                        case "7":
                            nuevamaterias = list(input('Escribe la nueva lista de materias del alumno: '))
                            alumno.__materias = nuevamaterias
                            print('Materias Actualizadas \n')
                            opcion = ''

                        case "8":
                            nuevsemestre = int(input('Escribe la nueva lista de materias del alumno: '))
                            alumno.__semestre = nuevsemestre
                            print('Materias Actualizadas \n')
                            opcion = ''

                        case "S":
                            print('Volviendo ...')
            else:
                print(f"No se encuentra el alumno con nombre {nom_completo}")

    def actualizar_profesor(self):
        """
        Metodo para actualizar un contacto del tipo Profesor, si se encuentra el nombre completo del profesor
        desplegara un menu para saber que valor actualizar. Si no imprimira un mensaje.
        """
        nomcompleto = input('Escribe el nombre completo del profesor: ')
        particion = 0  # Ajustar si los alumnos están en una partición específica
        indice = self.buscar_indice(nomcompleto, particion)
        if indice == -1:
            print(f"No se encuentra el profesor con nombre completo {nomcompleto}")
        else:
            profesor = self.obtener_nodo(particion, indice)
            if isinstance(profesor, cPr.Profesor) and not isinstance(profesor, cC.Coordinador):
                print(profesor)
                opcion = ''
                while opcion != 'S':
                    opcion = self.menu_actualizar_profesor()

                    match opcion:
                        case "1":
                            nuevonombre = input('Escribe el nuevo nombre del profesor a actualizar: ')
                            profesor._Persona__nombre_completo = nuevonombre
                            print('Nombre Actualizado \n')
                            opcion = ''

                        case "2":
                            nuevocelular = int(input('Escribe la nuevo celular del profesor: '))
                            profesor._Persona__celular = nuevocelular
                            print('Celular Actualizado \n')
                            opcion = ''

                        case "3":
                            nuevocumple = int(input('Escribe el nuevo cumpleanios del profesor: '))
                            profesor._Persona__fecha_cumpleanios = nuevocumple
                            print('Cumpleanios Actualizado \n')
                            opcion = ''

                        case "4":
                            nuevoemail = input('Escribe el nuevo email del profesor: ')
                            profesor._Persona__email = nuevoemail
                            print('Email Actualizado \n')
                            opcion = ''

                        case "5":
                            while True:
                                try:
                                    nuevonumprofesor = int(input('Escribe el nuevo numero de profesor: '))
                                    break
                                except ValueError:
                                    print('El numero de profesor del profesor, tiene que ser un entero')
                            self.__numeros_profesor.remove(profesor.num_profesor)
                            profesor.__num_profesor = nuevonumprofesor
                            self.__numeros_profesor.add(profesor.num_profesor)
                            print('Numero de Profesor Actualizado \n')
                            opcion = ''

                        case "6":
                            nuevoteloficina = int(input('Escribe el nuevo telefono de oficina del profesor: '))
                            profesor.__tel_oficina = nuevoteloficina
                            print('Tel. Oficina Actualizado \n')
                            opcion = ''

                        case "7":
                            nuevosueldo = int(input('Escribe el nuevo sueldo del profesor: '))
                            profesor.__sueldo = nuevosueldo
                            print('Sueldo Actualizado \n')
                            opcion = ''

                        case "8":
                            nuevodeptads = input('Escribe el nuevo Dept. de Ads. del profesor: ')
                            profesor.__dept_ads = nuevodeptads
                            print('Dept. de Ads. Actualizado \n')
                            opcion = ''

                        case "9":
                            nuevocarrera = input('Escribe la nueva carrera donde imparte materias el profesor: ')
                            profesor.__dept_ads = nuevocarrera
                            print('Carrera Actualizada \n')
                            opcion = ''

                        case '10':
                            nuevgrup = list(input('Escribe la nueva lista de grupos del profesor: '))
                            profesor.__grupos = nuevgrup
                            print('Materias Actualizadas \n')
                            opcion = ''

                        case "S":
                            print('Volviendo ...')
            else:
                print(f"No se encuentra el profesor con nombre {nomcompleto}")

    def actualizar_coordinador(self):
        """
        Metodo para actualizar un contacto del tipo Coordinador, si se encuentra el nombre completo del coordinador
        desplegara un menu para saber que valor actualizar. Si no imprimira un mensaje.
        """
        nomcompleto = input('Escribe el nombre completo del coordinador: ')
        particion = 0  # Ajustar si los alumnos están en una partición específica
        indice = self.buscar_indice(nomcompleto, particion)
        if indice == -1:
            print(f"No se encuentra el coordinador con nombre completo {nomcompleto}")
        else:
            coordinador = self.obtener_nodo(particion, indice)
            if isinstance(coordinador, cC.Coordinador) and not isinstance(coordinador, cPr.Profesor):
                print(coordinador)
                opcion = ''
                while opcion != 'S':
                    opcion = self.menu_actualizar_coordinador()

                    match opcion:
                        case "1":
                            nuevonombre = input('Escribe el nuevo nombre del coordinador a actualizar: ')
                            coordinador._Persona__nombre_completo = nuevonombre
                            print('Nombre Actualizado \n')
                            opcion = ''

                        case "2":
                            nuevocelular = int(input('Escribe la nuevo celular del coordinador: '))
                            coordinador._Persona__celular = nuevocelular
                            print('Celular Actualizado \n')
                            opcion = ''

                        case "3":
                            nuevocumple = int(input('Escribe el nuevo cumpleanios del coordinador: '))
                            coordinador._Persona__fecha_cumpleanios = nuevocumple
                            print('Cumpleanios Actualizado \n')
                            opcion = ''

                        case "4":
                            nuevoemail = input('Escribe el nuevo email del coordinador: ')
                            coordinador._Persona__email = nuevoemail
                            print('Email Actualizado \n')
                            opcion = ''

                        case "5":
                            while True:
                                try:
                                    nuevonumempleado = int(
                                        input('Escribe el nuevo numero de empleado del coordinador: '))
                                    break
                                except ValueError:
                                    print('El numero de empleado del coordinador, tiene que ser un entero')
                            self.__numeros_empleado.remove(coordinador.num_empleado)
                            coordinador.__num_empleado = nuevonumempleado
                            self.__numeros_empleado.add(coordinador.num_empleado)
                            print('Numero de Empleado Actualizado \n')
                            opcion = ''

                        case "6":
                            nuevoteloficina = int(input('Escribe el nuevo telefono de oficina del coordinador: '))
                            coordinador.__tel_oficina = nuevoteloficina
                            print('Tel. Oficina Actualizado \n')
                            opcion = ''

                        case "7":
                            nuevosueldo = int(input('Escribe el nuevo sueldo del coordinador: '))
                            coordinador.__sueldo = nuevosueldo
                            print('Sueldo Actualizado \n')
                            opcion = ''

                        case "8":
                            nuevodeptads = input('Escribe el nuevo Dept. de Ads. del coordinador: ')
                            coordinador.__dept_ads = nuevodeptads
                            print('Dept. de Ads. Actualizado \n')
                            opcion = ''

                        case "9":
                            nuevocarrera = input('Escribe la nueva carrera que coordina: ')
                            coordinador.__carrera_coordina = nuevocarrera
                            print('Carrera Actualizada \n')
                            opcion = ''

                        case "S":
                            print('Volviendo ...')
            else:
                print(f"No se encuentra el coordinador con nombre {nomcompleto}")

    def mostrar_contactos_por_sueldo(self, sueldo: float):
        """
        Muestra todos los contactos con un sueldo determinado.
        La información se muestra agrupada por categoría (profesor o coordinador).
        Los contactos se muestran ordenados.
        :param sueldo: int - el sueldo especifico que busco
        :return un string ordenado que divide profesores y coordinadores con ese sueldo especifico.
        """
        self.ordenar_directorio(0, self.__num_personas - 1, self.nombre_comparador)  # Ordenamos la lista
        actual = self.__centinela.siguiente
        profesores = ''
        coordinadores = ''

        while actual is not None:
            if isinstance(actual.dato, (cPr.Profesor, cC.Coordinador)):
                if actual.dato.sueldo == sueldo:
                    if isinstance(actual.dato, cPr.Profesor):
                        profesores += str(actual.dato) + '\n'
                    elif isinstance(actual.dato, cC.Coordinador):
                        coordinadores += str(actual.dato) + '\n'
            actual = actual.siguiente

        print("\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores)

    # Issac
    def contiene(self, contacto) -> bool:
        """
        Metodo que permite determinar si un contacto esta contenido en el Directorio
        :param contacto: El contacto a buscar
        :return: True si está contenido, False en caso contrario
        """
        actual = self.__centinela.siguiente
        while actual is not None:
            if actual.dato == contacto:  # Lo encontró
                return True
            actual = actual.siguiente
        return False  # No lo encontró

    def eliminar(self, contacto):
        """
        Este metodo permitira eliminar un contacto del directorio.
        :param contacto: El contacto que se va a eliminar
        """
        # Hay que asegurarnos que el arreglo no este vacío y el elemento exista
        self.ordenar_directorio(0, self.__num_personas-1, self.nombre_comparador)
        if not self.esta_vacio() and self.contiene(contacto):
            previo = self.__centinela
            actual = self.__centinela.siguiente

            while actual is not None:
                if actual.dato == contacto:
                    previo.siguiente = actual.siguiente  # Elimina el nodo
                    self.__num_personas -= 1
                    print(f"El contacto {contacto} fue eliminado!\n")
                    return
                previo = actual
                actual = actual.siguiente
            print(f"El elemento {contacto} no está en el Directorio!\n")
    def eliminar_cel(self, celular):
        """
        Elimina los datos de un contacto a partir del numero de celular.
        :param celular:int - El celular del contacto que se va a eliminar.
        """
        self.ordenar_directorio(0, self.__num_personas-1, self.nombre_comparador)
        actual = self.__centinela.siguiente
        while actual is not None:
            if actual.dato.celular == celular:
                self.eliminar(actual.dato)
                print(f"El contacto con el número de celular: '{celular}' ha sido eliminado.")
                return
            actual = actual.siguiente
        print(f"No se encontró contacto con el número de celular: {celular}")
    def eliminar_email(self, correo):
        """
        Elimina los datos de un contacto a partir del correo electronico.
        :param: correo:str - el correo de la persona que busco.
        """
        self.ordenar_directorio(0, self.__num_personas-1, self.nombre_comparador)
        actual = self.__centinela.siguiente
        while actual is not None:
            if actual.dato.email == correo:
                self.eliminar(actual.dato)
                print(f"El contacto con el correo electrónico: '{correo}' ha sido eliminado.")
                return
            actual = actual.siguiente
        print(f"No se encontró contacto con el correo: {correo}")

    def buscar_indice_cum(self, cumpleanios) -> int:
        """
        Método auxiliar que busca el índice del arreglo de directorio, dado la fecha de cumpleaños de una persona.
        :param cumpleanios: La fecha de cumpleaños a buscar en el directorio.
        :return: El índice (int) del arreglo del directorio si se encuentra un valor >= 0.
                 Si no se encuentra en el arreglo, retorna un valor < 0.
        :rtype: int
        """
        actual = self.__centinela.siguiente
        while actual is not None:
            if actual.dato.fecha_cumpleanios == cumpleanios:
                print(actual.dato)
                return
            actual = actual.siguiente
        print(f"No se encontró un contacto con cumpleaños {cumpleanios}")

    def buscar_indice_cel(self, celular) -> int:
        """
        Método auxiliar que busca el índice del arreglo de directorio, dado el número de celular de una persona.

        :param celular: El número de celular a buscar en el directorio.
        :return: El índice (int) del arreglo del directorio si se encuentra un valor >= 0.
                 Si no se encuentra en el arreglo, retorna un valor < 0.
        :rtype: int
        """
        actual = self.__centinela.siguiente
        while actual is not None:
            if actual.dato.celular == celular:
                print(actual.dato)
                return
            actual = actual.siguiente
        print(f"No se encontró un contacto con cumpleaños {celular}")

    def buscar_contacto_celular(self, celular: int):
        """
        Metodo __str__ que define como mostrar una persona dentro del directorio.
        La representa a traves de los elementos en el array.
        :param celular:int - numero de celular del contacto
        :return: cadena: Str - La representacion de la persona en el directorio
        :rtype: Str
        """
        self.ordenar_directorio(0, self.__num_personas-1, self.nombre_comparador)
        actual = self.__centinela.siguiente
        while actual is not None:
            if actual.dato.celular == celular:
                print(actual.dato)
                return
            actual = actual.siguiente
        print(f"No se encontró un contacto con celular {celular}")

    def buscar_contacto_cum(self, cumpleanios: str):
        """
        Metodo __str__ que define como mostrar una persona dentro del directorio a partir de su cumpleanios.
        La representa a traves de los elementos en el directorio.
        :param cumpleanios: cumpleanios del contacto
        :return: cadena: Str - La representacion de la persona en el directorio
        :rtype: Str
        """
        self.ordenar_directorio(0, self.__num_personas - 1, self.nombre_comparador)
        actual = self.__centinela.siguiente
        while actual is not None:
            if actual.dato.fecha_cumpleanios == cumpleanios:
                print(actual.dato)
                return
            actual = actual.siguiente
        print(f"No se encontró un contacto con celular {cumpleanios}")

    # Carlos

    def __str__(self) -> (str, str, str):
        """
        Metodo que permitira mostrar un contacto de la clase Directorio.
        :return: Una cadena de caracteres que incluiran la informacion de contacto.
        """
        cadena = ''
        self.ordenar_directorio(0, self.__num_personas-1, self.nombre_comparador)
        if not self.esta_vacio():
            alumnos = []
            profesores = []
            coordinadores = []
            for indice in range(self.__num_personas):  # Si __num_personas es la longitud de la lista
                nodo = self.obtener_nodo(0, indice)  # Obtener el nodo en la posición 'indice'
                if isinstance(nodo, cA.Alumno):
                    alumnos.append(nodo)
                elif isinstance(nodo, cPr.Profesor):
                    profesores.append(nodo)
                elif isinstance(nodo, cC.Coordinador):
                    coordinadores.append(nodo)
            if alumnos:
                cadena += '\nAlumnos: '
                for alumno in alumnos:
                    cadena += f'\n{str(alumno)}'
            else:
                cadena += '\n\nNo hay alumnos registrados'

            if profesores:
                cadena += '\n\nProfesores: '
                for profesor in profesores:
                    cadena += f'\n{str(profesor)}'
            else:
                cadena += '\n\nNo hay profesores registrados'

            if coordinadores:
                cadena += '\n\nCoordinadores: '
                for coordinador in coordinadores:
                    cadena += f'\n{str(coordinador)}'
            else:
                cadena += '\n\nNo hay coordinadores registrados'
            return cadena
        print('No hay contactos.')

    def mostrar_contactos_con_email(self):
        """
        Muestra los contactos por categoria y ordenados
        Obs: por como fue definido la clase Persona, los objetos persona
        tienen un email valido.
        """
        self.ordenar_directorio(0, self.__num_personas-1, self.nombre_comparador)
        if not self.esta_vacio():
            copia = copy.deepcopy(self)
            copia.eliminar_email(None)
            copia.eliminar_email('')
            print(copia)
            return
        print('El directorio aun no tiene contactos.')

    def mostrar_contactos_por_carrera(self, carrera_particular: str):
        """
        Muestra todos los contactos con una carrera particular.
        La información se muestra agrupada por categoría (alumno, profesor o coordinador).
        Los contactos se muestran ordenados.
        :param carrera_particular: str -la carrera especifica que busco
        :return un string ordenado que divide alumnos, profesores y coordinadores con esa carrera especifica.
        """
        actual = self.__centinela.siguiente
        alumnos = ''
        profesores = ''
        coordinadores = ''

        while actual is not None:
            if isinstance(actual.dato, cA.Alumno) and actual.dato.carrera == carrera_particular:
                alumnos += str(actual.dato) + '\n'
            elif isinstance(actual.dato, cPr.Profesor) and actual.dato.carrera == carrera_particular:
                profesores += str(actual.dato) + '\n'
            elif isinstance(actual.dato, cC.Coordinador) and actual.dato.carrera_coordina == carrera_particular:
                coordinadores += str(actual.dato) + '\n'
            actual = actual.siguiente

        print("\nALUMNOS:\n" + alumnos + "\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores)

    def mostrar_alumnos_o_profesores(self, eleccion):
        """
        Muestra solo los alumnos o solo los maestros en orden
        Esto segun la eleccion del usuario
        :param eleccion: 0 si alumnos, 1 si maestros
        """
        self.ordenar_directorio(0, self.__num_personas - 1, self.nombre_comparador)
        actual = self.__centinela.siguiente
        if eleccion == 0:
            alumnos = ''
            while actual is not None:
                if isinstance(actual.dato, cA.Alumno):
                    alumnos += str(actual.dato) + '\n'
                actual = actual.siguiente
            print('Alumnos registrados:\n' + alumnos if alumnos else 'No hay alumnos registrados\n')

        elif eleccion == 1:
            profesores = ''
            actual = self.__centinela.siguiente
            while actual is not None:
                if isinstance(actual.dato, cPr.Profesor):
                    profesores += str(actual.dato) + '\n'
                actual = actual.siguiente
            print('Profesores registrados:\n' + profesores if profesores else 'No hay profesores registrados\n')

        else:
            print('No es una entrada válida')



