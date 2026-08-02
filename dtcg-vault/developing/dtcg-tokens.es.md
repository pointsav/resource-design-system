# Consumo de tokens DTCG

Los tokens se publican en el formato W3C Design Tokens Community Group (DTCG).

## Paquete completo

`GET /tokens.json` — devuelve el paquete completo de tokens, combinando la capa
primitive y las anulaciones semantic del tema activo.

## Paquete tipado por tema

`GET /api/tokens/{theme}.dtcg.json` — devuelve un paquete DTCG tipado, limitado a un
tema. El parámetro `{theme}` es el nombre de archivo en `vault/themes/` sin la
extensión `.json`. Para la instancia del proveedor: `pointsav-brand`.

## Registro shadcn

`GET /r/registry.json` — índice de registro compatible con shadcn. Las entradas de
componentes individuales están en `/r/{component}`. Funciona de fábrica con v0, Cursor,
Claude Code y Windsurf.

## Variables CSS

Cada token se asigna a una propiedad personalizada CSS. El conjunto completo de
variables está disponible en el código fuente de la página y en `/tokens.json` bajo la
clave de exportación `css`.
