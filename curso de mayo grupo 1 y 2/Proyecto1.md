# Proyecto 1 - Ruta A: Tablero De Riesgo Y Cobranza Operativa

Profesor: M. Alan Badillo Salas

---

Este proyecto usa el archivo `financiera.csv` para construir un tablero sencillo de cobranza en Power BI.

La intención completa del proyecto sería crear un dashboard para supervisores de cobranza y gerencia. Sin embargo, para una práctica de 1 hora se trabajará únicamente un punto concreto:

> Construir un KPI visual de monto vencido usando herramientas de Power BI, evitando DAX en la medida de lo posible.

---

# 1. Contexto Del Proyecto

Una financiera necesita revisar semanalmente qué parte de su cobranza está en riesgo.

Cada fila del CSV representa un movimiento o pago esperado dentro de una amortización. Algunas filas son anticipos y otras son pagos semanales.

Columnas importantes para esta práctica:

- `folio`: identificador del financiamiento.
- `concepto`: texto del pago, por ejemplo `Anticipo` o `Pago 1 de 35`.
- `pagoFechaEsperada`: fecha en la que se esperaba recibir el pago.
- `pagoFechaRecibido`: fecha real de recepción, si existe.
- `pagoMontoEsperado`: monto que debía pagarse.
- `pagoMontoRecibido`: monto realmente recibido.
- `pagoMontoFaltante`: monto pendiente.
- `pagado`: indicador de pago completado.
- `sucursalOrigenFolio`: sucursal donde se originó la venta.
- `vendedorOrigenFolio`: vendedor asociado al financiamiento.

---

# 2. Pregunta De Negocio

La pregunta general del proyecto es:

> ¿Dónde está creciendo la cartera en riesgo y quién debe actuar?

Para esta sesión se reducirá a una pregunta más pequeña:

> ¿Cuánto dinero vencido está pendiente de cobrar a la fecha de corte?

---

# 3. Ideas De KPIs Para El Proyecto Completo

Estas ideas pueden usarse para ampliar el tablero en una entrega posterior:

- Saldo vencido.
- Saldo vigente.
- Porcentaje de morosidad.
- Total financiado.
- Total recuperado.
- Monto faltante por sucursal.
- Monto faltante por vendedor.
- Número de pagos vencidos.
- Número de contratos con atraso.
- Flujo esperado semanal.
- Clientes liquidados.
- Contratos con riesgo crítico.

Para esta práctica solo construiremos:

> KPI: Saldo vencido a la fecha de corte.

---

# 4. Teoría Mínima Necesaria

Un KPI no es solo un número bonito. Un KPI debe responder una pregunta operativa.

Ejemplo:

```text
Métrica:
Monto faltante = suma de pagoMontoFaltante.

KPI:
Saldo vencido = monto faltante de pagos cuya fecha esperada ya pasó.

Decisión:
Priorizar cobranza sobre esos folios, vendedores o sucursales.
```

En Power BI se puede construir un KPI sin escribir una medida DAX si usamos:

- Power Query para preparar una columna de clasificación.
- Filtros visuales para quedarnos solo con pagos vencidos.
- Una tarjeta para sumar automáticamente el campo numérico.

---

# 5. Resultado Esperado En 1 Hora

Al terminar, el estudiante deberá tener una página de Power BI con:

- Una tarjeta con el `Saldo vencido`.
- Un gráfico de barras de `Saldo vencido por sucursal`.
- Una tabla con folio, fecha esperada y monto faltante.

---

# 6. Actividad Guiada: Construir El KPI Saldo Vencido

## Paso 1. Cargar El CSV

1. Abrir Power BI Desktop.
2. Seleccionar **Obtener datos**.
3. Elegir **Texto/CSV**.
4. Seleccionar el archivo `financiera.csv`.
5. Revisar que Power BI detecte las columnas.
6. Presionar **Transformar datos**.

---

## Paso 2. Revisar Tipos De Datos

En Power Query, verificar estos tipos:

| Columna | Tipo recomendado |
|---|---|
| `folio` | Texto o número entero |
| `pagoFechaEsperada` | Fecha |
| `pagoFechaRecibido` | Fecha |
| `pagoMontoEsperado` | Número decimal |
| `pagoMontoRecibido` | Número decimal |
| `pagoMontoFaltante` | Número decimal |
| `pagado` | Número entero |
| `sucursalOrigenFolio` | Texto o número entero |

Si una columna de fecha aparece como texto:

1. Seleccionar la columna.
2. Ir a **Transformar**.
3. Cambiar el tipo a **Fecha**.

Si una columna de monto aparece como texto:

1. Seleccionar la columna.
2. Cambiar el tipo a **Número decimal**.

---

## Paso 3. Crear Una Columna De Estado Sin DAX

Usaremos una fecha de corte fija para la práctica:

```text
Fecha de corte: 2026-05-18
```

En Power Query:

1. Ir a **Agregar columna**.
2. Seleccionar **Columna condicional**.
3. Nombre de la nueva columna:

```text
EstadoCobranza
```

4. Configurar la primera condición:

```text
Si pagoMontoFaltante es mayor que 0
y pagoFechaEsperada es anterior a 18/05/2026
entonces Vencido
```

5. En caso contrario:

```text
Vigente o pagado
```

Si la interfaz no permite agregar dos condiciones fácilmente, crear primero una condición sencilla:

```text
Si pagoMontoFaltante es mayor que 0 entonces Pendiente
Si no Pagado
```

Después se puede filtrar manualmente por fecha esperada dentro del reporte.

---

## Paso 4. Aplicar Cambios

1. Presionar **Cerrar y aplicar**.
2. Esperar a que Power BI cargue el modelo.

---

## Paso 5. Crear La Tarjeta Del KPI

1. En la vista de reporte, insertar una visualización de **Tarjeta**.
2. Arrastrar `pagoMontoFaltante` al campo de la tarjeta.
3. Verificar que la agregación sea **Suma**.
4. En el panel de filtros de la tarjeta, filtrar:

```text
EstadoCobranza = Vencido
```

5. Cambiar el título del visual a:

```text
Saldo vencido
```

6. Formatear el valor como moneda.

Este número representa el monto pendiente de pagos atrasados según la fecha de corte.

---

## Paso 6. Crear Un Gráfico Por Sucursal

1. Insertar un **Gráfico de barras agrupadas**.
2. En el eje, colocar:

```text
sucursalOrigenFolio
```

3. En valores, colocar:

```text
pagoMontoFaltante
```

4. Verificar que esté como **Suma**.
5. Filtrar el visual:

```text
EstadoCobranza = Vencido
```

6. Ordenar de mayor a menor por suma de `pagoMontoFaltante`.

Título sugerido:

```text
Saldo vencido por sucursal
```

---

## Paso 7. Crear Una Tabla Operativa

Insertar una tabla con estos campos:

- `folio`
- `concepto`
- `pagoFechaEsperada`
- `pagoMontoEsperado`
- `pagoMontoRecibido`
- `pagoMontoFaltante`
- `EstadoCobranza`

Aplicar el filtro:

```text
EstadoCobranza = Vencido
```

Ordenar por:

```text
pagoMontoFaltante descendente
```

Esto permite pasar del KPI general al detalle operativo.

---

# 7. Entregable

El estudiante debe entregar una captura o archivo `.pbix` con:

- Una tarjeta de `Saldo vencido`.
- Un gráfico de barras por sucursal.
- Una tabla de detalle de pagos vencidos.

---

# 8. Aplicaciones Futuras

Este ejercicio construye solo un KPI, pero puede convertirse en un tablero operativo más completo.

Aplicaciones futuras:

- Agregar segmentadores por `vendedorOrigenFolio`, `sucursalOrigenFolio` y `plan`.
- Construir una página gerencial con saldo vencido, saldo vigente y total recuperado.
- Agregar formato condicional a la tabla de pagos vencidos.
- Crear una clasificación de riesgo por monto faltante.
- Comparar sucursales para detectar dónde se concentra la cartera vencida.
- Separar pagos vencidos leves y severos usando rangos de días vencidos.
- Publicar el tablero en Power BI Service para compartirlo con supervisores.

---

# 9. Conclusiones

Este ejercicio muestra una idea central de analítica de negocio:

> Un dashboard no empieza con una gráfica. Empieza con una decisión.

En este caso, la decisión es identificar dónde concentrar la cobranza.

El trabajo realizado permitió pasar de un archivo CSV a una visualización accionable. Aunque se usó muy poco DAX, Power BI permitió construir un indicador útil mediante carga de datos, transformación básica, filtros y agregaciones visuales.

La conclusión principal es que un KPI sencillo puede tener mucho valor si responde una pregunta clara de negocio.
