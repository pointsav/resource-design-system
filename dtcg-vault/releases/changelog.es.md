<div class="page-intro">
<span class="eyebrow">Versiones</span>
<p class="page-intro__lede">Cambios reales y fechados en el servidor y el grafo de tokens
de este sistema de diseño. A diferencia de un changelog de producto numerado por
versión, esta página registra lo que realmente se publicó y cuándo — no un historial
de números de versión inventado.</p>
</div>

<div class="release-list">
<div class="release-entry">
<div class="release-entry__head">
<span class="release-entry__date">2026-07-15</span>
</div>
<p class="release-entry__summary">Los pilares de tokens Paper y Writing quedaron
conectados de extremo a extremo; las páginas de Productos/Versiones/Instalación se
reconstruyeron al sistema visual actual; se corrigió un fallo real de contraste WCAG en
el botón Critical.</p>
<ul class="release-notes">
<li><span class="release-notes__tag release-notes__tag--added">Añadido</span>Los
pilares de tokens Paper y Writing quedaron conectados en la galería de tokens
(<code>/tokens</code>) de extremo a extremo: 185 &rarr; 381 tokens (Paper 164,
Writing 32). Ambos cuentan ahora con propiedades personalizadas CSS reales en
<code>tokens.css</code> (276 variables, incluyendo compuestos tipográficos
descompuestos), no solo datos de JSON/galería.</li>
<li><span class="release-notes__tag release-notes__tag--added">Añadido</span>Páginas
de aterrizaje reales para Paper y Writing, reconstrucción de las páginas de línea de
producto de Knowledge Platform/GIS/Org Charts, y una página de Instalación
reconstruida — sustituyendo listas de markdown planas por el sistema visual actual de
tarjetas, estadísticas y comparaciones.</li>
<li><span class="release-notes__tag release-notes__tag--fixed">Corregido</span>la
navegación móvil, que antes desaparecía por completo por debajo de 1300px de ancho de
viewport sin ningún reemplazo. Se incorporó un mecanismo de hamburguesa/cajón sin
JavaScript.</li>
<li><span class="release-notes__tag release-notes__tag--fixed">Corregido</span>un
fallo real de contraste WCAG AA en el color de reposo del botón Critical (4.44:1, por
debajo del piso de 4.5:1) — se cambió a <code>color.critical-60</code> (7.33:1). Ver
<a href="/components/button/accessibility">Button — Accesibilidad</a> para el detalle
completo.</li>
<li><span class="release-notes__tag release-notes__tag--changed">Cambiado</span>el
tratamiento de hover de las tarjetas ahora incluye una elevación (translateY + sombra
de elevación), no solo un cambio de color de borde.</li>
</ul>
</div>
</div>

<p class="doc-footer-meta">El historial real de componentes y tokens anterior a esta
fecha vive en los metadatos propios de recipe/changelog de cada componente
(<code>dtcg-vault/components/*/recipe.json</code>) y en el historial de git de este
repositorio — no se duplica aquí como una línea de tiempo de números de versión
inventada.</p>

<div class="closing-cta">
<div class="closing-cta__text"><h3>Obtenga la versión actual</h3>
<p>Cada token y componente anterior está hoy en producción en el registro — descargue
el paquete actual o explore el conjunto completo de tokens.</p></div>
<div class="closing-cta__actions">
<a href="/bundles/tokens" class="btn btn--secondary">Descargar tokens</a>
<a href="/tokens" class="btn btn--primary">Explorar el registro</a>
</div>
</div>
