# Contribuir

Este sustrato está construido para recibir propuestas reales de otros conglomerados de
producto, no solo del equipo que lo mantiene directamente. El proceso descrito a
continuación no es hipotético — es la ruta exacta que siguió una contribución real,
desde la construcción de un producto específico de dominio hasta ocho componentes que
ahora están documentados en la [biblioteca de componentes](/components/chip-row/usage).

## Dos vías de entrada

**Estás construyendo algo específico de un dominio y crees que parte de ello es
genérico.** Esta es la vía habitual — un equipo de producto (GIS, BIM, el motor de la
wiki, o un futuro conglomerado) construye interfaz para su propio dominio, detecta un
patrón que no es específico del dominio en absoluto, y lo propone para el sustrato
compartido. El ejemplo desarrollado a continuación sigue exactamente esta vía.

**Quieres cambiar un token o componente existente.** Abre un issue en
[GitHub](https://github.com/pointsav/pointsav-design-system) con la etiqueta `design`,
incluyendo una captura de pantalla y el nombre del componente o token afectado. Los
cambios de tokens requieren específicamente una co-firma adicional del mantenedor
antes de poder integrarse — ver la nota al respecto más abajo.

## Proceso, desarrollado a partir de un ejemplo real

Entre abril y mayo de 2026, el equipo de producto BIM estaba a mitad de la
construcción de su propia interfaz de dominio AEC. En el camino, había reunido nueve
patrones de componentes. Algunos eran genuinamente específicos de BIM —
un visor 3D, un navegador de árbol espacial, un panel de propiedades IFC. Otros no
eran específicos del dominio en absoluto: un bloque de código con copiar al
portapapeles, una fila de chips semántica, una barra lateral categorizada. El
equipo propuso el segundo grupo de vuelta a este sustrato.

**Paso 1 — redactar un borrador, no solo pegar código.** La propuesta no fue un pull
request de marcado en bruto. Fue un borrador `DESIGN-RESEARCH` —
`design-generic-components-index.md` — que nombraba cada componente candidato, su
forma estructural, y una pregunta genuinamente abierta: ¿deberían las versiones
genéricas heredar la convención de nomenclatura de clases propia de BIM, `.bim-*`, o
usar el prefijo `ps-*` ya existente en este sustrato?

**Paso 2 — enviarlo, dirigido a este sustrato.** La propuesta se envió a través del
pipeline estándar de contribución de diseño y quedó en espera. Nada se movió
automáticamente hasta que un mantenedor aquí la recogió.

**Paso 3 — la revisión resuelve nomenclatura, alcance y licenciamiento — de forma
explícita y por escrito.** Esta es la parte que vale la pena leer con detenimiento,
porque el razonamiento es lo que hace que una revisión sea real y no un mero sello de
aprobación:

- *Nomenclatura*: ganó `ps-*`, no `.bim-*` — porque una superficie de inquilino que
  consume tanto componentes específicos de BIM como componentes genéricos necesita un
  vocabulario coherente. Las clases internas propias de BIM se
  mantienen como `.bim-*` en el propio código base de BIM; solo las formas genéricas
  que cruzan hacia este sustrato adoptan el prefijo `ps-*`.
- *Alcance — qué cruzó realmente*: ocho de los nueve patrones propuestos fueron
  aceptados como stubs genéricos (`chip-row`, `code-block-with-copy`,
  `edit-on-github-link`, `empty-state-card`, `machine-surface-footer`,
  `preview-frame`, `sidebar-accordion`, `tab-bar-disclosure` — los mismos ocho ya
  documentados por completo en esta biblioteca). El noveno, un patrón de breadcrumb,
  **no** se añadió. Este sustrato ya incluía un componente `breadcrumb` equivalente,
  así que la revisión indicó al equipo de BIM que reutilizara ese en lugar
  de bifurcar un casi-duplicado. Otros siete patrones (un visor 3D, un árbol
  espacial, un panel de propiedades, y cuatro componentes más específicos de AEC)
  fueron explícitamente **excluidos** por ser demasiado específicos del dominio para
  un sustrato genérico. Esos permanecieron en el propio código base de BIM en
  lugar de cruzar hacia la biblioteca genérica.
- *Licenciamiento, remitido en lugar de decidido unilateralmente*: el mismo ciclo de
  revisión reveló un hallazgo de licenciamiento. Un componente específico de BIM —
  un visor 3D construido sobre una biblioteca de renderizado con licencia AGPL-3.0 —
  cambia la postura de licenciamiento de cualquier aplicación que lo distribuya. Este
  sustrato no toma decisiones de licenciamiento en nombre de otro equipo. El
  hallazgo se documentó por escrito y se remitió para revisión de gobernanza en
  lugar de actuarse localmente.

**Paso 4 — la aceptación es un registro de decisión confirmado y rastreado en git**,
no un acuerdo verbal. Dos archivos de investigación recogen el razonamiento completo:
uno registra la aceptación estructural (convenciones de rutas, taxonomía de tokens,
qué queda dentro y qué queda fuera), el otro registra el propio flujo de retorno de
los componentes (resolución de nomenclatura, la lista de aceptados/rechazados, y lo
que a cada stub aún le falta antes de ser una receta completa). Ambos residen en
`research/` dentro de este vault, legibles por cualquiera — humano o agente de IA —
que decida construir sobre este patrón.

**Paso 5 — un stub se convierte en un componente real con el tiempo, no de una sola
vez.** Llegar como un stub de `recipe.json` es el comienzo, no el final. Cada uno de
esos ocho componentes necesitó un pase de seguimiento — `usage.md`, `style.md`,
`code.md`, `accessibility.md` — escrito contra la estructura real del stub, señalando
con honestidad dónde la receta todavía no está a la altura de su nombre (uno de los
ocho sigue siendo una lista estática, no un acordeón verdadero, y así lo indica en su
propia página de uso en lugar de aparentar lo contrario).

## Qué significa esto si estás proponiendo algo

- Escribe *por qué* un patrón es genérico, no solo que existe — la revisión necesita
  una razón para decir que sí, y una razón para decir que no a las partes que
  deberían seguir siendo específicas del dominio.
- Espera que las preguntas de nomenclatura y alcance se resuelvan por escrito, con
  una justificación explícita — no que se aplacen en silencio ni que las decida
  quien primero escriba más código.
- Si tu propuesta afecta al licenciamiento (una dependencia con una licencia vírica,
  un token que cruza un límite de cumplimiento normativo), dilo explícitamente en
  lugar de dejar que salga a la luz más adelante.
- Un stub es un punto de partida honesto. No prometas en la documentación propia de
  un componente un comportamiento completo que la receta todavía no implementa
  realmente.

## Los cambios de tokens necesitan una co-firma

Cualquier cambio a `tokens/dtcg-bundle.json` o a un archivo de tokens requiere una
co-firma adicional del mantenedor antes de poder confirmarse
aquí — esta es una barrera más estricta que la de las propuestas de componentes, ya
que un cambio de token puede desplazar silenciosamente el color, el espaciado o la
tipografía en todas las superficies consumidoras a la vez.
