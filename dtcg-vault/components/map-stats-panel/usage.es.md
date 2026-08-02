<div class="doc-header">
<span class="eyebrow">Componentes</span>
<div class="doc-header__badges">
<span class="badge">4 variantes</span>
<span class="badge badge--brand">Con tokens</span>
<span class="badge">Objetivo WCAG 2.2 AA</span>
</div>
<p class="doc-header__lead">Un panel flotante de visualización de datos que muestra
estadísticas agregadas de la vista de mapa filtrada actual. Siempre visible, se
actualiza de forma reactiva a medida que cambian los filtros — chips de país,
casillas de familia — y se ubica en la esquina superior derecha para nunca
colisionar con los controles de zoom del mapa.</p>
<div class="registry-note"><span>Renderizado desde</span> <code>components/map-stats-panel/recipe.json</code></div>
</div>

## Cuándo usar Map Stats Panel

Use Map Stats Panel para mantener siempre visible un resumen continuo de *qué
muestra el mapa actualmente*. A medida que un visitante acota el mapa con
filtros, los conteos del panel se recalculan en el mismo lugar — de modo que
la respuesta a "¿cuánto de los datos estoy viendo ahora mismo?" siempre está
en pantalla, sin necesidad de un clic.

Es un agregado de solo lectura para toda la vista filtrada. Para el detalle
de una sola característica seleccionada, use en su lugar
[Map Side Drawer](/components/map-side-drawer/usage) — ese panel responde
"cuéntame sobre *esta*", este panel responde "cuéntame sobre *todas* estas".

Implementación de referencia: en vivo en gis.woodfinegroup.com (v0.1.94).
Ambos componentes pertenecen a la línea de producto GIS — vea la
[visión general de GIS](/products/gis/overview) para cómo se combinan en
la superficie del mapa.

## Variantes

El sistema ofrece cuatro variantes de panel. Todas comparten la misma
cuadrícula de lista de definiciones; solo difieren en cuántas celdas de
estadística llevan y cómo se organizan esas celdas.

| Variante | Diseño | Usar para |
|---|---|---|
| **Predeterminada** | 4 celdas, cuadrícula 2×2 | El uso actual en GIS — Corredores, Anclas, Países y Calificación promedio de conglomerado. |
| **Compacta** | 2 celdas, horizontal | Paneles de estadísticas de un solo eje donde solo importan dos cifras. |
| **Ancha** | 6 celdas, cuadrícula 3×2 | Comparación de conglomerados federados, donde se muestran más dimensiones agregadas a la vez. |
| **Con minigráfico** | Cada celda lleva un pequeño minigráfico en línea | Uso de Fase 2 — contexto de tendencia junto a cada cifra. |

## Anatomía

El panel es un punto de referencia `<aside>` que envuelve una única lista
de definiciones:

- **Cuadrícula** (`.ps-map-stats__grid`) — una cuadrícula CSS de dos
  columnas de celdas de estadística.
- **Celda** (`.ps-map-stats__cell`) — un par `<dt>`/`<dd>` por estadística.
- **Etiqueta** (`.ps-map-stats__label`, el `<dt>`) — una micro-etiqueta en
  mayúsculas que nombra la cifra (p. ej. *Corredores*, *Anclas*, *Países*,
  *Calificación promedio de conglomerado*).
- **Valor** (`.ps-map-stats__value`, el `<dd>`) — la cifra misma, en tipo
  grande en negrita, con una transición de `color` para que un valor
  cambiado se lea como una actualización deliberada y no como un parpadeo.

## Posicionamiento

El panel se posiciona de forma absoluta sobre el contenedor del mapa en
`top: 16px; right: 16px` (`top: 1rem; right: 1rem` en el CSS de la receta),
con `z-index: 5`. La ubicación superior derecha es intencional: mantiene el
panel alejado de los controles de zoom del mapa. Tiene un `min-width` de
160px para que los conteos no reorganicen la cuadrícula al cambiar el ancho
de sus dígitos.

## Tokens

Todo valor de color, radio y espaciado en la receta se resuelve a través
del sistema de tokens — el panel no lleva ningún valor de diseño
codificado de forma fija excepto su sombra. Desde `recipe.json`:

| Token | Nivel | Controla |
|---|---|---|
| `semantic.surface.layer` | [tema](/tokens#theme) | Fondo del panel (`--pds-surface-layer`) |
| `semantic.text.primary` | [tema](/tokens#theme) | Color del valor de estadística (`--pds-text-primary`) |
| `semantic.text.secondary` | [tema](/tokens#theme) | Color de la etiqueta de estadística (`--pds-text-secondary`) |
| `semantic.border.subtle` | [tema](/tokens#theme) | Borde del panel (`--pds-border-subtle`) |
| `primitive.radius.sm` | [primitivo](/tokens#primitive) | Radio de esquina (`--pds-radius-sm`) |
| `primitive.space.2` | [primitivo](/tokens#primitive) | Relleno del panel, espacio entre filas de la cuadrícula (`--pds-space-2`) |
| `primitive.space.4` | [primitivo](/tokens#primitive) | Espacio entre columnas de la cuadrícula (`--pds-space-4`) |
| `primitive.motion.duration.base` | [primitivo](/tokens#primitive) | Transición de cambio de color del valor (`--pds-duration-base`) |

Dado que los valores de superficie, texto y borde son semánticos (nivel de
tema), el panel se re-adapta al tema del inquilino anfitrión sin ningún
cambio a nivel de componente. El `box-shadow`
(`0 2px 8px rgba(0,0,0,0.15)`) es el único valor literal en la receta —
aún no está tokenizado.

## Accesibilidad

El panel se basa en los propios campos `aria` y `wcag` de la receta:

- **Punto de referencia.** El contenedor es `role="region"` con
  `aria-label="Map statistics"`, de modo que la tecnología de asistencia
  pueda saltar a él como una región nombrada.
- **Actualizaciones en vivo.** `aria-live="polite"` anuncia los cambios de
  conteo impulsados por filtros sin interrumpir el habla ya en curso — el
  visitante escucha las nuevas cifras en la siguiente pausa natural en
  lugar de ser interrumpido.
- **Emparejamiento semántico.** Cada estadística es un par término/valor
  `<dt>`/`<dd>` dentro de la lista de definiciones, de modo que la
  etiqueta y su cifra están asociadas programáticamente.
- **Unidades explícitas.** Cuando una unidad no es implícita, el valor
  lleva un `aria-label` explícito (p. ej. `aria-label="N corridors"`) de
  modo que un lector de pantalla anuncie "42 corredores," no un número
  aislado.
- **Contraste.** Las etiquetas cumplen 4.5:1 (WCAG 2.2 AA) y los valores
  cumplen 7:1 (AAA) contra la superficie del panel. El objetivo WCAG del
  componente es **2.2 AA**.

## Preguntas abiertas

- Si el panel debe colapsarse automáticamente en pantallas pequeñas
  (móvil &lt;640px) y expandirse al tocar, o permanecer siempre visible.
  Decisión pendiente de la telemetría de uso móvil (`oq-1` de la receta).

## Cuándo no usar

- No use este panel para el detalle de una sola característica — para
  eso está [Map Side Drawer](/components/map-side-drawer/usage).
- No lo use para cifras no relacionadas con la vista de mapa actual. El
  contrato del panel es que sus conteos reflejan exactamente lo que
  muestra el mapa filtrado; poner en él números estáticos o fuera de
  vista rompe esa expectativa.
