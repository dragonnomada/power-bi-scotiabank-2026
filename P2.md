# Curso de Power BI para Scotiabank

![scotiabank](https://mma.prnewswire.com/media/1004365/Scotiabank_Scotiabank_delivers_Ultimate_value_and_rewards_with_t.jpg?p=facebook)

> Alan Badillo Salas

## Práctia 2

En esta *Práctica 2* analizaremos el modelo de avance de los financiamientos basados únicamente en las fechas de pago esperados y realizados.

Sigue los pasos para completar la práctica y responde las preguntas de análisis.

> API de Ventas y Pagos

[https://sandbox.geocarta.org/api/cursos/powerbi/lab/ventas](https://sandbox.geocarta.org/api/cursos/powerbi/lab/ventas)

[https://sandbox.geocarta.org/api/cursos/powerbi/lab/pagos](https://sandbox.geocarta.org/api/cursos/powerbi/lab/pagos)

> JSON de Ventas y Pagos

[ventas.json](./practica2/ventas.json)

[pagos.json](./practica2/pagos.json)

> Pasos de la *Práctica 2*

1. Carga el modelo y los informes de [Práctica 2 - Inforeme.pbix](./practica2/Practica2_informes.pbix)
2. Analiza las tablas `factAvanceResumidoHistorial` y `factAvanceResumidoVenta`
3. Determina qué informes puedes producir de `factAvanceResumidoVenta`
4. Revisa los medidores y evolución de pagos, cierres y avance
5. Revisa el informe sobre los días de mora
6. Revisa el informe de riesgos
7. Crea un KPI que explique el avance cumplido respescto al avance esperado en el resumido de `factAvanceResumidoHistorial`
8. Crea un KPI que explique el avance cumplido respescto al avance esperado en el resumido de `factAvanceResumidoVenta`
9. Crea un KPI que explique los pagos realizados respescto a los pagos esperados en el resumido de `factAvanceResumidoHistorial`
10. Crea un KPI que explique los pagos realizados respescto a los pagos realizados en el resumido de `factAvanceResumidoVenta` 

> Preguntas de análisis

- ¿Qué significa el avance esperado?
- ¿Qué significa el avance realizado?
- ¿Qué significan los pagos esperados?
- ¿Qué significa los pagos realizados?
- ¿Cómo podemos determinar el riesgo de una venta/financiamiento?
- Revisa el Excel [Pagos en riesgo.xlsx](./practica2/Pagos en riesgo.xlsx) y explica los riesgos expresados, ¿Cómo se determinaron y qué faltaría saber para determinar el dinero que está en riesgo?
- Basandonte en el mismo Excel de Riesgos ¿Cómo podemos determinar cuál es la sucursal y vendedor que mayor riesgo tiene en sus ventas/financiamientos?