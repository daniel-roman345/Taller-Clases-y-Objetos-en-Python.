"""
Reto Integrador - Sistema de Préstamos de Equipos.

Demostración funcional en consola de todo el sistema: registro de
usuarios y equipos, préstamos, consultas, modificaciones, devoluciones
y manejo de casos de error.
"""

from equipo import Equipo
from usuario import Usuario
from sistema_prestamos import SistemaPrestamos


def separador(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def main():
    sistema = SistemaPrestamos()

    # ---------- Registro de equipos ----------
    separador("1. REGISTRO DE EQUIPOS")
    print(sistema.registrar_equipo(Equipo("E001", "Portátil Lenovo", "Computador", "Lenovo")))
    print(sistema.registrar_equipo(Equipo("E002", "Portátil HP", "Computador", "HP")))
    print(sistema.registrar_equipo(Equipo("E003", "Videobeam Epson", "Videobeam", "Epson")))
    print(sistema.registrar_equipo(Equipo("E004", "Tablet Samsung", "Tablet", "Samsung")))
    print(sistema.registrar_equipo(Equipo("E001", "Duplicado", "Computador", "X")))

    # ---------- Registro de usuarios ----------
    separador("2. REGISTRO DE USUARIOS")
    print(sistema.registrar_usuario(Usuario("1002003004", "Daniel Salas", "Aprendiz", "daniel@sena.edu.co")))
    print(sistema.registrar_usuario(Usuario("1003004005", "Laura Gómez", "Aprendiz", "laura@sena.edu.co")))
    print(sistema.registrar_usuario(Usuario("2001002003", "Carlos Ríos", "Instructor", "carlos@sena.edu.co")))

    # ---------- Listado inicial ----------
    separador("3. INVENTARIO INICIAL DE EQUIPOS")
    print(sistema.listar_equipos())

    separador("4. LISTADO DE USUARIOS")
    print(sistema.listar_usuarios())

    # ---------- Préstamos ----------
    separador("5. REGISTRO DE PRÉSTAMOS")
    print(sistema.registrar_prestamo("1002003004", "E001", "Clase de POO"))
    print(sistema.registrar_prestamo("1003004005", "E003", "Presentación de proyecto"))
    print(sistema.registrar_prestamo("2001002003", "E002"))
    # Casos de error
    print(sistema.registrar_prestamo("9999999999", "E004"))
    print(sistema.registrar_prestamo("1002003004", "E999"))
    print(sistema.registrar_prestamo("1002003004", "E002"))  # ya prestado

    # ---------- Consultas ----------
    separador("6. PRÉSTAMOS ACTIVOS")
    print(sistema.listar_prestamos(solo_activos=True))

    separador("7. PRÉSTAMOS DE UN USUARIO ESPECÍFICO")
    print(sistema.consultar_prestamos_de_usuario("1002003004"))

    # ---------- Modificación ----------
    separador("8. MODIFICACIÓN DE OBSERVACIONES")
    print(sistema.modificar_observaciones(1, "Se entrega con cargador y mouse."))

    # ---------- Devoluciones ----------
    separador("9. DEVOLUCIÓN DE EQUIPOS")
    print(sistema.devolver_prestamo(1, "Bueno"))
    print(sistema.devolver_prestamo(2, "Regular"))
    print(sistema.devolver_prestamo(1))  # ya devuelto
    print(sistema.devolver_prestamo(99))  # inexistente

    # ---------- Estado final ----------
    separador("10. ESTADO FINAL DEL INVENTARIO")
    print(sistema.listar_equipos())

    separador("11. HISTÓRICO COMPLETO DE PRÉSTAMOS")
    print(sistema.listar_prestamos())

    separador("12. PRÉSTAMOS ACTIVOS RESTANTES")
    print(sistema.listar_prestamos(solo_activos=True))


if __name__ == "__main__":
    main()
