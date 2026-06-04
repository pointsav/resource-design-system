# Tokens de organigrama

Una extensión de paleta de colores para los organigramas corporativos de Woodfine.
Cuatro familias de colores de IBM Carbon se agregan a la paleta de organigramas de
Woodfine existente usando el tratamiento matizado: borde Carbon -70, relleno de fondo
Carbon -20.

## Tratamiento matizado vs. pesado

La paleta Woodfine existente usa el tratamiento pesado — borde oscuro, fondo muy
pálido (p. ej. `token-blue-solid`, `token-green`). Las cuatro extensiones de IBM
Carbon usan el tratamiento matizado — borde de tono medio, fondo matizado saturado.
El contraste visual entre los dos tratamientos es legible a simple vista y sobrevive
la impresión en escala de grises.

## Roles de entidad

| Clase CSS | Borde | Fondo | Rol de entidad |
|---|---|---|---|
| `token-magenta` | `#9F1853` | `#FFD6E8` | Promotor / gestión — distinción cálida de `token-purple` |
| `token-teal` | `#005D5D` | `#9EF0F0` | Socio General / Socio Limitado de SPV (SPV-GP, SPV-LP) |
| `token-red` | `#A2191F` | `#FFB3B8` | Entidades SPV que requieren distinción roja (p. ej. SPV-1 vs SPV-2) |
| `token-warm-gray` | `#565151` | `#E5E0DB` | Sociedades holding, entidades pasivas por encima de la capa de gestión |

## Paleta completa de organigrama

Estas cuatro extienden la paleta completa. Las filas en negrita son las adiciones de IBM Carbon.

| Clase CSS | Borde | Fondo | Tratamiento | Fuente |
|---|---|---|---|---|
| `token-orange-solid` | `#E65100` | `#FFF3E0` | Sólido pesado | Material Deep Orange |
| `token-blue-solid` | `#1565C0` | `#E3F2FD` | Sólido pesado | Material Blue |
| `token-blue-dashed` | `#1565C0` | `#E3F2FD` | Elipse discontinua pesada | Material Blue |
| `token-grey-solid` | `#757575` | `#EEEEEE` | Sólido pesado | Material Grey |
| `token-grey-dashed` | `#94A3B8` | `#F8FAFC` | Discontinuo | Tailwind Slate |
| `token-green` | `#2E7D32` | `#F1F8E9` | Sólido pesado | Material Green |
| `token-purple` | `#7B1FA2` | `#F3E5F5` | Sólido pesado | Material Purple |
| `token-olive` | `#827717` | `#F9FBE7` | Sólido pesado | Material Yellow oscuro |
| `token-yellow` | `#F57F17` | `#FFFDE7` | Elipse discontinua | Material Amber |
| **`token-magenta`** | **`#9F1853`** | **`#FFD6E8`** | **Sólido matizado** | **IBM Carbon** |
| **`token-teal`** | **`#005D5D`** | **`#9EF0F0`** | **Sólido matizado** | **IBM Carbon** |
| **`token-red`** | **`#A2191F`** | **`#FFB3B8`** | **Sólido matizado** | **IBM Carbon** |
| **`token-warm-gray`** | **`#565151`** | **`#E5E0DB`** | **Sólido matizado** | **IBM Carbon** |

## Paquete DTCG

Las definiciones legibles por máquina están en [`/tokens.full.json`](/tokens.full.json)
bajo `ibm-carbon-org-chart` (valores primitivos) y `org-chart-extended` (entradas
semánticas). La geometría de la clase CSS (210×110 px, 10 px de relleno, borde sólido)
está en `components/nodes.css`.
