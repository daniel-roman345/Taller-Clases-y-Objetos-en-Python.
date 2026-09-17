"""
Módulo Usuario: define la clase Usuario del Sistema de Préstamos.

El documento y la lista de préstamos activos se manejan de forma
encapsulada para preservar la integridad de los datos.
"""


class Usuario:
    """Representa a un usuario del sistema (aprendiz, instructor, etc.)."""

    def __init__(self, documento, nombre, rol, correo):
        self.__documento = documento
        self.nombre = nombre
        self.rol = rol
        self.correo = correo
        self.__prestamos_activos = []  # códigos de equipos prestados

    def obtener_documento(self):
        return self.__documento

    def obtener_prestamos_activos(self):
        return list(self.__prestamos_activos)

    def agregar_prestamo(self, codigo_equipo):
        if codigo_equipo in self.__prestamos_activos:
            return False
        self.__prestamos_activos.append(codigo_equipo)
        return True

    def quitar_prestamo(self, codigo_equipo):
        if codigo_equipo not in self.__prestamos_activos:
            return False
        self.__prestamos_activos.remove(codigo_equipo)
        return True

    def ficha(self):
        return (
            f"Usuario: {self.nombre} | Doc: {self.__documento} | "
            f"Rol: {self.rol} | Correo: {self.correo} | "
            f"Préstamos activos: {len(self.__prestamos_activos)}"
        )
