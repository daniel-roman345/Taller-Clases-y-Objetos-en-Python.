class Libro:
    """
    Clase que representa un libro en una biblioteca.
    """

    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro.

        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            paginas (int): Número total de páginas.
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True

    def prestar(self):
        """
        Presta el libro si está disponible.
        """
        if self.disponible:
            self.disponible = False
            return f'El libro "{self.titulo}" ha sido prestado.'
        return f'El libro "{self.titulo}" no está disponible.'

    def devolver(self):
        """
        Devuelve el libro a la biblioteca.
        """
        if not self.disponible:
            self.disponible = True
            return f'El libro "{self.titulo}" ha sido devuelto.'
        return f'El libro "{self.titulo}" ya estaba en la biblioteca.'

    def informacion(self):
        """
        Devuelve la información completa del libro.
        """
        estado = "Disponible" if self.disponible else "Prestado"

        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Páginas: {self.paginas}\n"
            f"Estado: {estado}"
        )


# Prueba de la clase Libro
def main():

    # Crear dos libros
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

    # Información inicial
    print("=== INFORMACIÓN INICIAL ===")
    print(libro1.informacion())
    print()
    print(libro2.informacion())

    # Prestar libros
    print("\n=== PRÉSTAMOS ===")
    print(libro1.prestar())
    print(libro2.prestar())

    # Intentar prestar nuevamente
    print("\n=== INTENTO DE PRESTAR DE NUEVO ===")
    print(libro1.prestar())

    # Información después del préstamo
    print("\n=== ESTADO ACTUAL ===")
    print(libro1.informacion())

    # Devolver libro
    print("\n=== DEVOLUCIÓN ===")
    print(libro1.devolver())

    # Intentar devolver nuevamente
    print(libro1.devolver())

    # Información final
    print("\n=== INFORMACIÓN FINAL ===")
    print(libro1.informacion())
    print()
    print(libro2.informacion())


if __name__ == "__main__":
    main()