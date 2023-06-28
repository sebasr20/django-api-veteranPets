import requests
from django.core.cache import cache
import datetime

def obtener_dolar():
    url = "https://api.sbif.cl/api-sbifv3/recursos_api/dolar/2023/06?apikey=eba350313ffa85eb44616c08949737ca082d6fc3&formato=JSON"
    response = requests.get(url)
    data = response.json()

    dolares = data.get("Dolares", [])
    for dolar in dolares:
        fecha = datetime.datetime.strptime(dolar["Fecha"], "%Y-%m-%d").date()
        valor = float(dolar["Valor"].replace(",", "."))
        cache.set(f"dolar_{fecha}", valor)

    return "Datos del dólar almacenados en caché."
