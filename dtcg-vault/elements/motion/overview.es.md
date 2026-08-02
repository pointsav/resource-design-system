# Motion

El movimiento comunica causalidad. El substrato distribuye cuatro
curvas de easing y seis pasos de duración. Combínelos según la
clase de interacción.

## Curvas de easing

| Token | Curva | Usar para |
|---|---|---|
| `motion.ease-utility` | `cubic-bezier(.2, 0, .4, 1)` | Interacciones productivas — botones, inputs, pestañas |
| `motion.ease-display` | `cubic-bezier(.4, .14, .3, 1)` | Interacciones expresivas — toasts, modales, hero |
| `motion.ease-enter` | `cubic-bezier(0, 0, .4, 1)` | Elemento apareciendo |
| `motion.ease-exit` | `cubic-bezier(.2, 0, 1, 1)` | Elemento desapareciendo |

Las curvas productivas están diseñadas para duraciones cortas
(≤200ms); las curvas expresivas funcionan con duraciones más largas
(≥320ms), donde el peso adicional es perceptible.

## Pasos de duración

| Token | Valor | Usar para |
|---|---|---|
| `duration.speed-1` | 70ms | Imperceptible — hover de color |
| `duration.speed-2` | 120ms | Rápido — pulsación de botón, anillo de foco |
| `duration.speed-3` | 200ms | Ágil — cambio de pestaña |
| `duration.speed-4` | 320ms | Suave — aparición de toast, deslizamiento de drawer |
| `duration.speed-5` | 480ms | Ponderado — entrada de modal |
| `duration.speed-6` | 720ms | Deliberado — animación hero |

## Movimiento reducido

`prefers-reduced-motion: reduce` se respeta en todas las capas de
interacción. Las recetas de componentes se distribuyen con la
sobreescritura por media query incluida; los consumidores la
heredan. No omita la sobreescritura — los usuarios sensibles al
movimiento han optado explícitamente por excluirse.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Antipatrones

- Animaciones que bloquean la entrada del usuario (modales que
  aparecen con fundido durante 700ms mientras el foco no puede
  recibirse). La entrada de un modal es `speed-5` para lo visual;
  el foco se mueve de inmediato con duración 0.
- Movimiento decorativo que añade tiempo a una tarea productiva.
  Reserve el movimiento expresivo para momentos que ameriten la
  atención del usuario.
- Duraciones fuera de escala (350ms, 500ms). La escala de 6 pasos
  cubre toda clase de interacción.
