Tokens de formato de impresión/documento para documentos regulados — geometría de
página, una escala de cuatro pasos de grosor de regla, tipografía de dos niveles y
contadores de paginación. Consolidados a partir de borradores reales, fundamentados en
producción, de tres subdominios de documentos: contratos legales, estados financieros y
navegación interactiva en PDF. Los valores de dimensión usan pt/in/cm — este es el
primer dominio de tokens nativo de impresión de este sistema de diseño, y el borrador
DTCG 2025-10 documenta su conjunto de unidades de dimensión solo como px/rem, de modo
que pt/in/cm son una extensión deliberada y documentada del dominio de impresión que el
CSS de impresión impulsado por estos tokens realmente necesita.

## Qué tokeniza Paper

<div class="card-grid">
<div class="card"><span class="card__eyebrow eyebrow">Geometría</span><h3>Geometría de página</h3>
<p>Dimensiones de tamaño Carta, márgenes por familia de documento
(estándar/estrecho/ancho/encuadernación/portada), distancias de encabezado y pie de
página — todos valores reales de producción, no valores por defecto.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Reglas</span><h3>Escala de grosor de regla</h3>
<p>Una escala de grosor de borde de 4 pasos (0.5pt–1.5pt) compartida de forma idéntica
entre las tres familias legales y ambas familias de estados financieros — la primitiva
más sólida encontrada en todas las fuentes de Paper.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Tipografía</span><h3>Tipografía de dos niveles</h3>
<p>Cada familia de documento combina una tipografía serif de lectura para el cuerpo y
los encabezados con una tipografía sans distinta reservada para las zonas de
llenado de formulario — nunca la misma tipografía para ambos roles.</p></div>
<div class="card"><span class="card__eyebrow eyebrow">Paginación</span><h3>Contadores de paginación</h3>
<p>Primitivas de coordenadas reales para la capa de tabla de contenidos del
encuadernador PDF interactivo — posición, paso, altura y ancho de entrada — que
impulsan una capa de navegación real, no una maqueta.</p></div>
</div>

## Escala de grosor de regla

La escala central de 4 pasos, idéntica en todas las familias legales y de estados
financieros:

<div class="rule-ladder">
<div class="rule-ladder__item"><span class="rule-ladder__label">línea capilar · 0.5pt</span><hr class="rule-ladder__sample" style="border-top-width: 0.5pt;"></div>
<div class="rule-ladder__item"><span class="rule-ladder__label">ligera · 0.75pt</span><hr class="rule-ladder__sample" style="border-top-width: 0.75pt;"></div>
<div class="rule-ladder__item"><span class="rule-ladder__label">estándar · 1pt</span><hr class="rule-ladder__sample" style="border-top-width: 1pt;"></div>
<div class="rule-ladder__item"><span class="rule-ladder__label">énfasis · 1.5pt</span><hr class="rule-ladder__sample" style="border-top-width: 1.5pt;"></div>
</div>

Línea capilar: bordes de tabla de términos clave, reglas de encabezado corriente,
reglas de subtotal estatutario. Ligera: encierros de línea de llenado, reglas de
subtotal de informe financiero. Estándar: celdas de formulario, líneas de firma,
reglas superiores de gran total. Énfasis: cuadros de advertencia, reglas de portada,
bordes de página de resumen. Dos familias extienden aún más la escala — la fila de
total de una tabla de datos de prospecto usa una regla doble de 2pt, y la barra de
énfasis de nota de formulario de un conjunto de agencia usa 3pt.

## Tipografía de dos niveles

Cada familia de documento mantiene el texto de lectura y las zonas de llenado de
formulario en tipografías deliberadamente distintas — un campo de llenado nunca debe
confundirse con el texto impreso del cuerpo.

<div class="type-sample-grid">
<div class="type-sample"><div class="type-sample__label">Texto del cuerpo — contrato de suscripción</div>
<p class="type-sample__text" style="font-family: 'Times New Roman', 'Liberation Serif', Times, serif; font-size: 9.5pt; font-weight: 400; line-height: 1.28;">This Subscription Agreement is entered into as of the date set forth below, by and between the parties identified in the signature block, for the purpose of subscribing to the securities described herein.</p></div>
<div class="type-sample"><div class="type-sample__label">Etiqueta de llenado — contrato de suscripción</div>
<p class="type-sample__text" style="font-family: Verdana, Tahoma, 'DejaVu Sans', sans-serif; font-size: 10pt; font-weight: 400; line-height: 1.35;">Subscriber name: ______________________<br>Date: ____ / ____ / ______<br>Signature: ______________________</p></div>
</div>

## Familias de documentos

<div class="doc-table-scroll">
<table class="doc-table">
<thead><tr><th>Familia</th><th>Margen de página</th><th>Tipografía del cuerpo</th></tr></thead>
<tbody>
<tr><td>Contrato legal (suscripción)</td><td>0.75in estándar, 0.7–0.9in encuadernación</td><td>Times New Roman / Liberation Serif, 9.5pt</td></tr>
<tr><td>Prospecto</td><td>0.75in estándar, 0.625in en línea</td><td>Times New Roman / Liberation Serif, 10pt</td></tr>
<tr><td>Conjunto de agencia</td><td>1in ancho</td><td>Tinos / Times New Roman, 11.5pt</td></tr>
<tr><td>Estado financiero (cierre de ejercicio)</td><td>1in ancho</td><td>Calibri / Carlito, sans estatutaria</td></tr>
<tr><td>Diseño de informe financiero</td><td>2cm en línea, 1.5cm de bloque</td><td>system-ui (tema de panel)</td></tr>
<tr><td>Navegación de encuadernador PDF</td><td>zona de contenido de 72pt–540pt (US Letter, 612×792pt)</td><td>Helvetica / Arial, fuentes PDF core-14</td></tr>
</tbody>
</table>
</div>

<p class="doc-footer-meta">Detalle completo de tokens: <a href="/tokens#paper">Tokens — nivel Paper</a> (164 tokens hoja reales). Investigación de origen: <code>dtcg-vault/research/*-token-map.md</code> en el repositorio del sistema de diseño.</p>
