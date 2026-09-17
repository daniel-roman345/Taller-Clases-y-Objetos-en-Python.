"""
Taller de Clases y Objetos - Caso 3: Clase Producto.

Se implementa una clase Producto para gestionar inventario básico.
"""


class Producto:
    """Producto con nombre, precio y stock."""

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= 0:
            return "La cantidad debe ser positiva."
        if cantidad > self.stock:
            return (
                f"No hay stock suficiente de '{self.nombre}'. "
                f"Disponibles: {self.stock}."
            )
        self.stock -= cantidad
        total = cantidad * self.precio
        return (
            f"Venta realizada: {cantidad} x {self.nombre} = ${total}. "
            f"Stock restante: {self.stock}."
        )

    def reabastecer(self, cantidad):
        if cantidad <= 0:
            return "La cantidad debe ser positiva."
        self.stock += cantidad
        return f"Reabastecido '{self.nombre}'. Stock actual: {self.stock}."

    def mostrar(self):
        return (
            f"Producto: {self.nombre} | Precio: ${self.precio} | "
            f"Stock: {self.stock}"
        )


def main():
    print("=== TALLER CLASES Y OBJETOS - CASO 3: PRODUCTO ===")
    p1 = Producto("Café", 12000, 10)
    p2 = Producto("Cuaderno", 5000, 3)

    print(p1.mostrar())
    print(p2.mostrar())

    print("\n=== VENTAS ===")
    print(p1.vender(3))
    print(p2.vender(5))
    print(p2.vender(2))

    print("\n=== REABASTECIMIENTO ===")
    print(p2.reabastecer(10))

    print("\n=== ESTADO FINAL ===")
    print(p1.mostrar())
    print(p2.mostrar())


if __name__ == "__main__":
    main()
