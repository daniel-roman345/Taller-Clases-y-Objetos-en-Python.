"""
Ejemplo 2 del material didáctico: Atributos y métodos.

Se replica el ejemplo donde se muestra cómo una clase agrupa datos
(atributos) y comportamientos (métodos) que operan sobre ellos.
"""


class Vehiculo:
    """Clase que representa un vehículo con atributos y métodos."""

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"El {self.marca} {self.modelo} ha sido encendido."
        return f"El {self.marca} {self.modelo} ya estaba encendido."

    def apagar(self):
        if self.encendido:
            self.encendido = False
            return f"El {self.marca} {self.modelo} ha sido apagado."
        return f"El {self.marca} {self.modelo} ya estaba apagado."

    def describir(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"{self.marca} {self.modelo} ({self.año}) - {estado}."


def main():
    print("=== EJEMPLO 2: ATRIBUTOS Y MÉTODOS ===")
    auto = Vehiculo("Toyota", "Corolla", 2022)
    print(auto.describir())
    print(auto.encender())
    print(auto.describir())
    print(auto.apagar())


if __name__ == "__main__":
    main()
