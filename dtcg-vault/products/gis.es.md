<div class="page-intro">
<span class="eyebrow">Línea de producto</span>
<p class="page-intro__lede">Conjunto de componentes para análisis de
portafolio/retail basado en mapas — en producción en
<strong>gis.woodfinegroup.com (v0.1.94)</strong>, una de las tres líneas de producto
construidas sobre los tokens de este sistema de diseño.</p>

<div class="domain-stats">
<div class="domain-stat"><span class="domain-stat__value">4</span><span class="domain-stat__label">componentes reales</span></div>
<div class="domain-stat"><span class="domain-stat__value">1</span><span class="domain-stat__label">ejemplo renderizado — Map Side Drawer</span></div>
<div class="domain-stat"><span class="domain-stat__value">v0.1.94</span><span class="domain-stat__label">implementación de referencia en vivo</span></div>
</div>
</div>

<div class="domain-intro">
<p>Los cuatro componentes siguientes citan la misma implementación de referencia
real y en vivo directamente en su receta registrada — este no es un conjunto de
componentes hipotético construido por adelantado a un producto; documenta uno que ya
está en funcionamiento. El componente de muestra taxonómica (Brand-Family Swatch) es
deliberadamente <strong>agnóstico de taxonomía</strong>: los valores predeterminados
distribuidos cubren una taxonomía de retail Department / Hardware / Warehouse Club,
pero un cliente extiende el conjunto mediante un archivo de taxonomía en tiempo de
ejecución en lugar de un cambio de código — los colores de familia de marca residen
fuera del paquete de tokens primitivos precisamente por esta razón.</p>
</div>

<section class="card-grid" aria-label="Componentes GIS">
<div class="card"><h3>Map Side Drawer</h3>
<p>Panel de información persistente en el lado derecho para el detalle de
características del mapa. Se desliza al hacer clic; sustituye al patrón de ventana
emergente sobre el marcador, de modo que el mapa permanece interactivo por debajo.</p>
<div class="card__tags"><a href="/components/map-side-drawer/usage" class="badge badge--brand">Ejemplo en vivo &rarr;</a></div></div>

<div class="card"><h3>Map Stats Panel</h3>
<p>Panel flotante de estadísticas agregadas para la vista de mapa filtrada actual.
Se actualiza de forma reactiva ante cambios de filtro; posicionado en la esquina
superior derecha para evitar los controles de zoom.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Brand-Family Swatch</h3>
<p>Chip de punto taxonómico + etiqueta para la taxonomía de retail Department /
Hardware / Warehouse Club. Agnóstico de taxonomía — los clientes lo extienden
mediante un archivo de taxonomía en tiempo de ejecución.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Country Filter Chips</h3>
<p>Radiogroup horizontal que filtra los datos del mapa y se desplaza a los límites
del país seleccionado. El estado predeterminado es ALL (vista mundial); selección
exclusiva por ahora.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>
</section>

<div class="closing-cta">
<div class="closing-cta__text"><h3>4 componentes reales, ya en producción.</h3>
<p>Cada tarjeta anterior documenta un componente que se ejecuta en producción hoy —
obtén los tokens en bruto o explora el registro completo.</p></div>
<div class="closing-cta__actions"><a href="/tokens" class="btn btn--secondary">Ver los tokens</a></div>
</div>
