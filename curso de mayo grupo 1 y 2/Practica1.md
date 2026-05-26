# Curso de Power BI para Scotiabank

![scotiabank](https://mma.prnewswire.com/media/1004365/Scotiabank_Scotiabank_delivers_Ultimate_value_and_rewards_with_t.jpg?p=facebook)

> Alan Badillo Salas

## Práctia 1

En esta *Práctica 1* dominaremos la carga de tablas vía API o JSON mediante Power Query y el *Lenguaje M*.

Sigue los pasos para completar la práctica y responde las preguntas de análisis.

> API de Ventas y Pagos

[https://sandbox.geocarta.org/api/cursos/powerbi/lab/ventas](https://sandbox.geocarta.org/api/cursos/powerbi/lab/ventas)

[https://sandbox.geocarta.org/api/cursos/powerbi/lab/pagos](https://sandbox.geocarta.org/api/cursos/powerbi/lab/pagos)

> JSON de Ventas y Pagos

[ventas.json](./conjuntos/ventas.json)

[pagos.json](./conjuntos/pagos.json)

> Pasos de la *Práctica 1*

1. Crea un nuevo modelo en Power BI para adquirir los datos de las ventas y pagos desde el API o los archivos JSON (`Ventas` y `Pagos`)
2. Obtén la tabla cruzada entre ventas y pagos (`Pagos por venta`). Sugerencia: Crea una consulta combinada que cruce las `Ventas.folio` y los `Pagos.folio` de tipo externa izquierda
3. De los `Pagos por venta` deja las columnas del `folio`, `fechaEsperada` y `fechaPago`
4. De los `Pagos por venta` agrupa los folios para determinar la primera `fechaEsperada` (fecha en la que inicia el financiamiento o venta) y la última `fechaPago` (el último movimiento del financiamiento o venta). Sugerencia: Agrupa de forma avanzada los folios y genera dos agregaciones de mínimo y máximo para `fechaEsperada` como `fechaPrimerPago` y `fechaUltimoPago`
5. En `Pagos por venta` crea una columna personalizada que determine la diferencia entre la fecha de último pago y la fecha del primer pago. Sugerencia: En la columna personalizada usa `Duration.Days([fechaUltimoPago] - [fechaPrimerPago])` (no olvides ponerlo de tipo entero), esta columna será la de `diasAlUltimoPago`
6. En `Pagos por venta` crea una columna personalizada que determine la diferencia entre la fecha actual y la fecha del primer pago. Sugerencia: En la columna personalizada usa `Duration.Days(Date.now() - [fechaPrimerPago])` (no olvides ponerlo de tipo entero), esta columna será la de `diasTranscurridos`
7. En `Pagos por venta` crea una columna personalizada que determine la diferencia en días entre los días transcurridos y los días al último pago. Sugerencia: En la columna personalizada usa `[diasTranscurridos] - [diasAlUltimoPago]` (no olvides ponerlo de tipo entero), esta columna será la de `diasRetraso`
8. En `Pagos por venta` crea una columna personalizada que determine progreso entre los días transcurridos y los días al último pago. Sugerencia: En la columna personalizada usa `[diasAlUltimoPago] / [diasTranscurridos]` (no olvides ponerlo de tipo porcentaje), esta columna será la de `progresoDias`
9. Crea un informe sencillo que muestre por folio la comparación entre los `diasTranscurridos` y `diasAlUltimoPago`
10. Agrega otra gráfica que muestre por folio los `diasRetraso` y el `progresoDias`

> Preguntas de análisis

- Sabiendo que los pagos se esperan semanalmente, los días de retraso comúnmente podrían ser menores a 7 ¿Cómo se podrían calcular las semanas de retraso? y ¿Qué sería más significativo observar, días de retraso o semanas de retraso?
- Sabiendo que la venta posee la columna `plazos` que indica cuántas semanas espera recibir el financiamiento o venta ¿Cómo podemos medir el progreso total de los días del último pago y los días transcurrido?
- Sabiendo que la venta posee la columna `total` que indica cuánto dinero espera recibir el financiamiento o venta ¿Cómo podemos medir el progreso total de los los montos recibidos respecto el total esperado?
- Sabiendo que la venta posee la columna `total` que indica cuánto dinero espera recibir el financiamiento o venta, además de la columna `semanal` que indica cuánto se espera recibir cada semana ¿Cómo podemos medir el progreso esperado según las semanas que han transcurrido a la fecha respecto al total esperado? ¿Se necesitaría información adicional?