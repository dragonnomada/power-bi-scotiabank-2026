import pandas

financiera = pandas.read_csv("financiera.csv")

print(financiera)

pagos = financiera[[
    "folio", 
    "numero",
    "concepto",
    "pagoFechaRecibido", 
    "pagoMontoRecibido", 
    "vendedorRecibeFolio", 
    "sucursalRecibeFolio"
]]

print(pagos)

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
    "INSERT INTO dbo.pagos ("
    "   folio,"
    "   numero,"
    "   concepto,"
    "   fecha,"
    "   monto,"
    "   vendedor,"
    "   sucursal"
    ") VALUES ("
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?,"
    "   ?"
    ")"
)

values = pagos.fillna(0).itertuples(index=False)

cursor.fast_executemany = True
cursor.executemany(query, values)
cursor.commit()

print("Cerrando el cursor")
cursor.close()
# ...

print("Cerrando la conexion")
conexion.close()
print("Finalizado :D")