# Typography

Dos escalas tipográficas — Utility y Display — dividen la carga
tipográfica entre el texto funcional de UI y las superficies
expresivas.

## Las dos escalas

| Escala | Usar para | Tamaños |
|---|---|---|
| **Utility** | Texto de UI — cuerpo, etiquetas, leyendas, celdas de tabla, etiquetas de botón | 4 pasos (12/14/16/16-bold) |
| **Display** | Tipografía expresiva — subencabezados, encabezados de sección, títulos de página, hero | 4 pasos (20/24/32/42) |

La división es estructural, no decorativa. El texto Utility usa un
espaciado entre letras optimizado para la legibilidad en pantalla a
tamaños pequeños; el texto Display usa espaciado entre letras
negativo para un ritmo de encabezado más ajustado y con más
carácter. Mezclar escalas (usar Utility-3 como encabezado, o
Display-1 como etiqueta de botón) rompe la jerarquía visual del
sistema.

## Pila de fuentes

El substrato distribuye Inter como la sans-serif canónica, con una
cadena de respaldo de pila de sistema:

```
'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif
```

Inter es un tipo de letra moderno, de código abierto y de uso
intensivo (SIL OFL 1.1), optimizado para el renderizado de UI a
tamaños pequeños. La pila de respaldo del sistema asegura que el
substrato sea completamente funcional incluso si el binario de
Inter no se carga — la degradación es elegante.

Un tema de inquilino puede sustituir cualquier familia tipográfica
en la capa primitiva. Sustituciones comunes:

- IBM Plex Sans (código abierto)
- Source Sans 3 (Adobe, código abierto)
- Public Sans (dominio público)
- El tipo de letra propio de la marca del inquilino

El autoalojamiento del binario de la fuente es responsabilidad del
cliente; el substrato referencia la familia por nombre.

## La escala

### Utility

| Token | Tamaño / Interlineado / Peso | Usar para |
|---|---|---|
| `typography.utility-1` | 12 / 16 / 400 | Leyenda, etiqueta, celda de tabla |
| `typography.utility-2` | 14 / 20 / 400 | Cuerpo secundario, texto de ayuda |
| `typography.utility-3` | 16 / 24 / 400 | Piso de cuerpo primario |
| `typography.utility-4` | 16 / 24 / 600 | Encabezado de UI, etiqueta de botón |

### Display

| Token | Tamaño / Interlineado / Peso | Usar para |
|---|---|---|
| `typography.display-1` | 20 / 28 / 500 | Subencabezado |
| `typography.display-2` | 24 / 32 / 500 | Encabezado de sección |
| `typography.display-3` | 32 / 40 / 400 | Título de página |
| `typography.display-4` | 42 / 50 / 300 | Hero / landing |

## Jerarquía de encabezados

| HTML | Token |
|---|---|
| `<h1>` | `display-3` |
| `<h2>` | `display-2` |
| `<h3>` | `display-1` |
| `<h4>` | `utility-4` |
| Cuerpo `<p>` | `utility-3` |
| `<small>`, ayuda, leyenda | `utility-2` |

Un salto de nivel de encabezado (h1 → h3 sin h2 de por medio) rompe
la accesibilidad — los lectores de pantalla dependen de la
jerarquía para navegar. El substrato aplica esto en el trabajo de
auditoría de un hito posterior.

## Voz de marca

La voz, el registro y la disciplina de vocabulario se rigen por el
paquete de guía de estilo editorial (montado en
`/bundles/editorial-style-guide`), no por este tema. El tema de
marca solo transporta datos visuales, de tokens y de accesibilidad.
