# Qué es el sistema de diseño de PointSav

El sistema de diseño de PointSav es un sustrato autoalojado y propiedad del cliente,
pensado para pymes que quieren lanzar interfaces coherentes, accesibles y legibles
por IA sin pagar precios de SaaS empresarial ni aceptar la voz de marca de un
hyperscaler.

El escaparate del proveedor en `design.pointsav.com` es la instancia canónica. Cada
cliente pyme que bifurca el sustrato ejecuta su propia instancia en su propio
dominio. Una sola base de código, una sola forma de despliegue, dos contextos.

## Qué hace

El sustrato transporta cinco elementos por inquilino, en un vault rastreado con Git
que el cliente posee:

- **Tokens** en el formato del W3C Design Tokens Community Group (especificación
  estable DTCG 2025.10) — capa primitiva (color, tipografía, espaciado, movimiento,
  foco), capa semántica (interactive-primary, surface-elevated, ...), ámbitos por
  componente
- **Componentes** como archivos de receta HTML+CSS+ARIA — agnósticos de framework;
  el framework de JS elegido por el cliente consume la receta, no al revés
- **Temas** — capas de anulación por marca que redirigen las referencias semánticas
  hacia las primitivas
- **Investigación** — justificación de decisiones de diseño legible por IA,
  justificaciones de accesibilidad, reglas de voz de marca
- **Exportaciones** — cachés derivadas (JSON de Figma Variables, configuración de
  Tailwind, variables CSS, builds de Style Dictionary)

El motor del sustrato lee el vault desde el disco y expone:

- Un escaparate público (este sitio) con la estructura que los profesionales de
  sistemas de diseño reconocen de su rol anterior
- Un paquete de tokens descargable a través de `/bundles/tokens/download`
- Un servidor JSON-RPC de Model Context Protocol en `POST /mcp` para que los agentes
  de IA consulten tokens, componentes e investigación en el momento de la
  decodificación
- Planificado: un paquete de tokens DTCG en vivo en `/tokens.json`, un registro
  compatible con shadcn en `/r/registry.json` (v0, Cursor, Claude Code, Windsurf), y
  una exportación DESIGN.md en `/api/design-<theme>.md` (especificación de Google de
  abril de 2026) — ninguno de estos tres está implementado todavía; no citarlos como
  ya lanzados

## Tres inversiones estructurales

El sustrato invierte el patrón de sistema de diseño de los hyperscalers en tres ejes
estructurales:

1. **La propiedad del cliente sustituye al alojamiento del hyperscaler.** El sistema
   de diseño reside en el repositorio Git del cliente, firmado con la clave del
   cliente, reproducible en cualquier herramienta. El costo de migración tiende a
   cero.

2. **La investigación como fuente canónica sustituye a la investigación como
   marketing.** El *porqué* reside en el mismo vault que el *qué*, en el mismo nivel
   legible por máquina, servido a través del mismo endpoint MCP. Los agentes de IA y
   los diseñadores humanos leen los mismos archivos.

3. **El agnosticismo de editor sustituye al bloqueo de editor.** DTCG es el
   denominador común. FIGMA mediante el plugin Tokens Studio, Penpot de forma
   nativa, Sketch mediante plugin, JSON escrito a mano — cualquier vía produce
   contenido de vault que el sustrato acepta.

## Quién usa el sustrato

- **Pymes sin un profesional de sistemas de diseño interno** — el sustrato les da la
  memoria muscular visual de un sistema de diseño maduro y de nivel productivo sin
  necesidad de contratar una agencia.
- **Sociedades holding, operadores de franquicias, revendedores de marca blanca** —
  el modelo de temas multiinquilino despliega un único sustrato a través de muchas
  marcas.
- **Pymes reguladas** (servicios financieros, salud, jurídico) — el patrón de
  certificación anclado en el cliente significa que el sistema de diseño forma parte
  de la superficie de auditoría del cliente, no de los controles SaaS del proveedor.
- **Equipos conscientes de la generación de código con IA** — cada generador de
  código (v0, Cursor, Claude Code, Windsurf) lee los endpoints MCP y de registro del
  sustrato en el momento de la decodificación. La interfaz generada coincide con la
  intención de marca de la pyme sin volver a decidir las mismas preguntas en cada
  sesión.

## Patrón de entrega y vocabulario

El *patrón de entrega* del sustrato — navegación con barra lateral, cuatro pestañas
canónicas por componente (Uso / Estilo / Código / Accesibilidad), vista previa en
vivo, código fuente vinculado a Git — sigue convenciones ampliamente reconocibles
en los sistemas de diseño de nivel productivo. La rampa cognitiva de acceso es
intencional: cualquier profesional que llegue desde un sistema comparable debería
orientarse en minutos.

El *vocabulario* del sustrato — nombres de tokens, recetas de componentes, archivos
de investigación — es original de PointSav, apoyado en sus propios valores y
estructura, no en la superficie de licenciamiento de ningún otro sistema. Inter se
distribuye por defecto; los inquilinos la sustituyen libremente.

## Lo que el sustrato NO es

- **No es un reemplazo de una herramienta de vista previa de componentes.** Un
  renderizador de vista previa paralelo puede coexistir de todos modos; el
  sustrato es dueño de su propio renderizado en cualquier caso.
- **No es un competidor de Figma / Penpot / Sketch.** Esos son editores de diseño;
  el sustrato es el almacén canónico con el que esos editores interoperan a través
  de DTCG.
- **No es una plataforma SaaS.** Es autoalojado por diseño.
- **No es una elección de framework de JS.** Los componentes son recetas
  HTML+CSS+ARIA; el framework elegido por el cliente consume la receta.
- **No es un artefacto de contenedor.** El sustrato se distribuye como binarios
  nativos desplegados mediante systemd. Sin Docker, sin Kubernetes, sin artefactos
  OCI.

## Hacia dónde ir después

- [Componentes](/components/button/usage) — la biblioteca de recetas de componentes
- [Color](/elements/color/overview) — el sistema de color
- [Tipografía](/elements/typography/overview) — las escalas tipográficas
- [GitHub](https://github.com/pointsav/pointsav-design-system) — bifurca el
  sustrato, abre un issue, aporta una receta
