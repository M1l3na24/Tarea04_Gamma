# Programa: clasePersona.py
# Objetivo: Clase que modela una Persona
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Fecha: 09-09-2024

from datetime import date
from validate_email import validate_email


class Persona:
    """
    Clase que representa una persona.
    """
    def __init__(self, *params):
        """
        Constructor por omision que permite crear Personas.
        :param params: Lista variable de parámetros (0, n) donde:
            nombre_completo: Str - El nombre completo de la persona
            celular: Int - El celular de la persona
            fecha_cumpleanios: Str - La fecha de cumpleanios de la persona no es lo mismo que la fecha de nacimiento
            email: Str - El email de la persona
        """
        if len(params) == 0:  # Constructor por omision
            print('No es posible crear una Persona sin informacion de contacto.')
        elif len(params) == 4:  # Constructor por parametros
            self.__nombre_completo = params[0]
            self.__celular = params[1]
            self.__fecha_cumpleanios = params[2]
            # confirmo que es una direccion valida
            if validate_email(params[3]):
                self.__email = params[3]
            # si no es valida
            else:
                raise ValueError(f"El correo electronico '{params[3]}' no es valido.")
        # casos donde me faltan parametros
        else:
            print('Faltan parametros para definir a la persona.')

    # Metodos GET
    @property
    def nombre_completo(self) -> str:
        """
        Metodo para obtener el nombre completo de la Persona
        :return: El nombre completo de la Persona
        :rtype: str
        """
        return self.__nombre_completo

    @property
    def celular(self) -> int:
        """
        Metodo para obtener el celular de la Persona
        :return: El celular de la Persona
        :rtype: str
        """
        return self.__celular

    @property
    def fecha_cumpleanios(self):
        """
        Metodo para obtener la fecha de cumpleanios de la Persona
        :return: La fecha de cumpleanios de la Persona
        :rtype: str
        """
        return self.__fecha_cumpleanios

    @property
    def email(self):
        """
        Metodo para obtener el email de la Persona
        :return: El email de la Persona
        :rtype: str
        """
        return self.__email

    # Metodos SET
    @nombre_completo.setter
    def nombre_completo(self, nombre_completo: str):
        """
        Metodo para modificar el nombre completo de la Persona
        :param nombre_completo: El nombre completo de la Persona
        """
        self.__nombre_completo = nombre_completo

    @celular.setter
    def celular(self, celular: int):
        """
        Metodo para modificar el celular de la Persona
        :param celular: El celular de la Persona
        """
        self.__celular = celular

    @fecha_cumpleanios.setter
    def fecha_cumpleanios(self, fecha_cumpleanios: str):
        """
        Método para modificar la fecha de cumpleanios de la Persona
        :param fecha_cumpleanios: La fecha de cumpleanios de la Persona
        """
        self.__fecha_cumpleanios = fecha_cumpleanios

    @email.setter
    def email(self, email: str):
        """
        Metodo para modificar el correo de la Persona
        :param email: El correo de la Persona
        """
        if validate_email(email):  # Si devuelve True, el correo es valido
            self.__email = email
        else:  # El correo no es valido y se define un correo generico
            print("El correo no es valido!\n"
                  f"Se conservo el mismo email: {self.__email}")
            self.__email = self.__email

    def edad(self):
        """
        Método para calcular la edad de una Persona
        :return: La edad de la Persona en años
        :rtype: int
        """
        hoy = date.today()  # Fecha actual
        diferencia_dias = hoy - self.__fecha_cumpleanios
        edad = diferencia_dias.days // 365.25
        return int(edad)

    # Metodos calculadores
    def __str__(self):
        """
        Metodo que permite definir una persona en formato cadena
        :return: La Persona en formato str
        :rtype: str
        """
        return ("Persona: {} | Celular: {} | "
                "Fecha cumpleanios: {} | Email: {}").format(self.__nombre_completo,
                                                            self.__celular,
                                                            self.__fecha_cumpleanios,
                                                            self.__celular,
                                                            self.__email)

    # Este metodo se define cuando se desea que los objetos se guarden en un archivo
    def __iter__(self):
        """
        Metodo que devuelve una representacion iterable de un objeto
        :return: La representacion en formato Lista de las Personas
        :rtype: iterable
        """
        return iter([self.__nombre_completo, self.__celular, self.__fecha_cumpleanios, self.__email])

    # Estos metodos se tienen que agregar cuando se trabajan con objetos en los Conjuntos y lograr
    # que sus objetos sean hasheables
    def __llave(self) -> tuple:
        """
        Método privado que permite definir una llave a traves de los atributos del objeto
        :return: Una tupla con los atributos del objeto.
        :rtype: tuple
        """
        return self.__nombre_completo, self.__celular, self.__fecha_cumpleanios, self.__email

    def __hash__(self) -> int:
        """
        Metodo que internamente llama la función hash() para obtener el valor hash del objeto.
        Se utilizan generalmente para una comparación mas rapida entre los dos objetos,
        ya que los valores hash se comparan directamente en lugar de comparar el valor de cada objeto.
        :return: Un valor entero que corresponde al valor hash del objeto
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otra) -> bool:
        """
        Metodo que permite definir el criterio de igualdad para dos objetos
        :param otra: La Persona con la que se va a realizar la comparacion
        :return: True si las Personas son iguales, False en caso contrario
        :rtype: bool
        """
        if isinstance(otra, Persona):
            return self.__llave() == otra.__llave()

    def __lt__(self, otra):
        """
        Metodo que permite definir el criterio de menor igual para dos objetos
        a partir de su nombre completo.
        :param otra: La Persona con la que se va a realizar la comparacion
        :return: True si la persona self es menor a la otra persona, False en caso contrario
        :rtype: bool
        """
        if isinstance(otra, Persona):
            return self.__nombre_completo < otra.__nombre_completo
        return NotImplemented

    def __gt__(self, otra):
        """
        Metodo que permite definir el criterio de menor igual para dos objetos
        a partir de su nombre completo.
        :param otra: La Persona con la que se va a realizar la comparacion
        :return: True si la persona self es mayor que la otra persona, False en caso contrario
        :rtype: bool
        """
        if isinstance(otra, Persona):
            return self.__nombre_completo < otra.__nombre_completo
        return NotImplemented
