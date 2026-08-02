# Accesibilidad

El sistema base tiene como objetivo WCAG 2.2 AAA. Cada receta de componente
se entrega conforme de fábrica; los arrendatarios que bifurcan el sistema
base heredan ese piso mínimo a menos que se desvíen en la capa primitiva.

## Compromisos de conformidad

- **WCAG 2.2 AAA** para el tema canónico de marca PointSav en cada receta
  de componente entregada
- **WCAG 2.2 AA como mínimo** para cualquier tema de arrendatario que
  anule primitivos — el endpoint de auditoría (hito posterior) marca las
  caídas por debajo de AA
- Alineación con **EN 301 549** para arrendatarios del sector público
  europeo
- Alineación con **Section 508** para arrendatarios del sector público de
  EE. UU.

## Lo que lleva cada componente

Cada receta en `dtcg-vault/components/` incluye una pestaña
`accessibility.md` que cubre:

1. **Estado de conformidad** — tabla criterio por criterio de WCAG
2. **Interacciones de teclado** — Tab, Shift+Tab, Espacio, Enter, teclas
   de flecha, Escape
3. **Comportamiento con lector de pantalla** — rol, nombre y valor
   anunciados
4. **Movimiento reducido** — se respeta `prefers-reduced-motion: reduce`
5. **Objetivos táctiles** — mínimo 44x44
6. **Independencia del color** — ningún estado se comunica solo mediante
   color
7. **Antipatrones** — desviaciones comunes y por qué rompen la
   accesibilidad

## El modelo de receta es estructuralmente accesible

El modelo de receta HTML+CSS+ARIA del sistema base es más conforme que
los modelos de bibliotecas de componentes en React porque:

- **Elementos HTML nativos primero.** `<button>` en lugar de `<div
  role="button">`. El elemento nativo aporta gratis el comportamiento de
  teclado y de lector de pantalla.
- **No requiere JS para activarse.** Botones, enlaces y controles de
  formulario funcionan sin que se cargue JavaScript — degrada con
  elegancia en conexiones lentas, bloqueadores de anuncios y errores de
  JS.
- **Sin secuestro de framework.** La receta no captura los eventos de
  teclado del usuario mediante eventos sintéticos de React; se disparan
  los eventos nativos del navegador.

## Piso mínimo ante anulaciones del arrendatario

Un arrendatario que bifurca el sistema base no puede desconfigurar el
piso mínimo de accesibilidad. Tres compromisos se aplican sin importar
las anulaciones de tema:

1. **El foco siempre es visible.** Las recetas de componente nunca
   establecen `outline: none` sin una alternativa.
2. **Los objetivos táctiles nunca están por debajo de 44x44.** Las
   recetas de componente incluyen el desplazamiento del anillo de foco
   dentro del área activable.
3. **El movimiento respeta `prefers-reduced-motion`.** Cada receta
   incluye la anulación por media query.

El endpoint de auditoría (hito posterior) marca las infracciones de
estos compromisos.

## Endpoint de auditoría (hito posterior)

`GET /api/audit/wcag?theme=<theme>` devolverá la conformidad WCAG por
componente para el tema indicado — relaciones de contraste, presencia de
anillo de foco, tamaños de objetivo táctil, cobertura de anulación de
movimiento. La respuesta es JSON apto para integración CI/CD (`exit 1`
en caso de falla) o para consumo por agentes de IA.

Hoy esta página es la declaración canónica de conformidad; el endpoint
de auditoría formaliza lo que ya es obligatorio.

## Dónde buscar

- Cada [componente](/components/button/usage) lleva su propia pestaña de
  Accesibilidad.
- [Color](/elements/color/overview) cubre el contraste en la capa
  primitiva.
- [Motion](/elements/motion/overview) cubre los patrones de movimiento
  reducido.
- [Tipografía](/elements/typography/overview) cubre la jerarquía de
  encabezados y la navegación con lector de pantalla.
