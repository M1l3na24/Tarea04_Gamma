# Programa: claseDirectorio.py
# Objetivo: Programa que define la clase Directorio
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 16-10-2024


import csv
import Lista as Li
import claseAlumno as cA
import claseProfesor as cPr
import claseCoordinador as cC
import Comparadores as Comp


def menu_actualizar_coordinador() -> str:
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


def menu_actualizar_profesor() -> str:
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


def menu_actualizar_alumno() -> str:
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


class Directorio:
    def __init__(self, comparador: callable):
        """
        Constructor que permite crear el objeto Directorio (escolar) que será
        un directorio que contendrá contactos (alumnos, profesores, coordinadores)
        utilizando listas simplemente ligadas.
        Se construye como un directorio nuevo: vacío por default.
        """
        # Crear una lista vacía con el comparador definido
        self.__lista = Li.Lista(comparador)
        self.__numeros_cuenta = set()
        self.__numeros_profesor = set()
        self.__numeros_empleado = set()
        self.__num_personas = 0

    def __agregar_a_lista(self, persona):
        """
        Método privado que agrega una nueva persona (Alumno, Profesor, etc.) a la lista de contactos.
        """
        self.__lista.agregar(persona)
        self.__num_personas += 1

    # Insertar datos de un nuevo contacto (alumno, profesor o coordinador).
    def insertar_nuevo_alumno(self):
        """
        Método para agregar un alumno en el directorio.
        Se pedirá cada uno de los campos necesarios y se validará que el número de cuenta no esté repetido.
        """
        while True:
            try:
                num_cuenta = int(input('Escribe el número de cuenta del alumno: '))
                if num_cuenta not in self.__numeros_cuenta:
                    self.__numeros_cuenta.add(num_cuenta)
                    break
                else:
                    print(f"El número de cuenta {num_cuenta} ya existe, escribe otro.")
                    continue
            except ValueError:
                print('El número de cuenta del alumno tiene que ser un entero.')

        nombre = input('Escribe el nombre completo del alumno: ')
        cumpleanios = input('Escribe la fecha de cumpleaños del alumno (día/mes/año): ')
        correo = input('Escribe el correo del alumno: ')
        carrera = input('Escribe la carrera del alumno: ')
        materias = input('Escribe las materias del alumno separadas por comas: ')

        while True:
            try:
                celular = int(input('Escribe el celular del alumno: '))
                break
            except ValueError:
                print('El celular del alumno tiene que ser un entero.')

        while True:
            try:
                semestre = int(input('Escribe el semestre del alumno: '))
                break
            except ValueError:
                print('El semestre del alumno tiene que ser un entero.')

        # Crear el objeto Alumno con los datos ingresados
        nuevo_alumno = cA.Alumno(
            nombre, celular, cumpleanios, correo, num_cuenta, carrera, materias.split(), semestre
        )
        # Agregar el nuevo alumno a la lista de contactos
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

    def buscar_nodo(self, persona) -> object:
        """
        Método auxiliar que busca el nodo que contiene a una persona en la lista de directorio,
        dado el nombre completo.
        :param persona: La persona a buscar en el directorio.
        :return: nodo_1: nodo en el que se encuentra la persona.
        """
        nodo_1 = self.__lista.buscar(persona)
        return nodo_1

    def esta_vacio(self) -> bool:
        """
        Método que verifica si está vacía la lista del directorio.
        :return: True si no hay elementos en la lista, False si hay al menos uno.
        """
        return self.__lista.esta_vacia()  # Se usa el método de la lista simplemente ligada

    def mostrar_persona(self, nombre):
        """
        Método que define cómo mostrar una persona dentro del directorio.
        Representa a la persona a través de los elementos en la lista.
        :param nombre: Nombre de la persona a mostrar.
        :return: Nada. Imprime la representación de la persona si la encuentra, o indica que no la encontró.
        """
        if self.esta_vacio():
            print("No hay contactos.")
            return

        actual = self.__lista.inicio
        alumnos = ''
        profesores = ''
        coordinadores = ''

        while actual is not None:
            if actual.elemento.nombre_completo == nombre:  # Se usa 'nombre' en vez de 'nombre_completo'
                if isinstance(actual.elemento, cA.Alumno):
                    alumnos += str(actual.elemento) + '\n'
                elif isinstance(actual.elemento, cPr.Profesor):
                    profesores += str(actual.elemento) + '\n'
                elif isinstance(actual.elemento, cC.Coordinador):
                    coordinadores += str(actual.elemento) + '\n'
            actual = actual.siguiente

        if alumnos or profesores or coordinadores:
            print('\nALUMNOS:\n' + alumnos + "\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores)
        else:
            print(f"No se encontró a la persona con el nombre {nombre}.")

    # Extra: lectura/escritura de archivos CSV

    def lectura_csvs(self, nombre: str):
        """
        Método que carga/abre la información de un archivo CSV en la lista de directorio,
        dependiendo del tipo de persona, se utilizará el constructor correspondiente.
        :param nombre: Nombre del archivo CSV.
        """
        while True:
            nombre_archivo = nombre
            try:
                with open(nombre_archivo, 'r') as archivo:
                    lector_csv = csv.reader(archivo)
                    for linea in lector_csv:
                        if linea[0] == 'A':  # Alumno
                            nuevo_alumno = cA.Alumno(linea[1], int(linea[2]), linea[3], linea[4], int(linea[5]),
                                                     linea[6], linea[7].split(), int(linea[8]))
                            self.__agregar_a_lista(nuevo_alumno)
                            self.__numeros_cuenta.add(int(linea[5]))
                        elif linea[0] == 'P':  # Profesor
                            nuevo_profesor = cPr.Profesor(linea[1], int(linea[2]), linea[3], linea[4], int(linea[5]),
                                                          int(linea[6]), float(linea[7]), linea[8], linea[9],
                                                          linea[10].split())
                            self.__agregar_a_lista(nuevo_profesor)
                            self.__numeros_profesor.add(int(linea[5]))
                        elif linea[0] == 'C':  # Coordinador
                            nuevo_coordinador = cC.Coordinador(linea[1], int(linea[2]), linea[3], linea[4],
                                                               int(linea[5]), int(linea[6]), float(linea[7]), linea[8],
                                                               linea[9])
                            self.__agregar_a_lista(nuevo_coordinador)
                            self.__numeros_empleado.add(int(linea[5]))
                print("Archivo cargado correctamente.")
                break
            except FileNotFoundError:
                print(f"El archivo {nombre_archivo} no existe.")

    def escritura_csvs(self, nombre: str):
        """
        Método que guarda la información del directorio en un archivo CSV.
        Se itera sobre la lista para guardar los datos de cada persona.
        :param: nombre: Nombre del archivo CSV.
        """
        nombre_archivo = nombre
        f = open(nombre_archivo, 'w')
        it1 = iter(self.__lista)
        try:
            while True:
                cadena = ''
                contacto = next(it1)
                cadena += str(contacto) + "\n"
                f.write(cadena)
        except StopIteration:
            pass
        f.close()
        print(f"Archivo {nombre_archivo} guardado correctamente.")

# Reedefinir el orden de la lista

    # Creo una nueva lista con un comparador diferente y reedefino mi lista inicial
    def ordenar_directorio(self, comparador):
        """
        Este metodo permitira reordenar la lista a partir de otro comparador.
        :param comparador: El comparador con el que se desea hacer el ordenamiento
        :return: el directorio nuevo ordenado
        """
        nuevo_directorio = Li.Lista(comparador)
        it1 = iter(self.__lista)
        try:
            while True:
                elem = next(it1)
                nuevo_directorio.agregar(elem)
        except StopIteration:
            pass
        self.__lista = nuevo_directorio

    def mostrar_informacion_contacto(self, nombre, rol):
        """
        Muestra la informacion completa de un contacto, dado su nombre y rol.
        La informacion se muestra agrupada por categoria (alumno, profesor o coordinador).
        Los contactos se muestran ordenados.
        :param nombre:str -el nombre completo del contacto
        :param rol - tipo de objeto
        :return un string con la informacion completa del contacto con esas caracteristicas.
        """
        # self.ordenar_directorio(0, self.__num_personas - 1, self.nombre_comparador)
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
        if self.__lista.esta_vacia():
            print("No hay contactos.")
            return
        actual = self.__lista.inicio
        encontrado = False
        while actual is not None:
            if actual.elemento.nombre_completo == nombre and isinstance(actual.elemento, rol_clase):
                print(actual.elemento)
                encontrado = True
                break
            actual = actual.siguiente
        if not encontrado:
            print('No existe un contacto con esas características')

    def eliminar_contacto(self, nombre):
        """
        Elimina los datos de un contacto a partir del nombre.
        """
        # self.ordenar_directorio(0, self.__num_personas - 1, self.nombre_comparador)

        if self.esta_vacio():
            print("No hay contactos.")
            return

        actual = self.__lista.inicio
        encontrado = False

        while actual is not None:
            if actual.elemento.nombre_completo == nombre:  # Encontramos el contacto
                # Eliminamos el nodo al saltar la referencia
                self.eliminar(actual.elemento)
                self.__num_personas -= 1  # Actualizamos el contador
                encontrado = True
                print(f"El contacto con el nombre: '{nombre}' ha sido eliminado.")
                break
            actual = actual.siguiente

        if not encontrado:
            print(f"No se encontró contacto con el nombre completo: {nombre}")

    def buscar_nodo_nomcompleto(self, nom):
        """
        Metodo que permite buscar el nodo que contiene a la persona con un cierto atributo
        :param nom: Atributo (Nombre completo) a partir del cual se desea buscar a una persona
        :return: nodo que lo contiene
        """
        pos = self.__lista.inicio
        while pos is not None and not pos.elemento.nombre_completo == nom:
            pos = pos.siguiente
        return pos

######################
    def actualizar_alumno(self):
        """
        Metodo para actualizar un contacto del tipo alumno, si se encuentra el nombre completo del alumno
        desplegara un menu para saber que valor actualizar. Si no imprimira un mensaje.
        """
        nom_completo = input('Escribe el nombre completo del alumno: ')
        nodo = self.buscar_nodo_nomcompleto(nom_completo)
        if nodo is None:
            print(f"No se encuentra el alumno con nombre completo {nom_completo}")
        else:
            alumno = nodo.elemento
            if isinstance(alumno, cA.Alumno) and not isinstance(alumno, cPr.Profesor):
                print(alumno)
                opcion = ''
                while opcion != 'S':
                    opcion = menu_actualizar_alumno()

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
                            alumno.__materias = list(nuevamaterias)
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
        nom_completo = input('Escribe el nombre completo del profesor: ')
        nodo = self.buscar_nodo_nomcompleto(nom_completo)
        if nodo is None:
            print(f"No se encuentra el profesor con nombre completo {nom_completo}")
        else:
            profesor = nodo.elemento
            if isinstance(profesor, cPr.Profesor) and not isinstance(profesor, cC.Coordinador):
                print(profesor)
                opcion = ''
                while opcion != 'S':
                    opcion = menu_actualizar_profesor()

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
                            profesor.__carrera = nuevocarrera
                            print('Carrera Actualizada \n')
                            opcion = ''

                        case '10':
                            nuevgrup = list(input('Escribe la nueva lista de grupos del profesor: '))
                            profesor.__grupos = list(nuevgrup)
                            print('Materias Actualizadas \n')
                            opcion = ''

                        case "S":
                            print('Volviendo ...')
            else:
                print(f"No se encuentra el profesor con nombre {nom_completo}")

    def actualizar_coordinador(self):
        """
        Metodo para actualizar un contacto del tipo Coordinador, si se encuentra el nombre completo del coordinador
        desplegara un menu para saber que valor actualizar. Si no imprimira un mensaje.
        """
        nom_completo = input('Escribe el nombre completo del coordinador: ')
        nodo = self.buscar_nodo_nomcompleto(nom_completo)
        if nodo is None:
            print(f"No se encuentra el coordinador con nombre completo {nom_completo}")
        else:
            coordinador = nodo.elemento
            if isinstance(coordinador, cC.Coordinador) and not isinstance(coordinador, cPr.Profesor):
                print(coordinador)
                opcion = ''
                while opcion != 'S':
                    opcion = menu_actualizar_coordinador()

                    match opcion:
                        case "1":
                            nuevonombre = input('Escribe el nuevo nombre del coordinador a actualizar: ')
                            coordinador.__nombre_completo = nuevonombre
                            print('Nombre Actualizado \n')
                            opcion = ''

                        case "2":
                            nuevocelular = int(input('Escribe la nuevo celular del coordinador: '))
                            coordinador.__celular = nuevocelular
                            print('Celular Actualizado \n')
                            opcion = ''

                        case "3":
                            nuevocumple = int(input('Escribe el nuevo cumpleanios del coordinador: '))
                            coordinador.__fecha_cumpleanios = nuevocumple
                            print('Cumpleanios Actualizado \n')
                            opcion = ''

                        case "4":
                            nuevoemail = input('Escribe el nuevo email del coordinador: ')
                            coordinador.__email = nuevoemail
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
                print(f"No se encuentra el coordinador con nombre {nom_completo}")

    def mostrar_contactos_por_sueldo(self, sueldo: float):
        """
        Muestra todos los contactos con un sueldo determinado.
        La información se muestra agrupada por categoría (profesor o coordinador).
        Los contactos se muestran ordenados.
        :param sueldo: int - el sueldo especifico que busco
        :return un string ordenado que divide profesores y coordinadores con ese sueldo especifico.
        """
        self.ordenar_directorio(Comp.salario_descendente)  # Ordenamos la lista
        actual = self.__lista.inicio
        profesores = ''
        coordinadores = ''

        while actual is not None:
            if isinstance(actual.elemento, (cPr.Profesor, cC.Coordinador)):
                if actual.elemento.sueldo == sueldo:
                    if isinstance(actual.elemento, cPr.Profesor):
                        profesores += str(actual.elemento) + '\n'
                    elif isinstance(actual.elemento, cC.Coordinador):
                        coordinadores += str(actual.elemento) + '\n'
            actual = actual.siguiente

        print("\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores)

    def contiene(self, contacto) -> bool:
        """
        Metodo que permite determinar si un contacto esta contenido en el Directorio
        :param contacto: El contacto a buscar
        :return: True si está contenido, False en caso contrario
        """
        return self.__lista.contiene(contacto)

    def eliminar(self, contacto):
        """
        Este metodo permitira eliminar un contacto del directorio.
        :param contacto: El contacto que se va a eliminar
        """
        # Hay que asegurarnos que el arreglo no este vacío y el elemento exista
        if not self.esta_vacio() and self.contiene(contacto):
            self.__lista.eliminar(contacto)
            print(f"El contacto {contacto} fue eliminado!\n")
        else:
            print(f"El elemento {contacto} no está en el Directorio!\n")

    def eliminar_cel(self, celular):
        """
        Elimina los datos de un contacto a partir del numero de celular.
        :param celular:int - El celular del contacto que se va a eliminar.
        """
        # Buscamos el contacto por número de celular
        actual = self.__lista.inicio
        while actual is not None:
            if actual.elemento.celular == celular:
                # Usamos el método eliminar de la clase Lista
                self.__lista.eliminar(actual)
                print(f"El contacto con el número de celular '{celular}' ha sido eliminado.")
                return
            actual = actual.siguiente
        print(f"No se encontró contacto con el número de celular: {celular}")

    def eliminar_email(self, correo):
        """
        Elimina los datos de un contacto a partir del correo electronico.
        :param: correo:str - el correo de la persona que busco.
        """
        # Buscamos el contacto con ese correo
        actual = self.__lista.inicio
        while actual is not None:
            if actual.elemento.email == correo:
                # Usamos el método eliminar de la clase Lista
                self.eliminar(actual)
                print(f"El contacto con el número de celular '{correo}' ha sido eliminado.")
                return
            actual = actual.siguiente
        print(f"No se encontró contacto con el número de celular: {correo}")

    def buscar_contacto_celular(self, celular: int):
        """
        Busca un contacto en el directorio a partir de su número de celular.
        Nota: Imprime el contacto si es encontrado, o un mensaje si no lo es.
        :param celular: int - Número de celular del contacto.
        :return: El contacto si es encontrado, sino None
        """
        # Usamos la lista para recorrer los contactos
        actual = self.__lista.inicio
        while actual is not None:
            if actual.elemento.celular == celular:
                print(actual.elemento)
                return actual.elemento
            actual = actual.siguiente
        # Mensaje si no encuentra el contacto
        print(f"No se encontró un contacto con celular {celular}")
        return None

    def buscar_contacto_cum(self, cumpleanios: str):
        """
        Busca un contacto en el directorio a partir de su fecha de cumpleaños.
        Nota: Imprime el contacto si es encontrado, o un mensaje si no lo es
        :param cumpleanios: str - Fecha de cumpleaños del contacto.
        :return: Imprime el contacto si es encontrado, o un mensaje si no lo es.
        """
        actual = self.__lista.inicio
        while actual is not None:
            if actual.elemento.fecha_cumpleanios == cumpleanios:
                print(actual.elemento)
                return actual.elemento
            actual = actual.siguiente
        print(f"No se encontró un contacto con cumpleaños {cumpleanios}")
        return None

    def __str__(self) -> (str, str, str):
        """
        Metodo que permitira mostrar el Directorio.
        :return: Una cadena de caracteres que incluiran la informacion de contacto.
        """
        cadena = ''
        if not self.__lista.esta_vacia():
            alumnos = []
            profesores = []
            coordinadores = []
            pos = self.__lista.inicio
            while pos is not None:
                if isinstance(pos.elemento, cA.Alumno):
                    alumnos.append(pos.elemento)
                elif isinstance(pos.elemento, cPr.Profesor):
                    profesores.append(pos.elemento)
                elif isinstance(pos.elemento, cC.Coordinador):
                    coordinadores.append(pos.elemento)
                pos = pos.siguiente
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

    def mostrar_contactos_con_email(self, email):
        """
        Muestra los contactos por categoria y ordenados
        Obs: por como fue definido la clase Persona, los objetos persona
        tienen un email valido.
        """
        if self.__lista.esta_vacia():
            print("No hay contactos.")
            return
        else:
            actual = self.__lista.inicio
            alumnos = ''
            profesores = ''
            coordinadores = ''

            while actual is not None:
                if actual.elemento.email == email:
                    if isinstance(actual.elemento, cA.Alumno):
                        alumnos += str(actual.elemento) + '\n'
                    elif isinstance(actual.elemento, cPr.Profesor):
                        profesores += str(actual.elemento) + '\n'
                    elif isinstance(actual.elemento, cC.Coordinador):
                        coordinadores += str(actual.elemento) + '\n'
                actual = actual.siguiente
        if alumnos or profesores or coordinadores:
            print('\nALUMNOS:\n' + alumnos + "\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores)
        else:
            print(f"No se encontró a la persona con el correo {email}.")

    def mostrar_contactos_por_carrera(self, carrera_particular: str):
        """
        Muestra todos los contactos con una carrera particular.
        La información se muestra agrupada por categoría (alumno, profesor o coordinador).
        Los contactos se muestran ordenados.
        :param carrera_particular: str -la carrera especifica que busco
        :return un string ordenado que divide alumnos, profesores y coordinadores con esa carrera especifica.
        """
        alumnos = ''
        profesores = ''
        coordinadores = ''
        if not self.__lista.esta_vacia():
            actual = self.__lista.inicio
            while actual is not None:
                if isinstance(actual.elemento, cA.Alumno) or isinstance(actual.elemento, cPr.Profesor):
                    if isinstance(actual.elemento, cA.Alumno) and actual.elemento.carrera == carrera_particular:
                        alumnos += str(actual.elemento) + '\n'
                    elif isinstance(actual.elemento, cPr.Profesor) and actual.elemento.carrera == carrera_particular:
                        profesores += str(actual.elemento) + '\n'
                actual = actual.siguiente
        else:
            print("No hay contactos.")
        if alumnos or profesores:  # coordinadores no tienen atributo carrera
            print('\nALUMNOS:\n' + alumnos + "\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores)
        else:
            print(f"No se encontró a la persona con el correo {carrera_particular}.")

    def mostrar_alumnos_o_profesores(self, eleccion):
        """
        Muestra solo los alumnos o solo los maestros en orden
        Esto segun la eleccion del usuario
        :param eleccion: 0 si alumnos, 1 si maestros
        """
        if not self.__lista.esta_vacia():
            actual = self.__lista.inicio
            if eleccion == 0:
                alumnos = ''
                while actual is not None:
                    if isinstance(actual.elemento, cA.Alumno):
                        alumnos += str(actual.elemento) + '\n'
                    actual = actual.siguiente
                print('Alumnos registrados:\n' + alumnos if alumnos else 'No hay alumnos registrados\n')
            elif eleccion == 1:
                profesores = ''
                while actual is not None:
                    if isinstance(actual.elemento, cPr.Profesor):
                        profesores += str(actual.elemento) + '\n'
                    actual = actual.siguiente
                print('Profesores registrados:\n' + profesores if profesores else 'No hay profesores registrados\n')
            else:
                print('No es una entrada válida')
        else:
            print("No hay contactos.")
