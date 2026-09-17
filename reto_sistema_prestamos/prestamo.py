"""
Módulo Prestamo: define la clase Prestamo del Sistema de Préstamos.

Representa la relación entre un Usuario y un Equipo con las fechas
de préstamo y devolución. El estado del préstamo se encapsula para
que solo el sistema pueda cerrarlo mediante métodos controlados.
"""

from datetime import datetime


class Prestamo:
    """Registra un préstamo puntual de un equipo a un usuario."""

    _contador = 0  # id incremental compartido por todos los préstamos

    def __init__(self, documento_usuario, codigo_equipo, observaciones=""):
        Prestamo._contador += 1
        self.id = Prestamo._contador
        self.documento_usuario = documento_usuario
        self.codigo_equipo = codigo_equipo
        self.observaciones = observaciones
        self.fecha_prestamo = datetime.now()
        self.__fecha_devolucion = None
        self.__activo = True

    def esta_activo(self):
        return self.__activo

    def obtener_fecha_devolucion(self):
        return self.__fecha_devolucion

    def cerrar(self):
        """Marca el préstamo como devuelto."""
        if not self.__activo:
            return False
        self.__activo = False
        self.__fecha_devolucion = datetime.now()
        return True

    def ficha(self):
        estado = "ACTIVO" if self.__activo else "DEVUELTO"
        fecha_dev = (
            self.__fecha_devolucion.strftime("%Y-%m-%d %H:%M")
            if self.__fecha_devolucion
            else "—"
        )
        return (
            f"Préstamo #{self.id} | Usuario: {self.documento_usuario} | "
            f"Equipo: {self.codigo_equipo} | "
            f"Salida: {self.fecha_prestamo.strftime('%Y-%m-%d %H:%M')} | "
            f"Devolución: {fecha_dev} | Estado: {estado}"
        )
