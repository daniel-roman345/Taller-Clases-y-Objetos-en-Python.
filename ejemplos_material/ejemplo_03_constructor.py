"""
Ejemplo 3 del material didáctico: El constructor __init__.

Se replica el ejemplo donde se muestra cómo el método especial __init__
inicializa el estado del objeto al momento de crearlo.
"""


class Estudiante:
    """Representa a un estudiante inicializado a través de su constructor."""

    def __init__(self, nombre, programa, semestre):
        self.nombre = nombre
        self.programa = programa
        self.semestre = semestre
        self.notas = []

    def registrar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def mostrar(self):
        return (
            f"Estudiante: {self.nombre}\n"
            f"Programa: {self.programa}\n"
            f"Semestre: {self.semestre}\n"
            f"Promedio: {self.promedio():.2f}"
        )


def main():
    print("=== EJEMPLO 3: CONSTRUCTOR __init__ ===")
    est = Estudiante("Daniel Salas", "ADSO", 2)
    est.registrar_nota(4.5)
    est.registrar_nota(3.8)
    est.registrar_nota(4.2)
    print(est.mostrar())


if __name__ == "__main__":
    main()
