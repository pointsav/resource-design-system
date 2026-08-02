<div class="doc-header">
<span class="eyebrow">Componentes</span>
<div class="doc-header__badges">
<span class="badge">2 variantes</span>
<span class="badge badge--brand">Con tokens</span>
<span class="badge">Objetivo WCAG 2.2 AA</span>
</div>
<p class="doc-header__lead">Un grupo horizontal de chips de país que filtra los datos
del mapa y desplaza la vista (`flyTo`) a los límites del país seleccionado. El estado
por defecto es TODOS — sin filtro, vista mundial. La selección es única y exclusiva;
una variante de selección múltiple está planificada pero pendiente de su primer caso
de uso real.</p>
<div class="registry-note"><span>Renderizado desde</span> <code>components/country-filter-chips/recipe.json</code></div>
</div>

## Cuándo usar Country Filter Chips

Use Country Filter Chips cuando una superficie de mapa ofrece un conjunto
pequeño y fijo de ámbitos por país, y elegir uno debe hacer dos cosas a la
vez: filtrar los datos visibles del mapa a ese país y desplazar la vista
(`flyTo`) a los límites de ese país. La fila de chips siempre comienza con
un chip **TODOS** — la vista mundial predeterminada, sin filtro — de modo
que nunca existe un estado de filtro oculto que el visitante no pueda ver
o del que no pueda salir.

Este es un componente de la [línea de producto GIS](/products/gis/overview).
Implementación de referencia: en vivo en gis.woodfinegroup.com (v0.1.94).
Se combina de forma natural con [Map Side Drawer](/components/map-side-drawer/usage),
la otra mitad del patrón de interacción de mapas GIS ya en producción.

## Variantes

| Variante | Descripción |
|---|---|
| **Predeterminada** | Selección exclusiva (radiogroup). El uso actual en GIS. |
| **Selección múltiple** | Varios chips activos simultáneamente. `role="group"` + `aria-pressed` reemplaza a `radiogroup` + `aria-checked`. Decisión pendiente del primer caso de uso de selección múltiple — aún no construida. |

## Anatomía

- **Contenedor** — una fila flex (`.ps-country-chips`) con
  `role="radiogroup"` y un `aria-label` ("Filtrar por país"),
  que pasa a varias líneas cuando el conjunto de chips supera el ancho.
- **Chip TODOS** — el primero de la fila; el estado activo
  predeterminado, sin filtro aplicado.
- **Chips de país** — uno por país, representados con emoji de bandera
  más código ISO de país (🇺🇸 US, 🇨🇦 CA, 🇲🇽 MX, 🇪🇸 ES en la
  implementación de referencia). El emoji de bandera es complementario;
  el código ISO siempre se muestra como respaldo textual.

Cada chip es un `<button type="button">` con forma de píldora — 2.25rem
de alto con un radio de 1.125rem y una `min-height` de 44px.

## Comportamiento

### Selección

Exclusiva: activar un chip desactiva el anterior, filtra los datos del
mapa a ese país y desplaza la vista a los límites de ese país. Activar
**TODOS** limpia el filtro y regresa a la vista mundial. El chip
seleccionado señala su estado mediante fondo, borde *y* `aria-checked`
— nunca solo el color.

### Teclado

Tab enfoca el grupo; las teclas de flecha se mueven entre chips; Espacio
o Enter activa. El foco se indica con un contorno de 2px
`{semantic.interactive.focus-ring}` con un desplazamiento de 2px.

### Movimiento

El color de fondo y de borde transicionan durante
`{primitive.motion.duration.base}`; bajo `prefers-reduced-motion:
reduce` la transición se elimina por completo.

## Tokens

La receta consume seis tokens de la capa de tema y cuatro de la capa
primitiva — ver [tokens de tema](/tokens#theme) y
[tokens primitivos](/tokens#primitive):

| Token | Rol |
|---|---|
| `{semantic.surface.layer}` | Fondo de reposo del chip |
| `{semantic.surface.layer-hover}` | Fondo del chip al pasar el cursor |
| `{semantic.text.primary}` | Etiqueta del chip, en reposo |
| `{semantic.text.on-color}` | Etiqueta del chip, seleccionado |
| `{semantic.border.subtle}` | Borde del chip, en reposo |
| `{semantic.interactive.focus-ring}` | Contorno de foco |
| `{primitive.color.brand.blue.60}` | Fondo y borde cuando está seleccionado |
| `{primitive.space.1}` | Espacio entre chips |
| `{primitive.space.2}` | Relleno horizontal del chip |
| `{primitive.motion.duration.base}` | Transición de hover/selección |

## Accesibilidad

La receta tiene como objetivo WCAG 2.2 AA.

- **Semántica de radiogroup.** El contenedor lleva `role="radiogroup"`
  con un `aria-label`; cada chip lleva `role="radio"` y
  `aria-checked` — no `aria-pressed`, porque la selección es exclusiva.
  (La variante de selección múltiple planificada es donde `aria-pressed`
  tomaría su lugar.)
- **No solo el color.** El estado seleccionado se transmite mediante
  fondo, borde y `aria-checked` en conjunto.
- **Respaldo textual para las banderas.** El emoji de bandera es
  complementario; el código ISO siempre se muestra como texto, de modo
  que el chip sea legible donde los emoji de bandera no se rendericen.
- **Área táctil.** Cada chip tiene una altura mínima de 44px — la
  receta señala que esto cumple el nivel de tamaño de objetivo WCAG
  2.2 AAA, por encima del objetivo AA general del componente.
- **Visibilidad del foco.** `:focus-visible` dibuja un contorno de 2px
  `{semantic.interactive.focus-ring}` con un desplazamiento de 2px.

## Preguntas abiertas

- **oq-1 — Selección múltiple y el chip TODOS.** Cuando se active la
  variante de selección múltiple, ¿TODOS se deshabilita o actúa como
  "limpiar todo"? Decisión pendiente del primer caso de uso de
  selección múltiple.

Investigación relacionada: `dtcg-vault/research/zoom-tier-reveal-pattern.md`.

## Cuándo no usar

- No usar para listas de países largas o abiertas — la fila de chips
  es un conjunto pequeño y fijo de ámbitos, no un buscador. Más allá
  de un puñado de países, un patrón de selector o autocompletado
  encaja mejor.
- No usar para filtrado no exclusivo hoy. La variante en producción es
  un radiogroup; las selecciones simultáneas múltiples son la variante
  de selección múltiple pendiente, no algo para improvisar con la
  variante predeterminada.
- No usar fuera de un contexto de mapa. El contrato del componente
  vincula el filtrado con un cambio de vista `flyTo`; un filtro de
  tabla de datos simple no tiene una vista que desplazar.
