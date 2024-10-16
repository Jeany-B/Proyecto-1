#import "templates/icci-temp.typ": conf

#show: doc => conf(
  title: [
    Plan de Proyecto
  ],
  theme: [
    "Proyecto Ada"
  ],
  authors: (
    "Jeany Aravena",
    "Tiara Canepa",
    "Brandon Pizarro",
    "Catalina Ramírez"
  ),
  course: [Proyecto 1],
  professor: [Humberto Pizarro],
  institution_logo: "/images/int_logo.png",
  faculty_logo: "/images/faculty_logo.png",
  department_logo: "/images/dept_logo.png",
  doc,
)

#show "Proyecto Ada": it => strong(it)

// Body

= Panorama General

== Introducción

Este documento detalla la planificación a largo plazo del Proyecto Ada, que
consiste en la fabricación de un robot con el kit LEGO Ev3 Mindstorms capaz de
ser controlado manualmente y rescatar objetos de tamaño pequeño. La programación
del robot se hará en el lenguaje de programación _Python_ mediante la librería
`ev3dev2`.

== Objetivos

=== Objetivo general

El objetivo general define la meta del proyecto, lo que se espera una vez
termine el plazo definido.

#align(center, text(size: 15pt)[_Diseñar y construir un robot funcional \ capaz de
    movimiento controlado y rescate de objetos pequeños_])

\
=== Objetivos específicos

Los objetivos específicos definen el camino y las ramas que se tomarán para
llegar a la meta. Algunos de los objetivos pueden ser modificados durante la
ejecución del proyecto, pero es importante mantener cohesión entre ellos.

- Planificar el proyecto: roles, calendario y metas.
- Construir un modelo usando el kit LEGO Ev3 Mindstorms.
- Lograr la conexión inalámbrica con el robot.
- Programar las funcionalidades del robot.
- Agregar varios dispositivos para su control a distancia.
- Crear una interfaz para uso común.
- Adoptar satisfactoriamente la metodología AGIL.

== Restricciones

La ejecución del proyecto tiene ciertas limitantes a considerar, por lo que la
planificación deberá adecuarse a ellas. Algunas de las restricciones del
proyecto son:

- La disponibilidad de las piezas está definida por el stock de la universidad.
- El lenguaje de programación del robot será _Python_.
- El tiempo límite del proyecto será de un semestre (4-5 meses).
- Solo se podrá trabajar con el robot dentro de la universidad.
- La plataforma de colaboración del equipo será Redmine y GitHub.

== Entregables

La organización y registro del proyecto se realizará mediante documentos
periódicos publicados en la plataforma Redmine.

- Bitácoras de avance cada semana.
- Calendario del proyecto.
- Informe de planificación del proyecto.
- Presentación de planificación del proyecto.

= Organización del Personal

== Descripción de los roles

Dentro del equipo se deben cubrir ciertos roles para la distribución de
trabajos y carga del proyecto. Estos roles son:

1. *Jefe de grupo*: Se encarga de organizar las tareas del equipo.
2. *Ensamblador*: Se encarga de la construcción y diseño del robot.
3. *Programador*: Se encarga de implementar y mantener la comunicación con 
   el robot y las funcionalidades que necesite.
4. *Diseñador*: Se encarga de diseñar las partes gráficas del proyecto, como el
   logotipo y las presentaciones.
5. *Documentador*: Se encarga de mantener actualizada la información del
   proyecto en la plataforma Redmine.

== Personal asignado

1. *Jefe de grupo*: Tiara Canepa
2. *Ensamblador*: Brandon Pizarro, Catalina Ramírez
3. *Programador*: Jeany Aravena, Tiara Canepa
4. *Documentador*: Brandon Pizarro, Catalina Ramírez
5. *Diseñador*: Brandon Pizarro, Jeany Aravena

== Mecanismos de comunicación

Para la comunicación entre los integrantes del equipo se utilizará la aplicación
_WhatsApp_ en donde se realizará la coordinación de las actividades y los
horarios de cada miembro. Otras posibles opciones a considerar dada la necesidad
serán _Discord_ y la misma plataforma _Redmine_.

= Planificación del Proyecto

== Actividades

== Calendario

La planificación del proyecto se realiza activamente mediante la repartición de
actividades durante un tiempo estimado. El calendario, visto en la @gantt, se
describe en una carta gantt.

#figure(
    caption: "Calendario de actividades del proyecto",
    supplement: "Figura",
    image("images/carta-gantt1.png")
) <gantt>

== Gestión de riesgos

En la duración del proyecto pueden ocurrir inesperada e inevitablemente
situaciones que pongan en peligro su avance. Para remediar estos casos se
realiza un plan de acción dependiendo de su gravedad:

1. *Daño catastrófico*: El proyecto puede detenerse indefinidamente o incluso
   ser cancelado; las medidas a tomar deben ser eficientes y ejecutadas de forma
   inmediata.
2. *Daño crítico*: El proyecto puede retroceder en su avance o detenerse por
   cantidades considerables de tiempo; las medidas a tomar deben ejecutarse lo
   antes posible para evitar ramificaciones.
3. *Daño circunstancial*: El proyecto puede ser pausado o llevado por un camino
   no importante; las medidas a tomar tienen baja prioridad, pero deberían
   ejecutarse más temprano que tarde.
4. *Daño irrelevante*: El proyecto puede presentar pequeños obstáculos que no
   necesariamente detienen su avance; las medidas a tomar no siempre son
   necesarias y deberían priorizarse otras situaciones.

#figure(
    align(center, table(
        columns: 4,
        inset: (x: 6pt, y: 10pt),
        [*Riesgo*], [*Probabilidad de Ocurrencia*], [*Nivel de Riesgo*],
        [*Medidas*],
        [Corrupción de la tarjeta SD], [10%], [Crítico], [Formatear y reinstalar
            el sistema del Ev3, recurrir a respaldos de archivos],
        [Descarga de la batería del Ev3], [70%], [Circunstancial], [Conectar el
            Ev3 a una fuente de poder],
        [Diseño incompatible con las necesidades], [60%], [Catastrófico], [Volver a
            pensar en el diseño del robot y retroceder a un estado compatible],
        [Error en el código], [90%], [Crítico], [Arreglar los bugs del código;
            volver a un estado anterior si es necesario],
        [Ausencia inesperada de algún integrante], [20%], [Irrelevante],
            [Repartir la responsabilidad del miembro faltante],
        [Piezas faltantes], [60%], [Circunstancial], [Pedir las piezas si es que
            quedan en stock; en caso contrario buscar diseño alternativo],
        [Desarme accidental considerable del robot], [10%], [Catastrófico],
            [Intentar volver al diseño actual mediante material fotográfico y el
            manual],
        [Cambio de horario en horas disponibles], [20%], [Crítico], [Reagendar
            las actividades del horario; considerar horas extra],
        [Fallo de los dispositivos de los integrantes], [5%], [Catastrófico],
            [Recurrir a equipo prestado, contabilizar los daños; si es posible
            reponer dispositivos],
        [Problemas en la conexión SSH], [60%], [Circunstancial], [Buscar el
            origen del problema; si toma mucho tiempo, recurrir a ejecución
            directamente en el brick]
    ))
)

= Planificación de los Recursos

== Hardware

El hardware son los dispositivos y accesorios físicos necesarios para la
realización del proyecto.

- Kit LEGO Ev3 Mindstorms
- Micro SD para el almacenamiento del robot
- Notebooks para la programación y búsqueda de información
- Adaptador Wi-Fi
- Control a distancia

== Software

El software son los programas y sistemas que se utilizarán para la realización
del proyecto.

- Editores Visual Studio Code y Neovim
- WhatsApp
- Sistemas operativos Windows y Linux (Arch)
- Canva
- SSH

== Estimación de costos

Las piezas de hardware a utilizar durante la realización del proyecto tienen los
siguientes costos:

#figure(
    supplement: "Tabla",
    align(center, table(
        columns: 2,
        inset: (x: 40pt, y: 7pt),
        align: center,
        [*Producto*], [*Precio*],
        [Kit LEGO Ev3 Mindstorms], [\$ 750,000],
        [Set de Expansión LEGO Ev3], [\$ 250,000],
        [Control PS3 DualShock 3], [\$ 30,000],
        [Micro SD 8 GB], [\$ 5,000],
        [Adaptador Wi-Fi USB], [\$ 10,000],
        [Notebook Lenovo V14 G3], [\$ 300,000],
        [Notebook Acer], [\$ 900,000],
        [Notebook ZenBook 14x Oled], [\$ 600,000],
        [Notebook Lenovo Thinkpad E14], [\$ 500,000],
        [Tablet Samsung], [\$ 300,000],
        [*Total*], [\$ 3,645,000]
))) <tb-hardware-prices>

\
El software a utilizar durante la duración del proyecto tiene principalmente
características de acceso simple; gratuito, como Visual Studio Code, o de código
abierto, como Neovim, SSH o los sistemas Linux. Si bien el sistema operativo
Windows requiere una licencia pagada, este costo está incluido en los productos
de la @tb-hardware-prices. Por esto, no hay costo por
software.

También se consideran los sueldos por rol:

\
#align(center, table(
    columns: 4,
    align: center,
    inset: (x: 20pt, y: 7pt),
    [*Rol*], [*Horas*], [*Precio/Hora*], [*Sueldo Semestral*],
    [Jefe de Grupo], [72], [\$ 35,000], [\$ 2,520,000],
    [Ensamblador], [72], [\$ 32,000], [\$ 2,304,000],
    [Documentador], [72], [\$ 28,000], [\$ 2,016,000],
    [Programador], [72], [\$ 30,000], [\$ 2,160,000],
    [Diseñador], [72], [\$ 30,000], [\$ 2,160,000],
    [*Total*], [-], [-], [\$ 8,890,000]
))

\
En total se obtiene la siguiente estimación de costos:

#align(center, table(
    columns: 2,
    inset: (x: 40pt, y: 7pt),
    [*Tipo*], [*Costo Total*],
    [Hardware], [\$ 3,645,000],
    [Sueldos], [\$ 8,890,000],
    [*Total*], [\$ 12,535,000]
))

= Conclusión

La exitosa realización del proyecto dependerá de seguir a cabalidad las
proyecciones registradas en este informe. Los plazos definidos y los roles
asignados son el punto de partida de un buen producto, así que el equipo se
muestra determinado a tener los mejores resultados posibles.

= Referencias

- #link("https://ev3dev.org")[Página principal de ev3dev]
- #link("https://github.com/ev3dev/ev3dev-lang-python")[Repositorio de la
    librería ev3dev2 en Python]
- #link("https://ev3dev-lang.readthedocs.io")[Referencia y documentación de la
    librería ev3dev2 en Python]
