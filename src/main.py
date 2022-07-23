from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

import src.cities_api as cities_api

app = FastAPI()

@app.exception_handler(AssertionError)
async def AssertionError(request: Request, exc: AssertionError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

@app.get('/endpoint/availableCities')
def get_available_cities(
            population: Union[int, None] = 1000000,
        ):
    return cities_api.get_available(population)

@app.get('/endpoint/nearCities')
def get_near_cities(
            city: int,
            radius: Union[int, None] = 100
        ):
    return cities_api.get_near(city, radius)

@app.get('/endpoint/listRequests')
def find_country_3():
    return 'test'
