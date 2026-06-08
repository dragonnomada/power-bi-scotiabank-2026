import numpy
import pandas

financiera = pandas.read_csv("financiera.csv")

print(financiera)

ventas = financiera.groupby("folio").agg(
    pagos = ("folio", "count"),
    plazos = ("plazos", "median"),
    precio = ("precio", "median"),
    anticipo = ("anticipo", "median"),
)

print(ventas)

ventas.to_csv("ventas.csv")