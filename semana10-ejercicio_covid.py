import requests
import time
import json

URL = "http://api.covid19api.com/summary"

solicitud = requests.get (URL)

covid = solicitud.json()

if (solicitud.status_code==200):

    fechas = covid["Global"]["Date"]
    print(fechas)
    # formato = "%Y-%m-%dT%H:%M:%S.315Z"
    # fecha2 = time.strptime(fecha, formato)
    # fechaConvertida = f"La cadena original {fecha}, se parsea como {fecha2.tm_mday}/{fecha2.tm_mon}/{fecha2.tm_year} a las {fecha2.tm_hour}:{fecha2.tm_min}"

    # print(fechaConvertida)

cadenaFecha = "2021-06-28T10:22:00.82Z"
formato = "%Y-%m-%dT%H:%M:%S.82Z"
fecha = time.strptime(cadenaFecha, formato)
fechaConvertida = f"La cadena original {cadenaFecha}, se parsea como {fecha.tm_mday}/{fecha.tm_mon}/{fecha.tm_year} a las {fecha.tm_hour}:{fecha.tm_min}"

print(fechaConvertida)