# Proyecto 2 - Ruta B: Modelado Y DAX Para Cobranza

Profesor: M. Alan Badillo Salas

---

Este proyecto usa el archivo `financiera.csv` para construir una métrica DAX de cobranza.

La intención completa del proyecto sería crear un modelo analítico con tabla de hechos, dimensiones, calendario, relaciones y medidas avanzadas. Sin embargo, para una práctica de 1 hora se trabajará únicamente un punto concreto:

> Crear una medida DAX de mora acumulada por fecha esperada de pago.

---

# 1. Contexto Del Proyecto

El dataset contiene pagos esperados y pagos recibidos de financiamientos.

La granularidad práctica del archivo es:

```text
1 fila = 1 pago esperado o movimiento de amortización
```

Columnas importantes para esta actividad:

- `folio`: identificador del financiamiento.
- `pagoFechaEsperada`: fecha programada del pago.
- `pagoMontoEsperado`: monto esperado.
- `pagoMontoRecibido`: monto recibido.
- `pagoMontoFaltante`: monto pendiente.
- `pagado`: indicador de pago.
- `sucursalOrigenFolio`: sucursal de origen.
- `vendedorOrigenFolio`: vendedor de origen.

---

# 2. Pregunta De Negocio

La pregunta general del proyecto es:

> ¿Cómo evoluciona la mora en el tiempo?

Para esta sesión se reducirá a:

> ¿Cuál es el monto faltante acumulado hasta cada fecha esperada de pago?

---

# 3. Métricas Interesantes Para El Proyecto Completo

En una versión más amplia podrían construirse estas medidas:

- Mora acumulada.
- Monto esperado acumulado.
- Monto recibido acumulado.
- Porcentaje de recuperación.
- Promedio móvil de morosidad.
- Aging buckets: 0-7, 8-30, 31-60, 60+ días.
- Riesgo dinámico.
- Curva de recuperación.
- Mora por vendedor.
- Mora por sucursal.

Para esta práctica solo construiremos:

> Medida DAX: Mora Acumulada.

---

# 4. Teoría Mínima Necesaria

En Power BI, una columna calculada se calcula fila por fila.

Una medida DAX se calcula dependiendo del contexto del reporte.

Ejemplo:

```text
Si una gráfica está agrupada por fecha,
la medida se recalcula para cada fecha.
```

La mora acumulada necesita sumar el monto faltante desde el inicio del calendario hasta la fecha visible en la gráfica.

Ese patrón se conoce como acumulado o running total.

---

# 5. Resultado Esperado En 1 Hora

Al terminar, el estudiante deberá tener:

- Una tabla calendario `DimFecha`.
- Una relación entre `DimFecha[Fecha]` y `financiera[pagoFechaEsperada]`.
- Una medida base `Monto Faltante`.
- Una medida `Mora Acumulada`.
- Una gráfica de línea con la evolución de la mora acumulada.

---

# 6. Actividad Guiada: Crear La Medida Mora Acumulada

## Paso 1. Cargar El CSV

1. Abrir Power BI Desktop.
2. Seleccionar **Obtener datos**.
3. Elegir **Texto/CSV**.
4. Seleccionar `financiera.csv`.
5. Presionar **Cargar** o **Transformar datos** si se desea revisar tipos.

Verificar que:

- `pagoFechaEsperada` sea tipo fecha.
- `pagoMontoFaltante` sea número decimal.

---

## Paso 2. Crear Una Tabla Calendario

En Power BI:

1. Ir a **Modelado**.
2. Seleccionar **Nueva tabla**.
3. Escribir:

```DAX
DimFecha =
CALENDAR(
    MIN(financiera[pagoFechaEsperada]),
    MAX(financiera[pagoFechaEsperada])
)
```

Esta tabla genera una fila por cada fecha entre la primera y la última fecha esperada de pago.

---

## Paso 3. Crear Columnas Útiles En El Calendario

Seleccionar la tabla `DimFecha`.

Crear una nueva columna:

```DAX
Año = YEAR(DimFecha[Date])
```

Crear otra columna:

```DAX
Mes = FORMAT(DimFecha[Date], "YYYY-MM")
```

Nota: Power BI puede nombrar la columna de fecha como `Date`. Si se renombra a `Fecha`, usar `DimFecha[Fecha]` en lugar de `DimFecha[Date]`.

Para simplificar el resto de la práctica, se recomienda renombrar:

```text
Date -> Fecha
```

---

## Paso 4. Relacionar La Tabla Calendario

1. Ir a la vista de **Modelo**.
2. Arrastrar `DimFecha[Fecha]` hacia `financiera[pagoFechaEsperada]`.
3. Revisar que la relación sea:

```text
DimFecha[Fecha] 1 -> * financiera[pagoFechaEsperada]
```

4. Dirección de filtro:

```text
Única
```

Esto permite que las fechas filtren los pagos.

---

## Paso 5. Crear La Medida Base

Seleccionar la tabla `financiera`.

Crear una nueva medida:

```DAX
Monto Faltante =
SUM(financiera[pagoMontoFaltante])
```

Esta medida suma el monto pendiente según el filtro activo en el reporte.

---

## Paso 6. Crear La Medida De Mora Acumulada

Crear una nueva medida:

```DAX
Mora Acumulada =
CALCULATE(
    [Monto Faltante],
    FILTER(
        ALL(DimFecha[Fecha]),
        DimFecha[Fecha] <= MAX(DimFecha[Fecha])
    )
)
```

Interpretación:

```text
CALCULATE cambia el contexto de cálculo.
ALL quita el filtro de la fecha actual.
FILTER vuelve a aplicar todas las fechas menores o iguales a la fecha visible.
MAX toma la fecha actual del punto de la gráfica.
```

El resultado es una suma acumulada hasta cada fecha.

---

## Paso 7. Crear La Gráfica

1. Insertar un **Gráfico de líneas**.
2. En el eje X colocar:

```text
DimFecha[Fecha]
```

3. En valores colocar:

```text
Mora Acumulada
```

4. Cambiar el título del visual:

```text
Evolución de mora acumulada
```

5. Formatear el eje Y como moneda.

---

## Paso 8. Agregar Un Segmentador Opcional

Para hacer la gráfica más analítica:

1. Insertar un segmentador.
2. Agregar `sucursalOrigenFolio`.
3. Probar seleccionar una sucursal.

La medida se recalcula automáticamente porque DAX responde al contexto de filtro.

---

# 7. Validación Rápida

Para revisar si la medida tiene sentido:

1. Crear una tabla visual.
2. Agregar `DimFecha[Fecha]`.
3. Agregar `Monto Faltante`.
4. Agregar `Mora Acumulada`.

Se debería observar que:

- `Monto Faltante` muestra el monto de cada fecha.
- `Mora Acumulada` va sumando progresivamente.

---

# 8. Entregable

El estudiante debe entregar una captura o archivo `.pbix` con:

- Tabla calendario creada.
- Relación con `pagoFechaEsperada`.
- Medida `Monto Faltante`.
- Medida `Mora Acumulada`.
- Gráfica de línea por fecha.

---

# 9. Aplicaciones Futuras

La medida `Mora Acumulada` es solo el primer paso para construir un modelo analítico financiero.

Aplicaciones futuras:

- Crear una medida de monto recibido acumulado.
- Crear una curva de recuperación comparando esperado contra recibido.
- Construir un promedio móvil de mora de 4 semanas.
- Agregar una tabla de vendedores y una tabla de sucursales.
- Analizar la mora por cohortes de originación.
- Crear buckets de atraso: 0-7, 8-30, 31-60 y 60+ días.
- Usar relaciones activas e inactivas para comparar fecha esperada contra fecha recibida.
- Optimizar medidas DAX usando variables y tablas calendario bien modeladas.

---

# 10. Conclusiones

Este ejercicio muestra por qué DAX es más que sumar columnas.

La medida `Mora Acumulada` no solo agrega datos; cambia el contexto del cálculo para responder una pregunta temporal:

> ¿Cuánta mora se ha acumulado hasta este punto del tiempo?

El trabajo realizado permitió crear una tabla calendario, relacionarla con la fecha esperada de pago y construir una medida acumulada. Con esto, el estudiante practica una de las ideas más importantes de Power BI: las medidas dependen del contexto de filtro.

Este patrón se puede reutilizar para recuperación acumulada, ventas acumuladas, flujo esperado acumulado y comparación contra metas.
