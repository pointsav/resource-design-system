# Color

El sistema de color del substrato tiene tres capas — primitiva,
semántica y de componente. La marca de cada inquilino vive en la
capa semántica; las primitivas son estables entre inquilinos; los
componentes referencian semánticas, nunca primitivas directamente.

## Modelo de tres capas

```
   primitive    color.primary-60  →  #234ed8
        ↓
   semantic     interactive-primary  →  {color.primary-60}
        ↓
   component    button.background-default  →  {semantic.interactive-primary}
```

Un inquilino que quiere que su acción primaria sea turquesa en
lugar de azul solo sobreescribe la capa semántica:

```json
"interactive-primary": { "$value": "{color.brand-teal-60}" }
```

Los componentes no cambian. Las primitivas no cambian. La
sobreescritura se propaga a través de todo consumidor de
`interactive-primary`.

## Familias primitivas

El substrato distribuye cinco familias de color en la capa
primitiva. Los nombres son genéricos — describen un rol, no un
significado de negocio.

| Familia | Usar para | Pasos |
|---|---|---|
| **Neutral** | Fondos, bordes, tinta, divisores | 10–100 (10 pasos) |
| **Primary** | El color interactivo más prominente del inquilino | 10–90 |
| **Positive** | Estado exitoso, retroalimentación positiva | 10–70 |
| **Caution** | Problemas reversibles, estados por expirar | 10–70 |
| **Critical** | Fallos, acciones destructivas, errores | 10–70 |

Los números indican luminosidad — `10` es el más claro, `90`/`100`
es el más oscuro. Esta convención de escala por pasos es común en
los sistemas de color de nivel de producción, de modo que la
memoria muscular se transfiere sin importar de cuál sistema venga
un diseñador. Cada valor hexadecimal de esta escala es propio de
PointSav.

## Roles semánticos

La capa semántica mapea roles sobre primitivas. PointSav-brand
distribuye un mapeo canónico; los clientes SMB lo bifurcan.

### Ink (texto)

| Token | Usar para |
|---|---|
| `ink-primary` | Texto de cuerpo, encabezados sobre la superficie predeterminada |
| `ink-secondary` | Leyendas, texto de ayuda, copy de apoyo |
| `ink-on-interactive` | Texto sobre fondos interactivos |
| `ink-on-positive` / `-caution` / `-critical` | Texto sobre fondos de apoyo |
| `ink-disabled` | Controles deshabilitados |
| `ink-placeholder` | Texto de marcador de posición en inputs |

### Surface (fondo)

| Token | Usar para |
|---|---|
| `surface-base` | Fondo de página predeterminado |
| `surface-subtle` | Paneles con fondo, barras laterales |
| `surface-elevated` | Modales, popovers, capas sobre la página |
| `surface-inverse` | Inversiones de alto énfasis |

### Border

| Token | Usar para |
|---|---|
| `border-subtle` | Borde predeterminado entre secciones, tarjetas |
| `border-strong` | Divisor enfatizado, borde de input |
| `border-interactive` | Estado de foco / activo |

### Interactive (fondo)

| Token | Usar para |
|---|---|
| `interactive-primary` (+ hover, pressed, disabled) | Botones primarios, enlaces primarios |
| `interactive-secondary` (+ hover, pressed) | Botones secundarios |
| `interactive-ghost` (+ hover, pressed) | Botones ghost |
| `interactive-critical` (+ hover, pressed) | Acciones críticas / destructivas |

### Support (retroalimentación de estado)

| Token | Usar para |
|---|---|
| `support-positive` (+ -bg) | Estado exitoso |
| `support-caution` (+ -bg) | Problema reversible |
| `support-critical` (+ -bg) | Fallo |
| `support-info` (+ -bg) | Contexto neutral |

## Temas

Un tema de inquilino es un archivo `themes/<tenant>.json` que
sobreescribe la capa semántica. El substrato distribuye
`pointsav-brand.json`; los clientes SMB lo bifurcan.

Un inquilino puede distribuir varios temas:

- `<tenant>-light.json` y `<tenant>-dark.json` para el cambio de tema
- `<tenant>-seasonal-2026-q4.json` para campañas de tiempo acotado
- `<tenant>-acquisition-x.json` para expansiones de submarca

El futuro endpoint de composición de temas
(`GET /api/themes/compose?base=...&override=...`) permitirá que
varios temas se resuelvan en un solo paquete DTCG en el momento de
la solicitud — ver el objetivo de salto de la reclamación #38 de
Doctrine, L8.

## Piso de contraste WCAG

Las elecciones primitivas del substrato garantizan un contraste
WCAG 2.2 AAA (7:1) para los pares canónicos texto-sobre-superficie:

- `ink-primary` sobre `surface-base`: 14.7:1
- `ink-on-interactive` sobre `interactive-primary`: 7.4:1
- `ink-secondary` sobre `surface-base`: 8.9:1

Un tema de inquilino que sobreescriba primitivas por debajo del
piso WCAG 2.2 AA (4.5:1 texto normal, 3:1 texto grande) falla el
endpoint de auditoría (hito posterior). El substrato aplica el
piso; el inquilino elige todo lo que está por encima de él.
