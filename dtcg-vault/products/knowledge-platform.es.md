<div class="page-intro">
<span class="eyebrow">Línea de producto</span>
<p class="page-intro__lede">Conjunto de componentes que impulsa el motor de wiki propio
de PointSav — la misma familia de wikis de documentation.pointsav.com,
projects.woodfinegroup.com y corporate.woodfinegroup.com, una de las tres líneas de
producto construidas sobre los tokens de este sistema de diseño.</p>

<div class="domain-stats">
<div class="domain-stat"><span class="domain-stat__value">13</span><span class="domain-stat__label">componentes reales</span></div>
<div class="domain-stat"><span class="domain-stat__value">1</span><span class="domain-stat__label">ejemplo renderizado — Home Grid</span></div>
<div class="domain-stat"><span class="domain-stat__value">Tipografía propia</span><span class="domain-stat__label">tipografía de artículo dedicada, separada del chrome de la interfaz (ver Tokens)</span></div>
</div>
</div>

<div class="domain-intro">
<p>El contenido de los artículos de la wiki se lee en una tipografía dedicada de
lectura extensa y su monoespaciada complementaria, distinta del emparejamiento que el
resto de este sistema de diseño usa para el chrome de la interfaz. Es un cambio de
registro deliberado para la lectura de formato largo — ver el token
<code>primitive.typography.wiki-h1</code> en <a href="/tokens">Tokens</a>.
La cuadrícula de navegación por categorías de la página de inicio (Home Grid, más
abajo) extiende el patrón estándar de cuadrícula de mosaicos con una regla ratificada
de renderizar siempre las nueve categorías, de modo que una categoría vacía se lee como "en
preparación", nunca como una página faltante. Los resultados de búsqueda están
respaldados por un índice de texto completo Tantivy real, servido a través del mismo
endpoint JSON-RPC <code>/mcp</code> documentado en
<a href="/developing/mcp/overview">Desarrollo</a>.</p>
</div>

<section class="card-grid" aria-label="Componentes de Knowledge Platform">
<div class="card"><h3>Home Grid</h3>
<p>Cuadrícula responsiva de navegación por categorías con 9 tarjetas para la página
de inicio de la wiki. Siempre renderiza las 9 categorías ratificadas, incluidas las
vacías ("0 artículos — en preparación"), en lugar de ocultarlas.</p>
<div class="card__tags"><a href="/components/home-grid/usage" class="badge badge--brand">Ejemplo en vivo &rarr;</a></div></div>

<div class="card"><h3>Wiki Search Results</h3>
<p>Lista ordenada de resultados de búsqueda con un extracto en texto sin formato.
Respaldada por el endpoint JSON-RPC de Tantivy en <code>/mcp</code> (método
<code>search</code>).</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Wiki TOC Sidebar</h3>
<p>Lista de encabezados fija en el riel derecho, con resaltado de la sección activa;
se colapsa en un interruptor en línea en pantallas compactas.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Wiki Article Header</h3>
<p>Breadcrumb, H1 a partir del frontmatter, distintivo de calidad y línea de
autoría. Sigue el diseño familiar de encabezado de artículo enciclopédico, en la
tipografía de lectura del artículo (<code>primitive.typography.wiki-h1</code>) a
2.25rem.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Wiki Article Footer</h3>
<p>Superficie al pie del artículo: etiquetas de categoría, sección de
referencias/citas, y un enlace de editar en GitHub — separa los metadatos
editoriales de la prosa del artículo.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Wiki Badge / Tag</h3>
<p>Chip de doble propósito: calificación de calidad del artículo
(Featured/Good/A/B/C/Stub) o un enlace de etiqueta de categoría. En línea, con forma
de píldora.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Citation Authority Ribbon</h3>
<p>Distintivos de diferenciación por tipo de fuente para las referencias — seis
clases de fuente fijas (académica, regulador, industria, y otras), cada una con su
propio color.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Freshness Ribbon</h3>
<p>Distintivo de fecha de última revisión de contenido por sección, mostrado después
del lápiz [editar] de la sección. Escala de color de tres puntos, de reciente a
desactualizado.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Research Trail Footer</h3>
<p>Panel desplegable colapsable al pie del artículo con tres subsecciones fijas:
Investigación realizada, Investigación sugerida, Preguntas abiertas — el registro de
la frontera epistémica de un artículo de la wiki.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Wiki Pagination</h3>
<p>Navegación de artículo anterior/siguiente dentro de una categoría. Cuadrícula de
tres columnas: artículo anterior, enlace de categoría, artículo siguiente.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Wiki Modal Dialog</h3>
<p>Elemento nativo <code>&lt;dialog&gt;</code> con captura de foco mediante
<code>showModal()</code>. Se usa para la caja de luz de imágenes, la superposición
de búsqueda y los mensajes de confirmación.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Wiki Dark Mode Toggle</h3>
<p>Alterna <code>data-theme="dark"</code> en <code>&lt;html&gt;</code> y conserva la
elección en <code>localStorage</code>, inicializándose a partir de ella al cargar.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>

<div class="card"><h3>Wiki Drawer (Mobile Navigation)</h3>
<p>Navegación superpuesta deslizante para pantallas compactas (&le;799px). El
disparador de hamburguesa abre un panel izquierdo de altura completa con la
navegación del sitio de la wiki.</p>
<div class="card__tags"><span class="badge">Receta documentada</span></div></div>
</section>

<div class="closing-cta">
<div class="closing-cta__text"><h3>13 componentes reales, uno renderizado hasta ahora.</h3>
<p>Cada tarjeta anterior es un componente real y registrado con un recipe.json
genuino detrás — las que aún no tienen una página renderizada están documentadas, no
son ficticias. Obtén los tokens en bruto o explora el registro completo.</p></div>
<div class="closing-cta__actions"><a href="/tokens" class="btn btn--secondary">Ver los tokens</a></div>
</div>
