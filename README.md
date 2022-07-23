# starting with docker-compose

## build and start
Requires `docker-compose` and a subscription on [RapidAPI](https://rapidapi.com/).

```
RADPID_API_KEY=[your-subscription-key-here] docker-compose up --build
```

## browsing and using API
Once the container is running you should be able to visit [http://0.0.0.0/docs](http://0.0.0.0/docs) to get an overview of the API and to interactively test the endpoints.

You will also find some curl-scripts in the project root.

# developing
Requires `python` and a subscription on [RapidAPI](https://rapidapi.com/).
```
RADPID_API_KEY=[your-subscription-key-here] uvicorn src.main:app --reload
```

# running the tests
Requires `python`.
```
cd service && \
pip install -r requirements.txt && \
pytest ./test_all.py
```

