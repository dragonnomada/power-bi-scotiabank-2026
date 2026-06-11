# Curso de Power BI para Scotiabank

![scotiabank](https://mma.prnewswire.com/media/1004365/Scotiabank_Scotiabank_delivers_Ultimate_value_and_rewards_with_t.jpg?p=facebook)

> Alan Badillo Salas

## Asesoría 1

## Resumen

En esta asesoría se resolvió cómo hacer el conteo de horas evitando fines de semana de una fecha inicial a una fecha final.

### Pasos para el cálculo de fechas de la inicial a la final

1. Determinar las horas totales entre las dos fechas con `= Duration.TotalHours([fechaB] - [fechaA])`
2. Redondear hacia arriba las horas totales con `Number.RoundUp([diferenciaHoras])`
3. Expandir las horas como una lista con `{0...[diferenciaHoras2]}`
4. Calcular la fecha intermedia por cada hora de la lista con `fechaA + #duration(0, [hora], 0, 0)`
5. Determinar el día de la semana de la fecha intermedia con `Date.DayOfWeek([fechaIntermedia])`
6. Determinar si el día es entre semana en la fecha intermedia (sábado - 5, domingo - 6) con `if Number.From([dia]=5) + Number.From([dia]=6) > 0 then 0 else 1`
7. Calcular el excedente si la fecha intermedia supera a la fecha final con `if Duration.TotalHours([fechaIntermedia] - [fechaB]) > 0 then Duration.TotalHours([fechaIntermedia] - [fechaB]) else 0`
8. Determinar las horas que se sumarán quitando el excedente con `= [entreSemana] - [horasExcedentes]`
9. Agrupar por índice y reducir sumando las horas con `AGRUPAR(indice) -> SUMA([horasSuma]), MEDIANA([fechaA]), MEDIANA([fechaB])`

Con esto tendremos la expansión y contracción para el cálculo de la suma de horas desde una **Fecha A** hasta una **Fecha B** sin contar los fines de semana.
