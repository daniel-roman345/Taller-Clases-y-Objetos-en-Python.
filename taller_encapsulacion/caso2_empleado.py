"""
Taller de Encapsulación - Caso 2: Empleado.

Se encapsulan el salario y la evaluación del empleado. Solo pueden
modificarse a través de métodos que validan la operación.
"""


class Empleado:
    """Empleado con salario y evaluación encapsulados."""

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario
        self.__evaluacion = 0

    def obtener_salario(self):
        return self.__salario

    def obtener_evaluacion(self):
        return self.__evaluacion

    def aumentar_salario(self, porcentaje):
        if porcentaje <= 0 or porcentaje > 100:
            return "El porcentaje de aumento debe estar entre 1 y 100."
        aumento = self.__salario * (porcentaje / 100)
        self.__salario += aumento
        return (
            f"Salario de {self.nombre} aumentado en {porcentaje}%. "
            f"Nuevo salario: ${self.__salario:,.0f}"
        )

    def registrar_evaluacion(self, puntaje):
        if not (0 <= puntaje <= 100):
            return "El puntaje debe estar entre 0 y 100."
        self.__evaluacion = puntaje
        return f"Evaluación registrada para {self.nombre}: {puntaje}/100"

    def resumen(self):
        return (
            f"Empleado: {self.nombre}\n"
            f"Cargo: {self.cargo}\n"
            f"Salario: ${self.__salario:,.0f}\n"
            f"Evaluación: {self.__evaluacion}/100"
        )


def main():
    print("=== TALLER ENCAPSULACIÓN - CASO 2: EMPLEADO ===")
    emp = Empleado("Daniel Salas", "Desarrollador Jr", 2000000)

    print(emp.resumen())
    print("\n" + emp.aumentar_salario(15))
    print(emp.registrar_evaluacion(92))
    print(emp.aumentar_salario(150))
    print(emp.registrar_evaluacion(120))

    print("\n=== RESUMEN FINAL ===")
    print(emp.resumen())


if __name__ == "__main__":
    main()
