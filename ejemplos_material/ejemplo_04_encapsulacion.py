"""
Ejemplo 4 del material didáctico: Encapsulación.

Se replica el ejemplo donde se protege el acceso directo a los atributos
usando la convención del guion bajo (_atributo) y se exponen métodos
públicos (getters y setters) para leerlos y modificarlos de forma
controlada.
"""


class CuentaBancaria:
    """Cuenta bancaria con saldo encapsulado."""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        # Atributo protegido: se usa guion bajo por convención.
        self.__saldo = saldo_inicial

    # Getter: acceso controlado al saldo.
    def obtener_saldo(self):
        return self.__saldo

    # Setter: modificación controlada del saldo.
    def depositar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva."
        self.__saldo += cantidad
        return f"Depósito exitoso. Nuevo saldo: ${self.__saldo}"

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva."
        if cantidad > self.__saldo:
            return "Fondos insuficientes."
        self.__saldo -= cantidad
        return f"Retiro exitoso. Nuevo saldo: ${self.__saldo}"


def main():
    print("=== EJEMPLO 4: ENCAPSULACIÓN ===")
    cuenta = CuentaBancaria("Daniel Salas", 1000)
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo inicial: ${cuenta.obtener_saldo()}")
    print(cuenta.depositar(500))
    print(cuenta.retirar(200))
    print(cuenta.retirar(5000))
    print(f"Saldo final: ${cuenta.obtener_saldo()}")

    # Demostración: el atributo __saldo no se puede leer directamente.
    try:
        print(cuenta.__saldo)  # noqa: intencional para mostrar el error
    except AttributeError as e:
        print(f"Acceso directo bloqueado por encapsulación: {e}")


if __name__ == "__main__":
    main()
