"""
Módulo SistemaPrestamos: orquesta usuarios, equipos y préstamos.

Emplea colecciones (listas y diccionarios) para organizar la información
y expone las operaciones principales: registrar, consultar, modificar y
devolver préstamos.
"""

from equipo import Equipo
from usuario import Usuario
from prestamo import Prestamo


class SistemaPrestamos:
    """Fachada del sistema. Centraliza toda la lógica del negocio."""

    def __init__(self):
        # Diccionarios para acceso rápido por clave.
        self.equipos = {}     # {codigo: Equipo}
        self.usuarios = {}    # {documento: Usuario}
        # Lista para el histórico completo de préstamos.
        self.prestamos = []   # [Prestamo, ...]

    # ---------- Registro ----------
    def registrar_equipo(self, equipo):
        if equipo.codigo in self.equipos:
            return f"Ya existe un equipo con código {equipo.codigo}."
        self.equipos[equipo.codigo] = equipo
        return f"Equipo '{equipo.nombre}' registrado con código {equipo.codigo}."

    def registrar_usuario(self, usuario):
        doc = usuario.obtener_documento()
        if doc in self.usuarios:
            return f"Ya existe un usuario con documento {doc}."
        self.usuarios[doc] = usuario
        return f"Usuario '{usuario.nombre}' registrado con documento {doc}."

    # ---------- Operaciones de préstamo ----------
    def registrar_prestamo(self, documento, codigo_equipo, observaciones=""):
        if documento not in self.usuarios:
            return f"No existe el usuario con documento {documento}."
        if codigo_equipo not in self.equipos:
            return f"No existe el equipo con código {codigo_equipo}."

        equipo = self.equipos[codigo_equipo]
        usuario = self.usuarios[documento]

        if not equipo.esta_disponible():
            return f"El equipo '{equipo.nombre}' no está disponible."

        equipo.marcar_prestado()
        usuario.agregar_prestamo(codigo_equipo)
        prestamo = Prestamo(documento, codigo_equipo, observaciones)
        self.prestamos.append(prestamo)
        return (
            f"Préstamo #{prestamo.id} registrado: "
            f"{usuario.nombre} -> {equipo.nombre}."
        )

    def devolver_prestamo(self, id_prestamo, estado_devolucion="Bueno"):
        prestamo = self._buscar_prestamo(id_prestamo)
        if prestamo is None:
            return f"No existe préstamo con id {id_prestamo}."
        if not prestamo.esta_activo():
            return f"El préstamo #{id_prestamo} ya fue devuelto."

        equipo = self.equipos[prestamo.codigo_equipo]
        usuario = self.usuarios[prestamo.documento_usuario]

        prestamo.cerrar()
        equipo.marcar_disponible()
        equipo.actualizar_estado(estado_devolucion)
        usuario.quitar_prestamo(prestamo.codigo_equipo)
        return (
            f"Préstamo #{id_prestamo} devuelto. "
            f"Equipo '{equipo.nombre}' reportado como '{estado_devolucion}'."
        )

    def modificar_observaciones(self, id_prestamo, nuevas_observaciones):
        prestamo = self._buscar_prestamo(id_prestamo)
        if prestamo is None:
            return f"No existe préstamo con id {id_prestamo}."
        prestamo.observaciones = nuevas_observaciones
        return f"Observaciones del préstamo #{id_prestamo} actualizadas."

    # ---------- Consultas ----------
    def _buscar_prestamo(self, id_prestamo):
        for p in self.prestamos:
            if p.id == id_prestamo:
                return p
        return None

    def listar_equipos(self):
        if not self.equipos:
            return "No hay equipos registrados."
        return "\n".join(e.ficha() for e in self.equipos.values())

    def listar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."
        return "\n".join(u.ficha() for u in self.usuarios.values())

    def listar_prestamos(self, solo_activos=False):
        datos = [p for p in self.prestamos if (not solo_activos or p.esta_activo())]
        if not datos:
            return "No hay préstamos que mostrar."
        return "\n".join(p.ficha() for p in datos)

    def consultar_prestamos_de_usuario(self, documento):
        if documento not in self.usuarios:
            return f"No existe el usuario con documento {documento}."
        usuario = self.usuarios[documento]
        codigos = usuario.obtener_prestamos_activos()
        if not codigos:
            return f"{usuario.nombre} no tiene préstamos activos."
        detalle = []
        for cod in codigos:
            equipo = self.equipos.get(cod)
            if equipo:
                detalle.append(f"- {equipo.ficha()}")
        return f"Préstamos activos de {usuario.nombre}:\n" + "\n".join(detalle)
