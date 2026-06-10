import pandas

financiera = pandas.read_csv("financiera.csv")

print(financiera)

ventas = financiera.groupby("folio").agg(
    folio = ("folio", "median"),
    plan = ("plan", "first"),
    plazos = ("plazos", "median"),
    precio = ("precio", "median"),
    anticipo = ("anticipo", "median"),
    interes = ("interes", "median"),
    subtotal = ("subtotal", "median"),
    total = ("total", "median"),
    semanal = ("semanal", "median"),
    vendedor = ("vendedorOrigenFolio", "first"),
    sucursal = ("sucursalOrigenFolio", "first"),
)

print(ventas)

import pyodbc

driver = "ODBC Driver 18 for SQL Server"
server = "DESKTOP-IUGR5BT\\SQLEXPRESS"
database = "Financiera3"

print("Conectando a:",
      f"DRIVER={driver};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
        f"TrustServerCertificate=yes;"
)
conexion = pyodbc.connect(
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Trusted_Connection=yes;"
    f"TrustServerCertificate=yes;"
)

# ...
print("Abriendo el cursor")
cursor = conexion.cursor()

query = (
    "INSERT INTO dbo.ventas ("
    "   folio,"
    "   [plan],"
    "   plazos,"
    "   precio,"
    "   anticipo,"
    "   interes,"
    "   subtotal,"
    "   total,"
    "   semanal,"
    "   vendedor,"
    "   sucursal"
    ") VALUES ("
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?"
    ")"
)

values = ventas.itertuples(index=False)

# values = []

# for venta in ventas.itertuples(index=False):
#     print("venta:", venta)
#     values.append((
#         int(venta.folio),
#         venta.plan,
#         int(venta.plazos),
#         float(venta.precio),
#         float(venta.anticipo),
#         float(venta.interes),
#         float(venta.subtotal),
#         float(venta.total),
#         float(venta.semanal),
#         int(venta.vendedor),
#         int(venta.sucursal),
#     ))

cursor.fast_executemany = True
cursor.executemany(query, values)
cursor.commit()

print("Cerrando el cursor")
cursor.close()
# ...

print("Cerrando la conexion")
conexion.close()
print("Finalizado :D")