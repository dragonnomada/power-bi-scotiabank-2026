# Curso de Power BI para Scotiabank

![scotiabank](https://mma.prnewswire.com/media/1004365/Scotiabank_Scotiabank_delivers_Ultimate_value_and_rewards_with_t.jpg?p=facebook)

> Alan Badillo Salas

## Práctia 1

En esta *Práctica 1* dominaremos el Power Query y el *Lenguaje M* para crear una tabla de hechos y una narrativa que permita determinar el porcentaje de recuperación de los financiamientos para el *Caso de Estudio* de la financiera.

Sigue los pasos para completar la práctica y responde las preguntas de análisis.

> API de los Financiamientos

[https://sandbox.geocarta.org/api/cursos/powerbi/lab/financiera.csv](https://sandbox.geocarta.org/api/cursos/powerbi/lab/financiera.csv)

> CSV de los financiamientos

[financiera.csv](practica1/financiera.csv)

> Excel de los financiamientos

[Financiera.xlsx](practica1/Financiera.xlsx)

### Pasos de la *Práctica 1*

> Paso 1 - Inspecciona el archivo de la Financiera para entender las columnas de interés que estaremos interactuando

![Paso 1](practica1/pasos/paso1.png)

> Paso 2 - O puedes el archivo CSV o el Excel

![Paso 2](practica1/pasos/paso2.png)

> Paso 3 - En el Excel se muestran las columnas de todos los pagos emitidos y esperados en la financiera

![Paso 3](practica1/pasos/paso3.png)

> Paso 4 - Carga los datos del CSV o Excel en PowerQuery de PowerBI

![Paso 4](practica1/pasos/paso4.png)

> Paso 5 - Crea una consulta nueva que parta de la tabla de la financiera para seleccionar únicamente el folio, número de pago y la fecha del pago recibido

![Paso 5](practica1/pasos/paso5.png)

> Paso 6 - Filtra los pagos con número de pago igual a 0

![Paso 6](practica1/pasos/paso6.png)

> Paso 7 - Quita la columna con el número de pago

![Paso 7](practica1/pasos/paso7.png)

> Paso 8 - Renombra la consulta como la fecha de anticipo para cada venta}
> 
> Ahora ya tenemos una tabla que explica por cada venta cuál es la fecha en la que se realizó su anticipo

![Paso 8](practica1/pasos/paso8.png)

> Paso 9 - Crea otra consulta nueva que parta de la venta y su fecha de anticipo

![Paso 9](practica1/pasos/paso9.png)

> Paso 10 - Combina los datos de la financiera

![Paso 10](practica1/pasos/paso10.png)

> Paso 11 - Extrae únicamente los plazos de cada fecha de anticipo

![Paso 11](practica1/pasos/paso11.png)

> Paso 12 - Seleccionando las tres columnas de folio, fecha de anticipo y plazos, reduce las ventas (dará el recuento)
> 
> Debería quedar una fecha de anticipo y plazos por cada venta

![Paso 12](practica1/pasos/paso12.png)

> Paso 13 - Ahora agrega una columna personalizada desde cero hasta el número de plasos:
> 
> `{0..[plazos]}`

![Paso 13](practica1/pasos/paso13.png)

> Paso 14 - Renombra la columna como número de pago esperado

![Paso 14](practica1/pasos/paso14.png)

> Paso 15 - Deja el número de pago esperado y la fecha de anticipo únicamente

![Paso 15](practica1/pasos/paso15.png)

> Paso 16 - Agrega otra columna personalizada que aumente las semanas dadas por el número de pago a la fecha de anticipo:
> 
> `Date.AddWeeks([fechaAnticipo], [numeroPagoEsperado])`

![Paso 16](practica1/pasos/paso16.png)

> Paso 17 - Quita la columna del anticipo y formatea la columna de la fecha de pago esperada como fecha
> 
> Esto generará la tabla de fechas de esperadas para cada pago

![Paso 17](practica1/pasos/paso17.png)

> Paso 18 - Crea una consulta partiendo de las fechas esperadas de los pagos

![Paso 18](practica1/pasos/paso18.png)

> Paso 19 - Combina la información de la financiera usando el folio y número de pago en cada lado

![Paso 19](practica1/pasos/paso19.png)

> Paso 20 - Recupera la fecha de pago recibido
> 
> Esto generará la tabla de fechas de pago esperados y recibidos para cada pago

![Paso 20](practica1/pasos/paso20.png)

> Paso 21 - Crea una consulta partiendo de las fechas de pago esperadas y recibidas

![Paso 21](practica1/pasos/paso21.png)

> Paso 22 - Agrega una columna personalizada con 1 si la fecha esperada y 0 sino
> 
> `if [fechaPagoEsperado] <= Date.From(DateTime.LocalNow()) then 1 else 0`

![Paso 22](practica1/pasos/paso22.png)

> Paso 23 - Agrega una columna personalizada con 1 si la fecha de pago recibido es distinto de vacío y 0 sino
> 
> `if [fechaPagoRecibido] <> null then 1 else 0`

![Paso 23](practica1/pasos/paso23.png)

> Paso 24 - Formatea las columnas
> 
> Ahora tenemos una tabla que explica si un pago es esperado y si está pagado

![Paso 24](practica1/pasos/paso24.png)

> Paso 25 - Crea una nueva consulta partiendo de los pagos esperados y recibidos

![Paso 25](practica1/pasos/paso25.png)

> Paso 26 - Extiende los datos de la financiera

![Paso 26](practica1/pasos/paso26.png)

> Paso 27 - Expande las columnas de anticipo, semanal y pagoMontoRecibido

![Paso 27](practica1/pasos/paso27.png)

> Paso 28 - preserva unicamente el folio, número de pago, anticipo y semanal

![Paso 28](practica1/pasos/paso28.png)

> Paso 29 - Agrega una columna llamada monto esperado que tenga el anticipo si el número de pago es 0 o el monto semanal sino

![Paso 29](practica1/pasos/paso29.png)

> Paso 30 - Deja únicamente las columnas del folio, número de pago, monto esperado y monto recibido
> 
> Ahora tenemos una tabla que explica por pago cuál es el monto esperado y el recibido

![Paso 30](practica1/pasos/paso30.png)

> Paso 31 - Crea una nueva consulta que parta de los montos esperados y recibidos de los pagos

![Paso 31](practica1/pasos/paso31.png)

> Paso 32 - Extiende los pagos esperados y recibidos

![Paso 32](practica1/pasos/paso32.png)

> Paso 33 - Reodena las columnas
> 
> Ahora tenemos la **Tabla de Hechos** sobre la recuperación de los pagos que explican los siguientes hechos:

- ¿Cuál es el folio del financiamiento?
- ¿Cuál es el número de pago?
- ¿Cuándo se esperaba el pago?
- ¿Cuándo se recibió el pago?
- ¿Era un pago esperado a la fecha actual?
- ¿Ya se recibió ese pago?
- ¿Cuánto se esperaba recibir en esa fecha?
- ¿Cuánto se recibió de lo esperado?

![Paso 33](practica1/pasos/paso33.png)

> Paso 34 - Crea un informe para detallar cuántos pagos se esperaban y cuántos se recibiero, además de los montos por cada año y mes
> 
> Este reporte explica la narrativa (objetivo de análisis):

- ¿Cuánto se esperaba recuperar y cuánto fue recuperado cada mes del año?
- ¿Cuánto se ha recuperado en total?

![Paso 34](practica1/pasos/paso34.png)

> Paso 35 - Agrega un filtro y medidor para determinar únicamente los pagos esperados y mostrar las sumas en el formato adecuado (Moneda / Español México)
> 
> **Nota:** Por defecto la moneda podría ser Español Latinoamérica y mostrar XDR

![Paso 35](practica1/pasos/paso35.png)

> Paso 36 - Crea una medida visual o medida DAX que calcule la suma del monto recibido entre la suma del monto esperado

![Paso 36](practica1/pasos/paso36.png)

> Paso 37 - En el formato condicional se pueden establecer íconos de indicación

![Paso 37](practica1/pasos/paso37.png)

> Paso 38 - Observa que en amarillo quedan entre el 41% y 81% de recuperación, mientras que una tercera parte de los financiamientos no han cubierto ni el 41% de del monto esperado

![Paso 38](practica1/pasos/paso38.png)

> Paso 39 - La medida visual se puede agregar como nuevo cálculo visual personalizado

![Paso 39](practica1/pasos/paso39.png)

> Paso 40 - Ingresa el monto recibido

![Paso 40](practica1/pasos/paso40.png)

> Paso 41 - Divide entre el monto esperado

![Paso 41](practica1/pasos/paso41.png)

> Paso 42 - Formatea el eje como porcentaje en el formato visual general

![Paso 42](practica1/pasos/paso42.png)

> Paso 43 - Usa el formato condicional sobre el eje para poner barras o íconos

![Paso 43](practica1/pasos/paso43.png)

> Paso 44 - Configura los colores de semáforo o barras

![Paso 44](practica1/pasos/paso44.png)

> Paso 45 - Visualiza diferentes formas que expliquen mejor los resultados del eje

![Paso 45](practica1/pasos/paso45.png)

> Preguntas de análisis

- ¿Cuál es el objetivo de análisis de la narrativa esperada?
- ¿Qué hechos son necesarios para construir la narrativa?
- ¿Cuál es el indicador que explica el objetivo de análisis de la narrativa?
- ¿Cómo explicas la caída del porcentaje de recuperación los últimos meses?