# TAD Fracción

**Dominio:** pares ordenados `(numerador, denominador)` de enteros, con denominador distinto de 0.

## Operaciones
- `crear(n, d) -> Fracción`: precondición `d ≠ 0`; representa `n/d`.
- `numerador(f) -> Entero`: devuelve el numerador sin modificar `f`.
- `denominador(f) -> Entero`: devuelve el denominador sin modificar `f`.
- `sumar(f1, f2) -> Fracción`: devuelve la suma.
- `simplificar(f) -> Fracción`: devuelve una equivalente con numerador y denominador coprimos.
- `restar(f1, f2) -> Fracción`: devuelve `f1 - f2`.
- `multiplicar(f1, f2) -> Fracción`: devuelve el producto.
- `sonIguales(f1, f2) -> Booleano`: compara el valor racional; por ejemplo `2/4` y `1/2` son iguales.
