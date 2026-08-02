<div class="page-intro">
<span class="eyebrow">Línea de producto</span>
<p class="page-intro__lede">Conjunto de componentes orientado a impresión para diagramas
de jerarquía de entidades/propiedad — la más nueva de las tres líneas de producto
construidas sobre los tokens de este sistema de diseño, incorporada en esta versión.</p>

<div class="domain-stats">
<div class="domain-stat"><span class="domain-stat__value">3</span><span class="domain-stat__label">componentes reales</span></div>
<div class="domain-stat"><span class="domain-stat__value">1</span><span class="domain-stat__label">ejemplo renderizado — Org Chart Node</span></div>
<div class="domain-stat"><span class="domain-stat__value">1 / 6</span><span class="domain-stat__label">color sin equivalente en una paleta de estado genérica</span></div>
</div>
</div>

<div class="domain-intro">
<p>Los diagramas de organigrama son una superficie orientada a impresión — cada nodo se
renderiza en una posición de píxel fija sobre un lienzo de 1056&times;816px (US Letter
horizontal a 96dpi), no como una maquetación web fluida. Esa restricción, y el sistema
de color por rol de entidad que requiere, no encajan limpiamente con una paleta de
color de estado/interactivo de propósito general — ver el análisis de brechas más abajo.</p>
<p>El registro de tokens reserva una paleta de 9 roles de entidad
(<code>primitive.color.orgchart.*</code>, ver <a href="/tokens#primitive">Tokens</a>)
— el componente Org Chart Node ya publicado usa hoy 6 de esos 9 roles (verde, azul,
morado, naranja, gris y amarillo); los 3 restantes (dos colores "entidad heredada" más
una variante de gris adicional) son capacidad reservada, aún no conectada a ninguna
variante de componente.</p>
</div>

<div class="gap-table-wrap">
<h2>Por qué los tokens de organigrama tienen su propio espacio de nombres, en lugar de reutilizar tokens de estado</h2>
<p>Del análisis de brechas real y ratificado
(<code>dtcg-vault/research/orgchart-carbon-token-map.md</code>): de los seis colores de
rol de entidad, uno (Broker / gestor de activos, morado) no tiene equivalente alguno en
una paleta de estado de propósito general típica — ese tipo de paleta no ofrece nada
similar en su sistema semántico. Otros dos (el azul de Vehículo de Inversión, el verde
de Holding Corporativo) se corresponden con un rol de paleta de estado de intención
similar, pero con un valor hexadecimal o un registro semántico notablemente distinto
(ver la tabla). Reutilizar los tokens de color de soporte de una paleta de estado para
los tres restantes importaría semántica de estado/alerta (éxito, precaución,
advertencia) a lo que son distinciones estructurales, no evaluativas, entre tipos de
entidad. Las dimensiones de las cajas (110&ndash;250px, más el lienzo de
1056&times;816px) tampoco derivan de una escala de espaciado típica de 8px — están
fijadas por la legibilidad en impresión y la geometría de la página US Letter. La
tipografía va de 9 a 12px, por debajo del piso de 12px que suele fijar una escala
tipográfica genérica de interfaz, porque solo caben alrededor de cinco cajas de 210px
de ancho en una fila del lienzo de 1056px, dejando poco margen para un tamaño de tipo
mayor.</p>

<div class="doc-table-scroll" role="region" tabindex="0" aria-label="Org chart to general-purpose status color mapping, scroll horizontally">
<table class="doc-table">
<thead><tr><th>Rol de entidad</th><th>Nuestro token</th><th>Rol de paleta de estado más cercano</th><th>Evaluación</th></tr></thead>
<tbody>
<tr><td>Holding corporativo</td><td><code>primitive.color.orgchart.green</code></td><td>support-success</td><td>Matiz distinto — el nuestro es un salvia más claro, el equivalente de la paleta de estado es un verde bosque más oscuro</td></tr>
<tr><td>Vehículo de inversión</td><td><code>primitive.color.orgchart.blue</code></td><td>interactive</td><td>Registro distinto — azul marino institucional frente a azul interactivo brillante</td></tr>
<tr><td>Broker / gestor de activos</td><td><code>primitive.color.orgchart.purple</code></td><td>ninguno</td><td><strong>Sin equivalente alguno en una paleta de estado de propósito general</strong></td></tr>
<tr><td>Socio de capital</td><td><code>primitive.color.orgchart.orange</code></td><td>support-caution-major</td><td>Visualmente cercano, semánticamente incorrecto — precaución implica una advertencia</td></tr>
<tr><td>Entidad administrativa</td><td><code>primitive.color.orgchart.grey</code></td><td>border-strong</td><td>Luminosidad similar, uso distinto — borde frente a relleno de entidad</td></tr>
<tr><td>Vehículo LP / fondo</td><td><code>primitive.color.orgchart.yellow</code></td><td>support-warning</td><td>Visualmente cercano, semánticamente incorrecto — advertencia implica una alerta</td></tr>
</tbody>
</table>
</div>
</div>

<section class="card-grid" aria-label="Org Charts components">
<div class="card"><h3>Org Chart Node</h3>
<p>Caja de entidad posicionada de forma absoluta sobre el lienzo de impresión. Tres
familias de forma — rectángulo (entidades operativas), píldora (vehículos de fondo,
siempre punteada), elipse (transferencias transfronterizas de paso).</p>
<div class="card__tags"><a href="/components/orgchart-node/usage" class="badge badge--brand">Ejemplo en vivo &rarr;</a></div></div>

<div class="card"><h3>Org Chart Canvas</h3>
<p>El lienzo de impresión de dimensión fija que aloja todas las cajas de nodo y las capas
de conectores superpuestas — exactamente US Letter horizontal a 96dpi
(1056&times;816px), que llena la página de borde a borde al imprimirse.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Org Chart Connector</h3>
<p>Capa SVG superpuesta de líneas de conexión dirigidas entre nodos, por debajo de las
cajas de nodo. El relleno de la punta de flecha coincide con el color de borde de la
caja de origen.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>
</section>

<div class="closing-cta">
<div class="closing-cta__text"><h3>3 componentes reales, la línea de producto más nueva.</h3>
<p>Cada tarjeta anterior es un componente real y registrado con su propio recipe.json —
obtenga los tokens en bruto o explore el registro completo.</p></div>
<div class="closing-cta__actions"><a href="/tokens" class="btn btn--secondary">Ver los tokens</a></div>
</div>
