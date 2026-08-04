<div class="page-intro">
<span class="eyebrow">Desarrollo</span>
<p class="page-intro__lede">El sistema base expone un servidor JSON-RPC de Model Context
Protocol (MCP) junto a las páginas que está leyendo ahora mismo, más un pequeño conjunto
de endpoints GET simples para agentes que no necesitan el sobre MCP completo. Apunte un
agente compatible con MCP hacia él y podrá consultar componentes, tokens y notas de
investigación directamente — sin necesidad de levantar un servicio aparte, sin una copia
del registro que mantener sincronizada a mano.</p>

<div class="stat-panel">
<div class="stat-panel__item"><span class="stat-panel__value">5</span><span class="stat-panel__label">Herramientas MCP</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">5</span><span class="stat-panel__label">Endpoints documentados</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">1</span><span class="stat-panel__label">Formato de exportación de tokens (DTCG)</span></div>
<div class="stat-panel__item"><span class="stat-panel__value">0</span><span class="stat-panel__label">Llamadas de red externas</span></div>
</div>
</div>

<nav class="domain-jump" aria-label="Saltar a la sección">
<a href="#mcp">Endpoint MCP</a>
<a href="#registry-api">API de registro</a>
<a href="#token-export">Exportación de tokens</a>
<a href="#why-it-matters">Por qué esto importa</a>
</nav>

<section class="doc-section" id="mcp">
<h2>Endpoint MCP on-prem</h2>
<p class="doc-section__intro">Este mismo binario expone un servidor de Model Context
Protocol (MCP) junto a las páginas que está leyendo ahora mismo. Apunte un agente
compatible con MCP hacia él y podrá consultar componentes, tokens y notas de
investigación directamente — sin necesidad de levantar un servicio aparte, sin una copia
del registro que mantener sincronizada a mano.</p>

<div class="card onprem-callout">
<div class="onprem-callout__icon" aria-hidden="true">&#8962;</div>
<div>
<h3>Se ejecuta en su propia infraestructura</h3>
<p>El servidor MCP se entrega dentro del mismo binario que este sitio de documentación.
Cuando lo ejecuta en su propio hardware, cada llamada a una herramienta — desde una
simple consulta de <code>get_token</code> hasta un barrido completo de
<code>list_components</code> — se responde localmente. Nada de su base de código, sus
prompts, o qué componentes está consultando un agente se envía a ningún tercero; nunca
sale de su propia red.</p>
<p>No existe una alternativa alojada — on-prem, tal como se describe en
<a href="/developing/install/overview">Alojamiento propio</a>, es la única forma en que
se ofrece esta superficie.</p>
</div>
</div>

<div class="card-grid">
<div class="card"><h3><span class="mcp-tool__name">list_components(category?)</span></h3>
<p class="mcp-tool__desc">Devuelve todos los componentes que el registro conoce
actualmente, opcionalmente filtrados por categoría de origen (sistema base genérico,
origen GIS, origen del motor wiki), junto con un puntero a su receta completa.</p></div>
<div class="card"><h3><span class="mcp-tool__name">get_component_recipe(name)</span></h3>
<p class="mcp-tool__desc">Devuelve la receta HTML/CSS, las dependencias de tokens y los
objetivos de accesibilidad de un componente nombrado — los mismos datos que una persona
lee en su página de Componentes.</p></div>
<div class="card"><h3><span class="mcp-tool__name">get_token(name)</span></h3>
<p class="mcp-tool__desc">Resuelve un único token de diseño por el nombre de su
propiedad personalizada CSS (<code>--ps-interactive</code>) o por su ruta DTCG
(<code>semantic.interactive-primary</code>).</p></div>
<div class="card"><h3><span class="mcp-tool__name">search_design_system(query)</span></h3>
<p class="mcp-tool__desc">Búsqueda de texto completo en todos los documentos indexados
del vault — components, tokens, research, guidelines, developing, designing, about —
para un agente que aún no conoce el nombre exacto de lo que necesita.</p></div>
<div class="card"><h3><span class="mcp-tool__name">list_token_families(pillar?)</span></h3>
<p class="mcp-tool__desc">Devuelve cada familia de tokens (agrupación pilar/capa/familia,
p. ej. <code>paper/semantic/financial-report-layout</code>) con su conteo de miembros,
opcionalmente filtrado a un pilar. La taxonomía a revisar antes de adivinar el nombre de
un grupo de tokens — ver <a href="/developing/token-families/overview">Familias de
tokens</a>.</p></div>
</div>
</section>

<section class="doc-section" id="registry-api">
<h2>API de registro / máquina</h2>
<p class="doc-section__intro">No existe un único archivo de registro agregado para
descargar. Las recetas de componentes, el paquete de tokens y la búsqueda de texto
completo son tres endpoints reales y separados — verificado directamente contra la
propia tabla de rutas del servidor en ejecución.</p>

<div class="endpoint-meta"><span class="badge badge--brand">POST</span><code>/mcp</code></div>
<p class="endpoint-meta__desc">JSON-RPC 2.0. Siempre devuelve HTTP 200 — revise el
cuerpo de la respuesta en busca de una clave <code>error</code> en lugar del código de
estado. Sobre estándar de MCP: <code>tools/list</code> para enumerar las cinco
herramientas anteriores, <code>tools/call</code> para invocar una.</p>
<div class="doc-code-block">
<div class="doc-code-block__label"><span>Solicitud</span><span>Ejemplo</span></div>
<pre><code>curl -s https://design.pointsav.com/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"get_component_recipe","arguments":{"name":"button"}}}'</code></pre>
</div>
<div class="doc-code-block">
<div class="doc-code-block__label"><span>Respuesta</span><span>application/json</span></div>
<pre><code><span class="tok-attr">{</span>
  <span class="tok-attr">"jsonrpc"</span>: <span class="tok-str">"2.0"</span>,
  <span class="tok-attr">"id"</span>: <span class="tok-str">1</span>,
  <span class="tok-attr">"result"</span>: <span class="tok-attr">{</span>
    <span class="tok-attr">"content"</span>: [<span class="tok-attr">{</span> <span class="tok-attr">"type"</span>: <span class="tok-str">"text"</span>, <span class="tok-attr">"text"</span>: <span class="tok-str">"{ ...recipe.json, as a string... }"</span> <span class="tok-attr">}</span>]
  <span class="tok-attr">}</span>
<span class="tok-attr">}</span></code></pre>
</div>
<p class="endpoint-meta__desc">La receta viaja dentro de <code>result.content[0].text</code>
como una cadena JSON, no como un objeto de nivel superior — analícela (parse) una vez
más de su lado. Leer <code>dtcg-vault/components/button/recipe.json</code> directamente
es la alternativa a nivel de sistema de archivos.</p>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/components/:slug/recipe.json</code></div>
<p class="endpoint-meta__desc">Un GET simple, invocable con curl, para la receta de un
componente — sin sobre JSON-RPC. Lee <code>vault/components/&lt;slug&gt;/recipe.json</code>
tal cual y lo sirve como <code>application/json</code>.</p>
<div class="doc-code-block">
<div class="doc-code-block__label"><span>Solicitud</span><span>Ejemplo</span></div>
<pre><code>curl -s https://design.pointsav.com/components/button/recipe.json</code></pre>
</div>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/tokens/search?q=...</code></div>
<p class="endpoint-meta__desc">Búsqueda de texto completo en componentes, tokens y notas
de investigación — el mismo índice que consulta la herramienta MCP
<code>search_design_system</code>. La respuesta es un arreglo JSON de objetos
<code>{id, title, snippet, url}</code>, con un tope de 20 resultados. Un <code>q</code>
vacío o ausente devuelve <code>[]</code>.</p>

<div class="registry-note"><span aria-hidden="true">&#8618;</span>
<span><code>/mcp</code>, <code>/components/:slug/recipe.json</code>, y
<code>/tokens/search</code> leen los mismos archivos del vault desde los que se
renderiza cada página de este sitio orientada a personas. No existe una segunda copia
de estos datos que pueda desincronizarse.</span>
</div>
</section>

<section class="doc-section" id="token-export">
<h2>Exportación de tokens DTCG</h2>
<p class="doc-section__intro">Los agentes que solo necesitan los valores de los tokens
— no las recetas completas de componentes — pueden obtener directamente la exportación
en formato DTCG del registro, sin pasar en absoluto por <code>/mcp</code>.</p>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/bundles/tokens/tokens.full.json</code></div>
<p class="endpoint-meta__desc">El paquete completo de tokens DTCG — todos los tokens
primitive y theme, con rutas y valores reales en notación de puntos, servido como
<code>application/json</code> simple.</p>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/bundles/tokens/tokens.css</code></div>
<p class="endpoint-meta__desc">Los mismos tokens compilados a propiedades personalizadas
CSS, servidos como <code>text/css</code> — enlácelo directamente.</p>

<div class="endpoint-meta"><span class="badge badge--brand">GET</span><code>/bundles/tokens/download</code></div>
<p class="endpoint-meta__desc">Comprime en zip el paquete de tokens actual
(<code>tokens.full.json</code>, <code>tokens.css</code>, más los archivos de
investigación/atribución del paquete) para uso sin conexión.</p>
</section>

<section class="doc-section closing-note" id="why-it-matters">
<h2>Por qué esto importa</h2>
<p class="doc-section__intro">Cada endpoint de esta página — <code>/mcp</code>,
<code>/components/:slug/recipe.json</code>, <code>/tokens/search</code>,
<code>/bundles/tokens/*</code> — lee del mismo registro que impulsa cualquier otra
página de este sitio, incluidos los conteos de tokens y las muestras en
<a href="/tokens">Tokens</a>. No existe una ruta de código separada reservada para
máquinas.</p>
</section>
