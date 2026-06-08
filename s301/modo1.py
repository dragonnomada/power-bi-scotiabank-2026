from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def home():
    return "Hola API de datos :)"

@api.get("/pagos")
def api_pagos():
    return [
        {
            "folio": 1,
            "fecha": "2026-01-01",
            "montoRecibido": 512.23
        },
        {
            "folio": 2,
            "fecha": "2026-01-03",
            "montoRecibido": 789.14
        },
        {
            "folio": 3,
            "fecha": "2026-01-15",
            "montoRecibido": 987.32
        },
    ]

import pandas

@api.get("/ventas")
def api_ventas():
    ventas = pandas.read_csv("ventas.csv")

    return [
        {
            "folio": folio,
            "pagos": pagos,
        }

        for index, folio, pagos, plazos, precio, anticipo in ventas.itertuples()
    ]