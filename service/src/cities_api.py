import http.client
import json
import os

RADPID_API_KEY = os.environ.get("RADPID_API_KEY")


conn = http.client.HTTPSConnection("wft-geo-db.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': RADPID_API_KEY,
    'X-RapidAPI-Host': "wft-geo-db.p.rapidapi.com"
    }

def check_rapid_api_key():
    if not isinstance(RADPID_API_KEY, str):
        print("RADPID_API_KEY is required")
        raise Exception("server not properly initialized")

def validate_int(value, name):
    assert isinstance(value, int), f"{name} must be an integer"
    assert value > 0, f"{name} must be above 0"

def format_cities(payload):
    formattedCities = []
    for d in payload["data"]:
        formattedCities.append({
            "id": d["id"],
            "city": d["city"],
            "country": d["country"]
        })
    return formattedCities

def get_available(min_population):
    validate_int(min_population, "min_population")
    check_rapid_api_key()
    conn.request("GET", f"/v1/geo/cities?minPopulation={min_population}", headers=headers)
    res = conn.getresponse()
    payload = res.read()

    formattedData = format_cities(json.loads(payload.decode("utf-8")))

    return formattedData


def get_near(city_id, radius):
    validate_int(city_id, "city_id")
    validate_int(radius, "radius")
    check_rapid_api_key()
    conn.request("GET", f"/v1/geo/cities/{city_id}/nearbyCities?radius={radius}", headers=headers)
    res = conn.getresponse()
    payload = res.read()

    formattedData = format_cities(json.loads(payload.decode("utf-8")))

    return formattedData
