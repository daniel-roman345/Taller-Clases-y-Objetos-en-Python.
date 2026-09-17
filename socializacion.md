# Socialización – GA1-220501093-04-AA1-EV04

**Aprendiz:** Daniel Salas Román
**Duración estimada:** 3 minutos
**Formato:** exposición oral acompañada de la demostración en consola

---

## 1. Presentación (20 s)

> "Buen día. Mi nombre es Daniel Salas Román. Voy a presentar el desarrollo de la evidencia GA1‑220501093‑04‑AA1‑EV04 sobre Fundamentos de Python: Clases, Objetos y Encapsulación. El repositorio contiene cuatro bloques de trabajo: los ejemplos replicados del material, el taller de Clases y Objetos, el taller de Encapsulación y el reto integrador del Sistema de Préstamos de Equipos."

## 2. Replicación de ejemplos del material (30 s)

> "En la carpeta `ejemplos_material` repliqué cuatro ejemplos del material didáctico: una clase básica `Persona`, una clase `Vehiculo` para ilustrar atributos y métodos, una clase `Estudiante` para explicar el constructor `__init__` y una clase `CuentaBancaria` para demostrar la encapsulación con atributos privados y getters/setters."

## 3. Taller de Clases y Objetos (30 s)

> "En la carpeta `taller_clases_objetos` desarrollé tres proyectos independientes: `Libro`, `Persona` y `Producto`. Cada uno define atributos propios, un constructor y métodos que modifican y consultan su estado (prestar/devolver, cumplir años, vender/reabastecer). El funcionamiento se valida en consola con `python`."

## 4. Taller de Encapsulación (30 s)

> "En `taller_encapsulacion` implementé tres casos: `CuentaBancaria` con saldo y clave privados, `Empleado` con salario y evaluación encapsulados, y `Estudiante` con lista de notas privada. En todos los casos los atributos sensibles usan doble guion bajo y solo pueden modificarse a través de métodos que validan la operación."

## 5. Reto integrador: Sistema de Préstamos de Equipos (60 s)

> "El reto integra todo lo aprendido. En `reto_sistema_prestamos` diseñé cuatro clases:
>
> - `Equipo`: encapsula la disponibilidad y el estado físico.
> - `Usuario`: encapsula el documento y la lista de préstamos activos.
> - `Prestamo`: encapsula el estado activo y la fecha de devolución.
> - `SistemaPrestamos`: fachada que orquesta todo mediante diccionarios (`equipos`, `usuarios`) y una lista (`prestamos`).
>
> El sistema permite **registrar** usuarios, equipos y préstamos, **consultar** el inventario y los préstamos activos por usuario, **modificar** observaciones y **devolver** equipos actualizando su estado. Todos los casos de error (usuario o equipo inexistente, equipo no disponible, préstamo ya devuelto) están controlados."

## 6. Reflexión y aprendizajes (20 s)

> "El reto principal fue decidir qué atributos debían ser privados y qué operaciones debían pasar por métodos validadores. La encapsulación se volvió tangible cuando comprobé que el sistema no permite marcar como prestado un equipo que ya lo estaba ni devolver un préstamo dos veces. Con esto reforcé el modelado orientado a objetos y el uso de colecciones para organizar la información."

## 7. Cierre (10 s)

> "El código completo está publicado en GitHub, con su README explicativo y ejemplos de ejecución. Gracias por su atención."

---

## Guion de demostración en vivo (para acompañar la exposición)

```bash
# 1. Ejemplos del material
python3 ejemplos_material/ejemplo_04_encapsulacion.py

# 2. Un caso del taller de Clases y Objetos
python3 taller_clases_objetos/caso1_libro.py

# 3. Un caso del taller de Encapsulación
python3 taller_encapsulacion/caso1_cuenta_bancaria.py

# 4. Reto integrador completo
cd reto_sistema_prestamos
python3 main.py
```
