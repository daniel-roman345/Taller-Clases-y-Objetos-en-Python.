"""
Taller de Encapsulación - Caso 1: Cuenta Bancaria.

Se aplican los principios de encapsulación: los atributos sensibles se
declaran como privados (doble guion bajo) y solo se accede a ellos
mediante métodos públicos (getters/setters) que validan las operaciones.
"""


class CuentaBancaria:
    """Cuenta bancaria con saldo y clave encapsulados."""

    def __init__(self, titular, saldo_inicial, clave):
        self.titular = titular
        self.__saldo = saldo_inicial
        self.__clave = clave

    # Getter con validación de clave.
    def consultar_saldo(self, clave):
        if clave != self.__clave:
            return "Clave incorrecta. Acceso denegado."
        return f"Saldo actual de {self.titular}: ${self.__saldo}"

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva."
        self.__saldo += cantidad
        return f"Depósito exitoso. Nuevo saldo: ${self.__saldo}"

    def retirar(self, cantidad, clave):
        if clave != self.__clave:
            return "Clave incorrecta. No se puede retirar."
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva."
        if cantidad > self.__saldo:
            return "Fondos insuficientes."
        self.__saldo -= cantidad
        return f"Retiro exitoso. Nuevo saldo: ${self.__saldo}"

    def cambiar_clave(self, clave_actual, clave_nueva):
        if clave_actual != self.__clave:
            return "Clave actual incorrecta."
        if len(str(clave_nueva)) < 4:
            return "La nueva clave debe tener al menos 4 caracteres."
        self.__clave = clave_nueva
        return "Clave actualizada correctamente."


def main():
    print("=== TALLER ENCAPSULACIÓN - CASO 1: CUENTA BANCARIA ===")
    cuenta = CuentaBancaria("Daniel Salas", 500000, "1234")

    print(cuenta.consultar_saldo("1234"))
    print(cuenta.consultar_saldo("0000"))

    print("\n=== DEPÓSITOS Y RETIROS ===")
    print(cuenta.depositar(150000))
    print(cuenta.retirar(200000, "1234"))
    print(cuenta.retirar(1000000, "1234"))
    print(cuenta.retirar(50000, "0000"))

    print("\n=== CAMBIO DE CLAVE ===")
    print(cuenta.cambiar_clave("1234", "9876"))
    print(cuenta.consultar_saldo("9876"))


if __name__ == "__main__":
    main()
