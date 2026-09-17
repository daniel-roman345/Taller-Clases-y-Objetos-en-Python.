"""
Taller de Clases y Objetos - Caso 2: Clase Persona.

Se implementa una clase Persona con atributos y métodos para registrar
datos básicos y comportamiento, validando su funcionamiento en consola.
"""


class Persona:
    """Representa a una persona con nombre, edad, documento y ciudad."""

    def __init__(self, nombre, edad, documento, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.documento = documento
        self.ciudad = ciudad

    def presentarse(self):
        return (
            f"Hola, soy {self.nombre}, tengo {self.edad} años, "
            f"mi documento es {self.documento} y vivo en {self.ciudad}."
        )

    def cumplir_años(self):
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años."

    def es_mayor_de_edad(self):
        return self.edad >= 18


def main():
    print("=== TALLER CLASES Y OBJETOS - CASO 2: PERSONA ===")
    p1 = Persona("Daniel Salas", 20, "1002003004", "Bogotá")
    p2 = Persona("Laura Gómez", 17, "1003004005", "Medellín")

    print(p1.presentarse())
    print(p2.presentarse())

    print("\n=== CUMPLEAÑOS ===")
    print(p1.cumplir_años())
    print(p2.cumplir_años())

    print("\n=== MAYORÍA DE EDAD ===")
    print(f"{p1.nombre} mayor de edad: {p1.es_mayor_de_edad()}")
    print(f"{p2.nombre} mayor de edad: {p2.es_mayor_de_edad()}")


if __name__ == "__main__":
    main()
