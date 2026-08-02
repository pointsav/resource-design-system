<div class="page-intro">
<span class="eyebrow">Alojamiento propio</span>
<p class="page-intro__lede"><code>app-privategit-design</code> es el mismo motor que ejecuta
design.pointsav.com — compile el binario, apúntelo a su propio directorio vault, y servirá
la galería de tokens de su sistema de diseño, la documentación de componentes, el contenido
de Writing/Paper, y un endpoint MCP on-prem directamente desde su propia infraestructura.
Sus tokens, su historial de cambios, su perímetro — una VM pequeña, una unidad de rack
sobrante, o una laptop reconvertida en servidor. Sin dependencia de la nube, sin base de
datos administrada, sin representante de cuenta a quien llamar.</p>
</div>

<section class="install-block">
<div class="install-block__label"><span class="badge badge--brand">Inicio rápido</span></div>
<h2>Compile el binario, apúntelo a un directorio vault, y ya está funcionando.</h2>
<p class="install-block__intro">No hay asistente de instalación ni paso de activación con
clave de licencia. El binario lee tres variables de entorno y comienza a servir.</p>

<div class="doc-code-block">
<div class="doc-code-block__label"><span>Terminal</span><span>bash</span></div>
<pre><code>$ git clone https://github.com/pointsav/pointsav-design-system.git
$ git clone https://github.com/pointsav/pointsav-monorepo.git
$ cd pointsav-monorepo &amp;&amp; cargo build --release -p app-privategit-design
$ DESIGN_VAULT_DIR=../pointsav-design-system/dtcg-vault \
  DESIGN_BIND=127.0.0.1:9094 \
  DESIGN_SITE_ORIGIN=https://design.example.com \
  ./target/release/app-privategit-design
<span class="tok-comment"># sirviendo en 127.0.0.1:9094
# Tokens, Componentes, Writing, Paper + endpoint MCP on-prem, todo desde este proceso</span></code></pre>
</div>
</section>

<section class="install-block">
<div class="install-block__label"><span class="badge badge--brand">Por qué un solo binario</span></div>
<h2>Un solo binario reemplaza la base de datos, la caché y el medidor por asiento.</h2>
<p class="install-block__intro">Una plataforma de sistema de diseño alojada típica le pide
a un equipo con poco personal que mantenga una segunda pila en paralelo al trabajo de
diseño real.</p>

<div class="compare-callout">
<div class="compare-callout__heading"><strong>Pila típica frente a este servidor</strong></div>
<div class="compare-callout__cols">
<div class="compare-callout__col compare-callout__col--them">
<div class="compare-callout__col-title">Plataforma alojada típica</div>
<ul>
<li>Instancia de Postgres administrada que hay que aprovisionar y respaldar</li>
<li>Redis (o similar) para sesiones/caché</li>
<li>Medidor mensual por asiento</li>
<li>Los datos de diseño viven en la infraestructura de un proveedor</li>
<li>La consulta de un agente de IA viaja a los servidores de un tercero para obtener una respuesta</li>
</ul>
</div>
<div class="compare-callout__col compare-callout__col--us">
<div class="compare-callout__col-title">app-privategit-design</div>
<ul>
<li>Sin Postgres — el estado vive en los propios archivos del vault rastreados por Git</li>
<li>Sin Redis</li>
<li>Sin medidor por asiento para el código fuente AGPL-3.0-or-later</li>
<li>Un solo binario, su propia infraestructura</li>
<li>Endpoint MCP on-prem — las consultas de los agentes permanecen en su propia red</li>
</ul>
</div>
</div>
<p class="compare-callout__footnote">Comparación de la arquitectura típica de una
plataforma alojada en términos generales; verificado contra el propio <code>Cargo.toml</code>
de este crate — no existe ninguna dependencia de controlador de base de datos o de caché
en el árbol de dependencias real.</p>
</div>
</section>

<section class="install-block">
<div class="install-block__label"><span class="badge badge--brand">Variantes de instalación</span></div>
<h2>Se planean una imagen de contenedor y un paquete sin conexión.</h2>
<p class="install-block__intro">La ruta de compilación desde el código fuente descrita
arriba es la única que se ofrece hoy. Se planean una imagen de Docker y un paquete sin
conexión para entornos aislados (air-gapped), pensados para equipos con reglas de
despliegue más estrictas — ambos seguirían entregando el mismo proceso único, sin
servicios adicionales que levantar.</p>
</section>

<section class="install-block">
<div class="install-block__label"><span class="badge badge--brand">Qué se necesita para ejecutarlo</span></div>
<h2>Hardware modesto, términos de licencia reales.</h2>

<div class="note-strip"><div class="note-strip__body">
<p><strong>Huella de hardware:</strong> un único binario de Rust sin proceso de base de
datos ni de caché que ejecutar junto a él — el árbol de dependencias no lleva ningún
controlador de Postgres/Redis. No se requiere GPU ni clúster para servir el propio
contenido del sistema de diseño.</p>
</div></div>

<div class="note-strip"><div class="note-strip__body">
<p><strong>Licencia:</strong> el código fuente se distribuye bajo
<strong>AGPL-3.0-or-later</strong>. Ya existe un nivel independiente <strong>PointSav
Commercial</strong> para el binario compilado — otorga derechos equivalentes a
Apache-2.0 (sin obligaciones de copyleft, con libertad para bifurcar y redistribuir) sin
tocar la licencia AGPL del código fuente en sí, distribuido por cliente a través del
<a href="https://software.pointsav.com">mercado de software de PointSav</a>. Los tokens
de diseño de este repositorio se licencian por separado, bajo Apache-2.0.</p>
</div></div>
</section>

<div class="closing-cta">
<div class="closing-cta__text"><h3>Qué sigue</h3>
<p>Recorra el conjunto de tokens que se entrega con el binario, o vea cómo un agente de
IA se conecta al endpoint MCP on-prem una vez que está en ejecución.</p></div>
<div class="closing-cta__actions">
<a href="/tokens" class="btn btn--secondary">Explorar tokens</a>
<a href="/developing/mcp/overview" class="btn btn--primary">Conectar sus agentes de IA</a>
</div>
</div>
