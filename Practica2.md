# Curso de Power BI para Scotiabank

![scotiabank](https://mma.prnewswire.com/media/1004365/Scotiabank_Scotiabank_delivers_Ultimate_value_and_rewards_with_t.jpg?p=facebook)

> Alan Badillo Salas

## Práctia 2

En esta *Práctica 2* dominaremos el diseño de un *KPI* con *DAX*.

Sigue los pasos para completar la práctica y responde las preguntas de análisis.

> API de los Financiamientos

[https://sandbox.geocarta.org/api/cursos/powerbi/lab/financiera.csv](https://sandbox.geocarta.org/api/cursos/powerbi/lab/financiera.csv)

> CSV de los financiamientos

[financiera.csv](practica2/financiera.csv)

### Pasos de la *Práctica 2*

1. Carga los datos de la financiera ([financiera.csv](practica2/financiera.csv))
2. Reconstruye la tabla de hechos sobre los montos recibidos y esperados de las sesiones de clase ([S204.pbix](s204/S204.pbix))
3. Construye las medidas para el monto esperado acumulado y el monto recibido acumulado
4. Determina el porcentaje de recuperación (monto recibido acumulado entre monto esperado acumulado)
5. Calcula el *MoM* a 1 mes previo del pocentaje de recuperación
6. Calcula la media acumulada del porcentaje de recuperación
7. Diseña una meta que tome la media acumulada del porcentaje de recuperación multiplicada por 1 más el *MoM* del porcentaje de recuperación
8. Construye un *KPI* con el porcentaje de recuperación, el mes como tendencia y la meta

> Preguntas de análisis

- ¿En qué año se ve más constante el porcentaje de recuperación?
- ¿En qué año el porcentaje de recuperación baja en la mitad del año?
- ¿En qué año el porcentaje de recuperación baja desde principios del año?
- ¿Qué puedes concluir de este KPI?