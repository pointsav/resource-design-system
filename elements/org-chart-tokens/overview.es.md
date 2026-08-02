# Tokens de organigrama

Una extensión de paleta de colores para los organigramas corporativos de Woodfine.
Una familia de color gris cálido se agrega a la paleta de organigramas de Woodfine
existente usando el tratamiento matizado: borde de tono medio, relleno de fondo
saturado.

## Tratamiento matizado vs. pesado

La paleta Woodfine existente usa el tratamiento pesado — borde oscuro, fondo muy
pálido (p. ej. `token-blue-solid`, `token-green`). La extensión gris cálido
usa el tratamiento matizado — borde de tono medio, fondo matizado saturado.
El contraste visual entre los dos tratamientos es legible a simple vista y sobrevive
la impresión en escala de grises.

## Roles de entidad

| Clase CSS | Borde | Fondo | Rol de entidad |
|---|---|---|---|
| `token-warm-gray` | `#565151` | `#E5E0DB` | Sociedades holding, entidades pasivas por encima de la capa de gestión |

## Paleta completa de organigrama

Esta extiende la paleta completa. La fila en negrita es la adición gris cálido.

| Clase CSS | Borde | Fondo | Tratamiento | Familia de tono |
|---|---|---|---|---|
| `token-orange-solid` | `#E65100` | `#FFF3E0` | Sólido pesado | Naranja intenso |
| `token-blue-solid` | `#1565C0` | `#E3F2FD` | Sólido pesado | Azul |
| `token-blue-dashed` | `#1565C0` | `#E3F2FD` | Elipse discontinua pesada | Azul |
| `token-grey-solid` | `#757575` | `#EEEEEE` | Sólido pesado | Gris |
| `token-grey-dashed` | `#94A3B8` | `#F8FAFC` | Discontinuo | Pizarra |
| `token-green` | `#2E7D32` | `#F1F8E9` | Sólido pesado | Verde |
| `token-purple` | `#7B1FA2` | `#F3E5F5` | Sólido pesado | Púrpura |
| `token-olive` | `#827717` | `#F9FBE7` | Sólido pesado | Oliva |
| `token-yellow` | `#F57F17` | `#FFFDE7` | Elipse discontinua | Ámbar |
| **`token-warm-gray`** | **`#565151`** | **`#E5E0DB`** | **Sólido matizado** | **Gris cálido** |

## Paquete DTCG

Las definiciones legibles por máquina están en [`/tokens.full.json`](/tokens.full.json)
bajo `ibm-carbon-org-chart` (valores primitivos) y `org-chart-extended` (entradas
semánticas) — la clave del pilar `ibm-carbon-org-chart` está programada para un
cambio de nombre genérico como parte de la consolidación de árbol de tokens en curso;
esta página se actualizará cuando eso se complete. La geometría de la clase CSS
(210×110 px, 10 px de relleno, borde sólido) está en `components/nodes.css`.
