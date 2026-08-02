<div class="doc-header">
<span class="eyebrow">Componentes</span>
<div class="doc-header__badges">
<span class="badge">2 variantes</span>
<span class="badge badge--brand">Con tokens</span>
<span class="badge">Objetivo WCAG 2.2 AA</span>
</div>
<p class="doc-header__lead">Panel de información persistente en el lado derecho para
el detalle de características del mapa. Se desliza al hacer clic en una
característica; permanece visible mientras el mapa sigue siendo interactivo.
Sustituye al patrón de ventana emergente sobre el marcador, de modo que el mapa nunca
pierde su contexto por debajo.</p>
<div class="registry-note"><span>Renderizado desde</span> <code>components/map-side-drawer/recipe.json</code></div>
</div>

## Cuándo usar Map Side Drawer

Use Map Side Drawer para mostrar el detalle de una sola característica de mapa
seleccionada — un panel persistente en el lado derecho que se desliza al hacer clic
y permanece visible mientras el mapa subyacente sigue siendo interactivo. Sustituye
al patrón de ventana emergente sobre el marcador, que obliga al mapa a perder su
contexto cada vez que un visitante inspecciona una característica.

Implementación de referencia: en vivo en gis.woodfinegroup.com (v0.1.94).

## Variantes

| Variante | Descripción |
|---|---|
| **Predeterminada** | Detalle de una sola característica — el uso actual en producción para GIS. |
| **Comparación** | Panel dividido que muestra dos características lado a lado, para comparación de conglomerados federados. Decisión pendiente, aún no construida. |

## Anatomía

- **Encabezado** — distintivo de familia de marca, título de la característica,
  botón de cierre.
- **Lista de datos** — dirección, código NAICS, año de apertura (lista de
  definiciones: pares término/valor).
- **Contexto de conglomerado** (oculto por defecto) — aparece cuando la
  característica pertenece a un conglomerado comercial: ID del conglomerado,
  número de anclas, radio máximo.

## Comportamiento

Se desliza a 340px de ancho desde el borde de fin de línea, con una curva de
entrada de 250ms (se reduce a un simple desvanecimiento de opacidad bajo
`prefers-reduced-motion`). `role="complementary"` con un `aria-label` que
nombra el tipo de característica; `aria-modal="false"` ya que el mapa permanece
interactivo por debajo. Tab recorre el panel mientras está abierto; Escape lo
cierra y devuelve el foco al lienzo del mapa.

## Preguntas abiertas

- Si el panel debe expandirse a ancho completo por debajo de 640px o mantener
  su ancho de superposición de 340px en pantallas pequeñas — aún no decidido.
- El diseño exacto de la variante de comparación (dos columnas de panel frente
  a pantalla dividida con el mapa en medio) está pendiente del trabajo de la
  función de comparación de conglomerados.

## Cuándo no usar

Este es un panel de detalle de contexto de mapa, no un modal o barra lateral
genérico — para esos casos, vea los componentes Modal Dialog y TOC Sidebar
del sistema.
