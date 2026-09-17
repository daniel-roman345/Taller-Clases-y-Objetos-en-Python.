"""
Módulo Equipo: define la clase Equipo del Sistema de Préstamos.

Aplica encapsulación sobre los atributos sensibles (disponibilidad y
estado interno) y expone métodos públicos para consultarlos y
modificarlos de forma controlada.
"""


class Equipo:
    """Representa un equipo prestable (computador, videobeam, etc.)."""

    def __init__(self, codigo, nombre, tipo, marca):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        # Atributos encapsulados (sensibles).
        self.__disponible = True
        self.__estado = "Bueno"  # Bueno / Regular / Malo

    # ---------- Getters controlados ----------
    def esta_disponible(self):
        return self.__disponible

    def obtener_estado(self):
        return self.__estado

    # ---------- Setters controlados ----------
    def marcar_prestado(self):
        if not self.__disponible:
            return False
        self.__disponible = False
        return True

    def marcar_disponible(self):
        if self.__disponible:
            return False
        self.__disponible = True
        return True

    def actualizar_estado(self, nuevo_estado):
        estados_validos = ("Bueno", "Regular", "Malo")
        if nuevo_estado not in estados_validos:
            return False
        self.__estado = nuevo_estado
        return True

    def ficha(self):
        disp = "Disponible" if self.__disponible else "Prestado"
        return (
            f"[{self.codigo}] {self.nombre} ({self.tipo} - {self.marca}) "
            f"| Estado: {self.__estado} | {disp}"
        )
