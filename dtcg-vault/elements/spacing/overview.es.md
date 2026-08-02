# Spacing

Una escala de espaciado de 13 pasos sobre una base de 16px.
Numérica — de `space-1` a `space-13` — da una respuesta canónica
por cada decisión de layout.

## Escala

| Token | Valor | Uso común |
|---|---|---|
| `space-1` | 2px | Canaleta de línea fina (rara; usualmente solo bordes) |
| `space-2` | 4px | Espacio entre elementos en línea |
| `space-3` | 8px | Piso de ritmo entre párrafos; espacio icono-etiqueta |
| `space-4` | 12px | Relleno de campo de formulario |
| `space-5` | 16px | Unidad de rejilla del cuerpo; relleno de contenedor predeterminado |
| `space-6` | 24px | Relleno de tarjeta; ritmo vertical entre secciones |
| `space-7` | 32px | Canaleta de sección |
| `space-8` | 40px | Separación de sección más amplia |
| `space-9` | 48px | Corte de sección mayor |
| `space-10` | 64px | Sección de nivel de página |
| `space-11` | 80px | Sección de nivel de página (más holgada) |
| `space-12` | 96px | Sección de nivel de página (la más holgada) |
| `space-13` | 160px | Espaciado exclusivo de hero / landing page |

## Composición

Componga espaciados mayores a partir de la escala; nunca invente
valores fuera de escala:

- 4px + 12px + 4px = `space-2 + space-4 + space-2` para un campo
  con etiqueta
- Tarjeta con 24px de relleno: `space-6`
- Corte de sección con título arriba y contenido abajo a 32px
  cada uno: `space-7` × 2

Los valores fuera de escala (5px, 14px, 22px) rompen el ritmo y se
acumulan como desviación. La escala de 13 pasos es lo bastante
densa como para cubrir toda necesidad de layout sin recurrir a
valores fuera de escala.

## Piso de layout

El substrato usa una rejilla base de 16px (`space-5`). El texto de
cuerpo y los encabezados se alinean a múltiplos de 16px en su
cálculo de altura de línea; el relleno de contenedor se alinea a
múltiplos de 16px en el eje en línea. Esto es estructural — asegura
que el ritmo vertical permanezca consistente entre superficies.
