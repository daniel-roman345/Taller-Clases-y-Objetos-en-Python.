# GA1-220501093-04-AA1-EV04
## Fundamentos de Python: Clases, Objetos y Encapsulación

**Autor:** Daniel Salas Román
**Programa:** Análisis y Desarrollo de Software (SENA)
**Actividad:** GA1-220501093-04-AA1-EV04

---

## 1. Descripción del proyecto

Este repositorio contiene la evidencia completa para la actividad
GA1-220501093-04-AA1-EV04. Se desarrollaron **cuatro bloques de trabajo**
que cubren la totalidad de los requerimientos de la rúbrica:

| Bloque | Carpeta | Peso rúbrica |
|--------|---------|--------------|
| Replicación de ejemplos del material didáctico | `ejemplos_material/` | 15% |
| Taller de Clases y Objetos (3 casos) | `taller_clases_objetos/` | 25% |
| Taller de Encapsulación (3 casos) | `taller_encapsulacion/` | — |
| Reto integrador: Sistema de Préstamos de Equipos | `reto_sistema_prestamos/` | 30% |
| Claridad, legibilidad y organización del código | (todo el repo) | 10% |
| Calidad del README.md | Este archivo | 10% |
| Argumentación y defensa (socialización) | `socializacion.md` | 10% |

---

## 2. Estructura del repositorio

```
Taller-Clases-y-Objetos-en-Python/
├── README.md
├── socializacion.md
├── capturas/                             # Capturas de consola
├── ejemplos_material/                    # Replicación del material
│   ├── ejemplo_01_clase_basica.py
│   ├── ejemplo_02_atributos_metodos.py
│   ├── ejemplo_03_constructor.py
│   └── ejemplo_04_encapsulacion.py
├── taller_clases_objetos/                # Taller 1: Clases y Objetos
│   ├── caso1_libro.py
│   ├── caso2_persona.py
│   └── caso3_producto.py
├── taller_encapsulacion/                 # Taller 2: Encapsulación
│   ├── caso1_cuenta_bancaria.py
│   ├── caso2_empleado.py
│   └── caso3_estudiante.py
└── reto_sistema_prestamos/               # Reto integrador (POO completo)
    ├── main.py
    ├── equipo.py
    ├── usuario.py
    ├── prestamo.py
    └── sistema_prestamos.py
```

---

## 3. Diseño de clases y encapsulación

### 3.1 Ejemplos del material didáctico (`ejemplos_material/`)

Se replicaron los cuatro ejemplos base del material:

- **`Persona`**: clase mínima con constructor y método `saludar()`.
- **`Vehiculo`**: atributos y métodos para encender/apagar/describir.
- **`Estudiante`**: uso del constructor `__init__` con lista de notas.
- **`CuentaBancaria`**: encapsulación con `__saldo` privado y getters/setters
  con validaciones.

### 3.2 Taller de Clases y Objetos (`taller_clases_objetos/`)

Cada caso es un proyecto independiente que se ejecuta por sí solo y valida
su funcionamiento imprimiendo el estado antes y después de las operaciones:

- **`Libro`** — títulos y préstamos de biblioteca (`prestar`, `devolver`).
- **`Persona`** — datos personales (`presentarse`, `cumplir_años`, `es_mayor_de_edad`).
- **`Producto`** — inventario simple (`vender`, `reabastecer`).

### 3.3 Taller de Encapsulación (`taller_encapsulacion/`)

Todos los casos siguen el mismo patrón: atributos sensibles marcados con
doble guion bajo (`__atributo`) y expuestos únicamente mediante métodos
que validan las operaciones.

- **`CuentaBancaria`** — `__saldo` y `__clave` privados; retiros exigen la clave.
- **`Empleado`** — `__salario` y `__evaluacion` privados con validaciones de
  rango (aumento 1–100%, evaluación 0–100).
- **`Estudiante`** — `__notas` como lista privada; el getter retorna una
  copia para evitar mutaciones externas; solo se aceptan notas entre 0 y 5.

### 3.4 Reto integrador: Sistema de Préstamos de Equipos

Diseño orientado a objetos con **cuatro clases**:

#### `Equipo` (`reto_sistema_prestamos/equipo.py`)
- Atributos públicos: `codigo`, `nombre`, `tipo`, `marca`.
- **Atributos encapsulados**: `__disponible`, `__estado`.
- Métodos: `esta_disponible`, `obtener_estado`, `marcar_prestado`,
  `marcar_disponible`, `actualizar_estado`, `ficha`.

#### `Usuario` (`reto_sistema_prestamos/usuario.py`)
- **Atributos encapsulados**: `__documento`, `__prestamos_activos`.
- Métodos: `obtener_documento`, `obtener_prestamos_activos`,
  `agregar_prestamo`, `quitar_prestamo`, `ficha`.

#### `Prestamo` (`reto_sistema_prestamos/prestamo.py`)
- **Atributos encapsulados**: `__activo`, `__fecha_devolucion`.
- Métodos: `esta_activo`, `obtener_fecha_devolucion`, `cerrar`, `ficha`.

#### `SistemaPrestamos` (`reto_sistema_prestamos/sistema_prestamos.py`)
Fachada que centraliza toda la lógica y usa **colecciones**:
- `self.equipos: dict[str, Equipo]` — acceso rápido por código.
- `self.usuarios: dict[str, Usuario]` — acceso rápido por documento.
- `self.prestamos: list[Prestamo]` — histórico completo.

Operaciones (rúbrica del reto):
- **Registrar**: `registrar_equipo`, `registrar_usuario`, `registrar_prestamo`.
- **Consultar**: `listar_equipos`, `listar_usuarios`, `listar_prestamos`,
  `consultar_prestamos_de_usuario`.
- **Modificar**: `modificar_observaciones`.
- **Devolver**: `devolver_prestamo`.

---

## 4. Cómo ejecutar

Se requiere **Python 3.10+**.

### 4.1 Ejemplos del material

```bash
python3 ejemplos_material/ejemplo_01_clase_basica.py
python3 ejemplos_material/ejemplo_02_atributos_metodos.py
python3 ejemplos_material/ejemplo_03_constructor.py
python3 ejemplos_material/ejemplo_04_encapsulacion.py
```

### 4.2 Taller de Clases y Objetos

```bash
python3 taller_clases_objetos/caso1_libro.py
python3 taller_clases_objetos/caso2_persona.py
python3 taller_clases_objetos/caso3_producto.py
```

### 4.3 Taller de Encapsulación

```bash
python3 taller_encapsulacion/caso1_cuenta_bancaria.py
python3 taller_encapsulacion/caso2_empleado.py
python3 taller_encapsulacion/caso3_estudiante.py
```

### 4.4 Reto integrador

```bash
cd reto_sistema_prestamos
python3 main.py
```

---

## 5. Ejemplos de ejecución (salidas reales en consola)

### 5.1 Encapsulación — `ejemplo_04_encapsulacion.py`

```text
=== EJEMPLO 4: ENCAPSULACIÓN ===
Titular: Daniel Salas
Saldo inicial: $1000
Depósito exitoso. Nuevo saldo: $1500
Retiro exitoso. Nuevo saldo: $1300
Fondos insuficientes.
Saldo final: $1300
Acceso directo bloqueado por encapsulación: 'CuentaBancaria' object has no attribute '__saldo'
```

### 5.2 Taller Clases y Objetos — `caso1_libro.py`

```text
=== INFORMACIÓN INICIAL ===
Título: Don Quijote de la Mancha
Autor: Miguel de Cervantes
Páginas: 863
Estado: Disponible

=== PRÉSTAMOS ===
El libro "Don Quijote de la Mancha" ha sido prestado.

=== INTENTO DE PRESTAR DE NUEVO ===
El libro "Don Quijote de la Mancha" no está disponible.

=== DEVOLUCIÓN ===
El libro "Don Quijote de la Mancha" ha sido devuelto.
```

### 5.3 Taller Encapsulación — `caso1_cuenta_bancaria.py`

```text
=== TALLER ENCAPSULACIÓN - CASO 1: CUENTA BANCARIA ===
Saldo actual de Daniel Salas: $500000
Clave incorrecta. Acceso denegado.

=== DEPÓSITOS Y RETIROS ===
Depósito exitoso. Nuevo saldo: $650000
Retiro exitoso. Nuevo saldo: $450000
Fondos insuficientes.
Clave incorrecta. No se puede retirar.

=== CAMBIO DE CLAVE ===
Clave actualizada correctamente.
```

### 5.4 Reto integrador — `main.py`

```text
============================================================
5. REGISTRO DE PRÉSTAMOS
============================================================
Préstamo #1 registrado: Daniel Salas -> Portátil Lenovo.
Préstamo #2 registrado: Laura Gómez -> Videobeam Epson.
Préstamo #3 registrado: Carlos Ríos -> Portátil HP.
No existe el usuario con documento 9999999999.
No existe el equipo con código E999.
El equipo 'Portátil HP' no está disponible.

============================================================
9. DEVOLUCIÓN DE EQUIPOS
============================================================
Préstamo #1 devuelto. Equipo 'Portátil Lenovo' reportado como 'Bueno'.
Préstamo #2 devuelto. Equipo 'Videobeam Epson' reportado como 'Regular'.
El préstamo #1 ya fue devuelto.
No existe préstamo con id 99.

============================================================
10. ESTADO FINAL DEL INVENTARIO
============================================================
[E001] Portátil Lenovo (Computador - Lenovo) | Estado: Bueno | Disponible
[E002] Portátil HP (Computador - HP) | Estado: Bueno | Prestado
[E003] Videobeam Epson (Videobeam - Epson) | Estado: Regular | Disponible
[E004] Tablet Samsung (Tablet - Samsung) | Estado: Bueno | Disponible
```

> Las capturas completas de la ejecución en consola se encuentran en la
> carpeta `capturas/` para incluirlas en la socialización.

---

## 6. Reflexión personal sobre aprendizajes y retos superados

Durante la realización de esta actividad afiancé los siguientes conceptos:

1. **Diferencia clara entre clase y objeto**. Una clase es la plantilla; un
   objeto es una instancia con estado propio. Trabajarlo en el `Libro`,
   la `Persona` y el `Producto` me permitió ver que el mismo código puede
   dar vida a múltiples entidades con estados independientes.

2. **Importancia del constructor `__init__`**. Comprendí que el constructor
   no es una función más: garantiza que un objeto **nace válido** con
   todos sus atributos inicializados, y me permite forzar reglas desde el
   primer instante (por ejemplo, que un `Equipo` siempre nazca con estado
   "Bueno" y disponible).

3. **Encapsulación como mecanismo de protección**. El mayor reto conceptual
   fue decidir qué atributos debían ser privados. Al implementar el
   `SistemaPrestamos` entendí que la encapsulación no es solo "esconder
   variables": es garantizar que el estado interno no pueda quedar
   inconsistente. Por ejemplo, un equipo nunca puede quedar "disponible y
   prestado a la vez" porque la única forma de cambiar `__disponible` es a
   través de `marcar_prestado()` o `marcar_disponible()`.

4. **Colecciones para organizar la información**. Elegir entre listas y
   diccionarios se volvió una decisión de diseño: los diccionarios de
   equipos y usuarios permiten buscar en O(1) por su clave natural
   (código, documento), mientras que la lista de préstamos guarda el
   histórico ordenado cronológicamente.

5. **Separación en módulos**. Al partir el reto en cuatro archivos
   (`equipo.py`, `usuario.py`, `prestamo.py`, `sistema_prestamos.py`) el
   proyecto se volvió más legible y mantenible. Este es el mismo patrón
   que usan proyectos reales.

**Reto superado**: al principio permitía que `SistemaPrestamos` modificara
directamente `equipo.disponible`, lo que rompía la encapsulación. Corrigí
el diseño para que toda modificación pasara por los métodos públicos, y
así el sistema completo respeta el principio de "hablar solo por la
interfaz pública".

---

## 7. Socialización

El guion completo de la socialización (máx. 3 minutos) está en
[`socializacion.md`](./socializacion.md), incluyendo el orden de la
exposición, los tiempos por bloque y los comandos que se ejecutan en vivo
para demostrar el funcionamiento del código.

---

## 8. Tecnologías utilizadas

- Python 3.11
- Visual Studio Code
- Git y GitHub

---

## 9. Materiales de apoyo consultados

- Documentación oficial de Python – Clases:
  https://docs.python.org/es/3/tutorial/classes.html
- Real Python – Object-Oriented Programming (OOP) in Python:
  https://realpython.com/python3-object-oriented-programming/
- W3Schools – Python Classes and Objects:
  https://www.w3schools.com/python/python_classes.asp
