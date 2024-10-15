# Programa: claseAlumno.py
# Objetivo: Clase que modela un Alumno que hereda de Persona
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-09-2024

import clasePersona as cP


class Alumno(cP.Persona):
    """
    Clase que representa una persona del tipo Alumno.
    """
    def __init__(self, nombre_completo: str, celular: int, fecha_cumpleanios: str, email: str, num_cuenta: int,
                 carrera: str, materias: list, semestre: int):
        """
        Constructor para un Alumno, ademas de los datos de una Persona, recibe el numero de cuenta,
        su carrera, una lista de materias y el semestre al que esta inscrito.
        :param nombre_completo:str - El nombre completo del Alumno
        :param celular:int - El celular del Alumno
        :param fecha_cumpleanios:str - La fecha de cumpleanios del Alumno
        :param email:str - EL correo electronico del Alumno
        :param num_cuenta:int - El numero de cuenta del Alumno
        :param carrera:str - La carrera del Alumno
        :param materias:list - La lista de materias del Alumno
        :param semestre:int - El semestre al que esta inscrito el Alumno
        """
        super().__init__(nombre_completo, celular, fecha_cumpleanios, email)
        self.__num_cuenta = num_cuenta
        self.__carrera = carrera
        self.__materias = materias
        self.__semestre = semestre

    # Metodos GET
    @property
    def num_cuenta(self) -> int:
        """
        Metodo para obtener el numero de cuenta del Alumno
        :return: El numero de cuenta del Alumno
        :rtype: int
        """
        return self.__num_cuenta

    @property
    def carrera(self) -> str:
        """
        Metodo para obtener la carrera del Alumno
        :return: La carrera del Alumno
        :rtype: str
        """
        return self.__carrera

    @property
    def materias(self) -> list:
        """
        Metodo para obtener las materias del Alumno
        :return: La lista de materias del Alumno
        :rtype: list
        """
        return self.__materias

    @property
    def semestre(self) -> int:
        """
        Metodo para obtener el semestre del Alumno
        :return: El semestre del Alumno
        :rtype: int
        """
        return self.__semestre

    # Metodos SET
    @num_cuenta.setter
    def num_cuenta(self, num_cuenta: int):
        """
        Metodo para modificar el numero de cuenta del Alumno
        :param num_cuenta: El numero de cuenta del Alumno
        """
        self.__num_cuenta = num_cuenta

    @carrera.setter
    def carrera(self, carrera: str):
        """
        Metodo para modificar la carrera del Alumno
        :param carrera: La carrera del Alumno
        """
        self.__carrera = carrera

    @materias.setter
    def materias(self, materias: list):
        """
        Metodo para modificar las materias del Alumno
        :param materias: La lista de materias del Alumno
        """
        self.__materias = materias

    @semestre.setter
    def semestre(self, semestre: int):
        """
        Metodo para modificar el semestre del Alumno
        :param semestre: El semestre del Alumno
        """
        self.__semestre = semestre

    # Metodos calculadores
    def __str__(self) -> str:
        """
        Metodo para obtener un Alumno en formato cadena
        :return: El Alumno en formato de impresion
        :rtype: str
        """
        return super().__str__().replace("Persona", "Alumno") + \
            " | Num_cuenta: {} | Carrera: {} | Materias: {} | Semestre: {} |".format(self.__num_cuenta,
                                                                                     self.__carrera, self.__materias,
                                                                                     self.__semestre)
    # Este metodo se define cuando se desea que los objetos se guarden en un archivo

    def __iter__(self):
        """
        Metodo que devuelve una representacion iterable de un objeto
        :return: La representacion en formato iterable del Alumno
        :rtype: iterable
        """
        return iter([super().nombre_completo, super().celular, super().fecha_cumpleanios, super().email,
                     self.__num_cuenta, self.__carrera, self.__materias, self.__semestre])
    # Estos metodos se tienen que agregar cuando se trabajan con objetos en los Conjuntos y lograr
    # que sus objetos sean hasheables

    def __llave(self) -> tuple:
        """
        Metodo privado que permite definir una llave a través de los atributos del objeto
        :return: Una tupla con los atributos del objeto.
        :rtype: tuple
        """
        return (super().nombre_completo, super().celular, super().fecha_cumpleanios, super().email, self.__num_cuenta,
                self.__carrera, self.__materias, self.__semestre)

    def __hash__(self) -> int:
        """
        Metodo que internamente llama la funcion hash() para obtener el valor hash del objeto.
        Se utilizan generalmente para una comparacion mas rapida entre los dos objetos,
        ya que los valores hash se comparan directamente en lugar de comparar el valor de cada objeto.
        :return: Un valor entero que corresponde al valor hash del objeto
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otro) -> bool:
        """
        Metodo que permite definir el criterio de igualdad para dos objetos
        :param otro: El Alumno con el que se va a realizar la comparacion
        :return: True si los Alumnos son iguales, False en caso contrario
        :rtype: bool
        """
        if isinstance(otro, Alumno):
            return self.__llave() == otro.__llave()