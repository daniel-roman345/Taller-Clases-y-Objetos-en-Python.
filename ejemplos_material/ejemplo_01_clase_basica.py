"""
Ejemplo 1 del material didáctico: Clase básica en Python.

Se replica el ejemplo introductorio donde se define una clase mínima con
atributos y un método simple, tal como aparece en el material de formación
sobre Fundamentos de Python: Clases, Objetos y Encapsulación.
"""


class Persona:
    """Clase básica que representa a una persona."""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."


def main():
    # Creación de dos objetos (instancias) a partir de la clase Persona
    persona1 = Persona("Daniel", 20)
    persona2 = Persona("María", 25)

    print("=== EJEMPLO 1: CLASE BÁSICA ===")
    print(persona1.saludar())
    print(persona2.saludar())


if __name__ == "__main__":
    main()
