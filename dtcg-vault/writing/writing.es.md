Tokens de gobernanza de la prosa — voz, ritmo, uso de mayúsculas, registro y plantillas
de exención de responsabilidad — por la misma razón que el color y el espaciado están
tokenizados: un estilo de casa decidido una vez debe poder aplicarse en todas partes, no
volver a discutirse en cada revisión de documento. Al igual que Paper, los tokens de
Writing se publican de forma genérica y sin vocabulario específico de un cliente; una
anulación de marca redirige el alias de la misma forma en que `themes/<brand>.json`
redirige el color.

## Voz

<div class="card-grid">
<div class="card"><span class="card__eyebrow eyebrow">Por defecto</span><h3>Voz activa</h3>
<p>Nombra al actor y la consecuencia. Postura por defecto para cada registro a
continuación.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Prospectivo</span><h3>Planeado / previsto / puede / objetivo</h3>
<p>Las capacidades que aún no son reales muestran su estado de forma visible — la
postura de divulgación de la BCSC, tokenizada para que sea mecánicamente exigible en
lugar de una frase de manual de estilo que alguien tiene que recordar.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Credibilidad</span><h3>Mecanismo, número, afirmación verificable</h3>
<p>Nunca tomar prestado el prestigio de una institución nombrada — respaldar una
afirmación con el mecanismo y un número real en su lugar.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Palabra concreta</span><h3>Preferir lo concreto sobre lo abstracto</h3>
<p><code>use</code> &gt; utilize &middot; <code>end</code> &gt; terminate &middot;
<code>explain</code> &gt; elucidate &middot; un número nombrado &gt; un cuantificador
vago.</p></div>
</div>

## Ritmo

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Regla</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Longitud de oración objetivo</td><td>15–20 palabras (promedio de la casa de 18 palabras)</td></tr>
<tr><td>Techo de oración de hecho consignado</td><td>25 palabras — un objetivo para una afirmación de definición/cumplimiento/legal, no un límite estricto</td></tr>
<tr><td>Longitud de párrafo</td><td>3–7 líneas; más allá de 7, un párrafo suele contener dos ideas</td></tr>
<tr><td>Densidad de encabezados</td><td>~1 encabezado por cada 120–140 palabras de cuerpo</td></tr>
<tr><td>Longitud de la entrada</td><td>100–400 palabras</td></tr>
</tbody>
</table>
</div>

## Uso de mayúsculas

El uso de mayúsculas en títulos, encabezados y slugs sigue una sola regla de forma
consistente: capitalizar solo la primera palabra más los nombres propios, siglas e
identificadores de código — nunca un paso de mayúscula-por-palabra genérico, y sin
artículo inicial ("el"/"la"/"un"/"una") en un título, encabezado o slug.

<div class="type-sample-grid">
<div class="type-sample"><div class="type-sample__label">Correcto</div>
<p class="type-sample__text">Designing with the token registry</p></div>
<div class="type-sample"><div class="type-sample__label">Incorrecto</div>
<p class="type-sample__text">The Designing With The Token Registry</p></div>
</div>

## Registro

Siete registros, cada uno vinculado a un perfil de contenido real en lugar de un "tono"
subjetivo:

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Registro</th><th>Postura</th></tr></thead>
<tbody>
<tr><td>how-to</td><td>Imperativo operativo</td></tr>
<tr><td>reference</td><td>Cláusula factual neutra</td></tr>
<tr><td>communications</td><td>Institucional</td></tr>
<tr><td>journal</td><td>Académico</td></tr>
<tr><td>legal</td><td>Vinculante en lenguaje llano</td></tr>
<tr><td>specialist</td><td>Normativo prescriptivo</td></tr>
<tr><td>financial-disclosure</td><td>Divulgación de cumplimiento precisa</td></tr>
</tbody>
</table>
</div>

Los perfiles de contenido combinan registros en lugar de elegir uno de forma aislada:
la documentación combina reference + how-to; las páginas corporativas y de proyecto se
leen como reference en su totalidad.

## Patrones de divulgación financiera

Cuatro patrones de prosa nombrados y reutilizables para la familia de documentos de
proforma de vehículo
([Financial Report Layout](/components/financial-report-layout/usage) /
[Proforma Vehicle Layout](/components/proforma-vehicle-layout/usage)) — cada uno
respaldado por un ejemplo real tomado de un documento que se publicó, no una copia
inventada. Más acotado que un registro (una postura) o una plantilla de exención de
responsabilidad (una cadena de relleno de espacio): un movimiento nombrado para una
situación recurrente específica.

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Patrón</th><th>Cuándo</th></tr></thead>
<tbody>
<tr><td>Base de preparación</td><td>El único párrafo de cierre de una proforma de vehículo — emisor, valor, tenencias, recuperación de costos, tratamiento fiscal, salvedad estructural, en ese orden.</td></tr>
<tr><td>Apertura de superposición de nota de formulario</td><td>El párrafo de apertura de una sección opcional/de escenario alternativo — qué asume el caso base, qué activa el escenario alternativo, qué se mantiene igual.</td></tr>
<tr><td>Cobertura prospectiva en línea</td><td>Cualquier proyección o cifra objetivo en línea — una cláusula, no una oración, que reutiliza el vocabulario de cobertura del pie de página BCSC a nivel de documento.</td></tr>
<tr><td>Suma fija, no condicionada a evidencia</td><td>Una tarifa fija cuyo encuadre de "reembolso" podría, de otro modo, implicar un requisito de documentación que no existe.</td></tr>
</tbody>
</table>
</div>

Detalle completo de cada patrón, con su ejemplo real de documento publicado: ver
`writing.semantic.pattern.financial-disclosure.*` en
[Tokens — nivel Writing](/tokens#writing).

## Patrón de etiqueta de entidad — referencia cruzada, no un token duplicado

Los diagramas de estructura corporativa (organigramas) tienen su propia convención de
etiquetado recurrente: nombre legal → código de registro (monoespaciado) → alias
definido (entre comillas, en cursiva) → jurisdicción (entre paréntesis) → ID de nodo.
Esa es una convención genuinamente propia de Writing, pero deliberadamente **no** es un
segundo token aquí — ya es la definición completa y autoritativa dentro de la propia
receta del componente
[Org Chart Print](/components/org-chart-print/usage) (las cinco zonas de etiqueta
apiladas). Un token de Writing paralelo que describiera la misma forma sería exactamente
el tipo de segunda copia que se ha desactualizado en otras partes de este sistema cada
vez que se ha intentado (hallazgo de reconciliación de registro del 2026-08-02) — así
que esto es un puntero, no una bifurcación. Lea la convención desde el componente.

## Plantillas de exención de responsabilidad

Cuatro plantillas reales y parametrizadas — los marcadores de posición se resuelven por
cliente, nunca codificados de forma fija a PointSav o Woodfine en la capa de tokens:

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Plantilla</th><th>Forma</th></tr></thead>
<tbody>
<tr><td>Prospectiva de valores</td><td><code>{corporate_entity} operates {technology_subsidiary} as {entity_relationship}...</code> — aviso de declaración prospectiva con cláusulas de riesgo material y de ausencia de obligación de actualización</td></tr>
<tr><td>Pie de página de marca registrada</td><td><code>{marks} are trademarks of {owner_entity}, used in {jurisdictions}...</code></td></tr>
<tr><td>Postura de privacidad</td><td><code>This interface operates on a {telemetry_scope} architecture.</code></td></tr>
<tr><td>Bloque de contacto</td><td><code>{role}, {entity}, {address}, {email}, {phone}</code></td></tr>
</tbody>
</table>
</div>

## Léxico — se publica vacío por diseño

Las listas de términos prohibidos/requeridos y de anclas temáticas son una estructura
real y definida sin **ninguna entrada genérica** — una anulación de marca aporta los
términos reales de la misma forma en que un archivo de tema redirige los alias de
color. Actualmente no hay ninguna lista de términos específica de PointSav o Woodfine
publicada aquí; esta página deliberadamente no inventa una.

## Ciclo de revisión

Un patrón editorial documentado: <code>draft-improves-draft</code> — cada pase de
revisión prepara el terreno para un siguiente pase claramente mejor, y un solo pase
revisa un nivel a la vez (estructura, luego párrafo, luego oración), de arriba hacia
abajo en lugar de mezclar niveles.

<p class="doc-footer-meta">Detalle completo de tokens: <a href="/tokens#writing">Tokens — nivel Writing</a>. Fuente: <code>dtcg-vault/writing/{primitive,semantic}.json</code> en el repositorio del sistema de diseño.</p>
