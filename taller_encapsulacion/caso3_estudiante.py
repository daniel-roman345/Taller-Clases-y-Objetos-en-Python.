"""
Taller de Encapsulación - Caso 3: Estudiante.

Se encapsulan las notas del estudiante. Solo pueden registrarse a través
de un método que valida el rango, y el promedio se calcula internamente.
"""


class Estudiante:
    """Estudiante con notas privadas y promedio calculado."""

    def __init__(self, nombre, programa):
        self.nombre = nombre
        self.programa = programa
        self.__notas = []

    def registrar_nota(self, nota):
        if not (0 <= nota <= 5):
            return f"Nota inválida ({nota}). Debe estar entre 0 y 5."
        self.__notas.append(nota)
        return f"Nota {nota} registrada para {self.nombre}."

    def obtener_notas(self):
        # Se retorna una copia para evitar modificaciones externas.
        return list(self.__notas)

    def promedio(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def aprobado(self):
        return self.promedio() >= 3.0

    def boletin(self):
        estado = "APROBADO" if self.aprobado() else "REPROBADO"
        return (
            f"Estudiante: {self.nombre}\n"
            f"Programa: {self.programa}\n"
            f"Notas: {self.obtener_notas()}\n"
            f"Promedio: {self.promedio():.2f}\n"
            f"Estado: {estado}"
        )


def main():
    print("=== TALLER ENCAPSULACIÓN - CASO 3: ESTUDIANTE ===")
    est = Estudiante("Daniel Salas", "Análisis y Desarrollo de Software")

    print(est.registrar_nota(4.5))
    print(est.registrar_nota(3.8))
    print(est.registrar_nota(4.2))
    print(est.registrar_nota(6.0))  # inválida
    print(est.registrar_nota(2.9))

    print("\n=== BOLETÍN FINAL ===")
    print(est.boletin())


if __name__ == "__main__":
    main()
