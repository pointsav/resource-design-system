<div class="page-intro">
<span class="eyebrow">Desarrollo</span>
<p class="page-intro__lede">Cada token de este sistema pertenece exactamente a una familia — una
agrupación <code>pilar / capa / familia</code>, por ejemplo
<code>paper / semantic / financial-report-layout</code>. Esta página nombra la taxonomía para
que un archivo productor pueda encontrar la familia correcta antes de adivinar un nombre de
token, en lugar de redactar un casi-duplicado porque el token real no fue fácil de encontrar.</p>

<div class="stat-panel">
<div class="stat-panel__item"><span class="stat-panel__value">40</span><span class="stat-panel__label">Familias de tokens</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">7</span><span class="stat-panel__label">Pilares</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">0</span><span class="stat-panel__label">Mantenidas a mano — generadas desde el mismo registro que lee get_token</span></div>
</div>
</div>

<nav class="domain-jump" aria-label="Saltar a la sección">
<a href="#shape">La forma: pilar / capa / familia</a>
<a href="#pillars">Los siete pilares</a>
<a href="#finding">Encontrar la familia correcta</a>
<a href="#mcp-tool">list_token_families()</a>
</nav>

<section class="doc-section" id="shape">
<h2>La forma: pilar / capa / familia</h2>
<p class="doc-section__intro">El id canónico de un token es su pilar y su ruta DTCG
completa, unidos textualmente — sin capa de traducción entre el id, la propiedad
personalizada CSS, y lo que <code>get_token</code> compara (ver
<a href="/developing/mcp/overview">MCP y API de máquina</a>). Una familia es la
agrupación un nivel arriba: todo token que comparte el mismo pilar, capa, y nombre de
nivel superior.</p>

<div class="card-grid">
<div class="card"><h3>Pilar</h3>
<p>El nivel superior: <code>primitive</code>, <code>theme</code>, <code>paper</code>,
<code>writing</code>, <code>wcp</code>, más los dos pilares de extensión de organigrama.</p></div>
<div class="card"><h3>Capa</h3>
<p>Solo <code>paper</code> y <code>writing</code> realmente anidan bajo un envoltorio
<code>primitive</code>/<code>semantic</code> antes de que comiencen sus grupos reales — así
que solo esos dos pilares llevan una capa. La capa de cualquier otro pilar es
<code>null</code>; su primer segmento de ruta es la familia directamente.</p></div>
<div class="card"><h3>Familia</h3>
<p>El grupo nombrado en sí — una familia de documento como
<code>financial-report-layout</code>, un grupo de oficio como <code>rhythm</code>, o una
categoría primitiva como <code>color</code>. Todo token hoja de una familia comparte el
mismo prefijo de id.</p></div>
</div>

<p class="doc-section__intro">Ejemplo trabajado: el token
<code>--ps-paper-semantic-financial-report-layout-header-rule</code> tiene pilar
<code>paper</code>, capa <code>semantic</code>, familia
<code>financial-report-layout</code> — legible directamente desde la cadena del id, ya que
el id <em>es</em> la ruta pilar/capa/familia sin re-formateo ni re-delimitación.</p>
</section>

<section class="doc-section" id="pillars">
<h2>Los siete pilares</h2>
<p class="doc-section__intro">Cada fila es un pilar real en la exportación actual, no una
lista aspiracional — los conteos son en vivo, misma fuente que el panel de estadísticas
arriba.</p>

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Pilar</th><th>Capa</th><th>Qué contiene</th><th>Familias de ejemplo</th></tr></thead>
<tbody>
<tr><td><code>primitive</code></td><td>—</td><td>Valores crudos, neutrales al arrendatario: color, espaciado, tipografía, movimiento, bordes, viewport, foco, duración.</td><td><code>color</code> (60), <code>typography</code> (14), <code>size</code> (13)</td></tr>
<tr><td><code>theme</code></td><td>—</td><td>El tema propio de referencia/predeterminado de PointSav — mapeos de rol semántico sobre primitivos, más una variante de modo oscuro. El tema de referencia del proveedor, no una bifurcación de arrendatario (ver la nota de pilar abajo).</td><td><code>semantic</code> (53), <code>dark</code> (28), <code>accessibility</code> (5)</td></tr>
<tr><td><code>paper</code></td><td>primitive / semantic</td><td>Sustrato de formato de impresión/documento — geometría de página, grosores de regla, escalas tipográficas, y una familia semántica por registro de documento (acuerdos legales, informes financieros, navegación de encuadernador PDF, fideicomiso/prospecto FIBRA de México, …).</td><td><code>mx-fibra-prospectus</code> (49), <code>legal-subscription-agreement</code> (30), <code>financial-report-layout</code> (25)</td></tr>
<tr><td><code>writing</code></td><td>primitive / semantic</td><td>Tokens de gobernanza de prosa — voz, ritmo, uso de mayúsculas, escala de registro, plantillas de descargo de responsabilidad, y patrones de contenido nombrados para una familia de documento específica.</td><td><code>register</code> (7), <code>rhythm</code> (7), <code>pattern</code> (4)</td></tr>
<tr><td><code>wcp</code></td><td>—</td><td>Espacios de nombres de propiedades personalizadas CSS de cara al motor — actualmente una familia, una capa pura de alias sobre una familia Paper ya canónica, nunca un segundo almacén de valores literales (ver <a href="/tokens#paper">financial-report-layout</a>).</td><td><code>finance</code> (25, todos alias)</td></tr>
<tr><td><code>ibm-carbon-org-chart</code> / <code>org-chart-extended</code></td><td>—</td><td>Niveles de extensión de componente de organigrama, incorporados como fuentes de primera clase desde <code>tokens-woodfine-org-chart-extended.json</code>.</td><td><code>warm-gray</code>, <code>token-warm-gray</code></td></tr>
</tbody>
</table>
</div>

<div class="registry-note"><span aria-hidden="true">&#8618;</span>
<span>El pilar <code>theme</code> contiene solo el tema de referencia propio de PointSav —
no es un objetivo de bifurcación multi-arrendatario. Los valores de token específicos de
marca de un arrendatario adoptante (por ejemplo, la paleta de Woodfine) viven en el propio
repositorio de activos de medios de ese arrendatario, superpuestos mediante anulación de
propiedad personalizada CSS, no dentro de este pilar. Ver
<code>.agent/rules/design-tokens.md</code> en el archivo project-design para la
justificación completa.</span>
</div>
</section>

<section class="doc-section" id="finding">
<h2>Encontrar la familia correcta antes de redactar una nueva</h2>
<p class="doc-section__intro">El modo de falla que esta taxonomía existe para prevenir: un
archivo productor no puede encontrar una familia existente, asume que no existe, y redacta
un casi-duplicado bajo un nombre nuevo. Dos verificaciones, en orden:</p>

<div class="card-grid">
<div class="card"><h3>1. ¿Es una variación de familia de documento?</h3>
<p>Un nuevo documento de cumplimiento, registro de impresión, o instrumento legal casi
siempre compone <code>paper.primitive.*</code> existente y añade un nuevo grupo
<code>paper.semantic.&lt;familia&gt;.*</code> — rara vez necesita primitivos nuevos.
Revise la tabla de familias Paper arriba y en <a href="/tokens#paper">Tokens — nivel
Paper</a> antes de asumir que ninguna de las once familias de documento existentes está
lo suficientemente cerca para extenderla.</p></div>
<div class="card"><h3>2. ¿Es un valor genuinamente nuevo, o una bifurcación de marca de un arrendatario?</h3>
<p>Un valor literal de color/tamaño/tipo reutilizable en cualquier marca adoptante
pertenece a <code>primitive</code> o a una familia Paper/Writing. Un valor que codifica la
identidad de marca de un arrendatario específico no pertenece a este repositorio en
absoluto — ver la nota de pilar arriba.</p></div>
</div>
</section>

<section class="doc-section closing-note" id="mcp-tool">
<h2>list_token_families(pillar?)</h2>
<p class="doc-section__intro">La forma legible por máquina de esta página. Devuelve cada
familia — las mismas filas que la tabla arriba — como JSON, opcionalmente filtrado a un
pilar, obtenido del mismo registro generado <code>token-families.json</code> que leen
tanto <code>get_token</code> como esta página. Ver
<a href="/developing/mcp/overview">MCP y API de máquina</a> para la lista completa de
herramientas y la forma de llamada.</p>
<div class="doc-code-block">
<div class="doc-code-block__label"><span>Respuesta</span><span>application/json</span></div>
<pre><code><span class="tok-attr">[</span>
  <span class="tok-attr">{</span> <span class="tok-attr">"pillar"</span>: <span class="tok-str">"paper"</span>, <span class="tok-attr">"layer"</span>: <span class="tok-str">"semantic"</span>, <span class="tok-attr">"family"</span>: <span class="tok-str">"financial-report-layout"</span>, <span class="tok-attr">"member_count"</span>: <span class="tok-str">25</span> <span class="tok-attr">}</span>,
  <span class="tok-attr">{</span> <span class="tok-attr">"pillar"</span>: <span class="tok-str">"wcp"</span>, <span class="tok-attr">"layer"</span>: <span class="tok-str">null</span>, <span class="tok-attr">"family"</span>: <span class="tok-str">"finance"</span>, <span class="tok-attr">"member_count"</span>: <span class="tok-str">25</span> <span class="tok-attr">}</span>
  <span class="tok-attr">// … 38 más</span>
<span class="tok-attr">]</span></code></pre>
</div>
</section>
