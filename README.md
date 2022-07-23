# Running the service

## starting with docker

### build and start
Requires `docker-compose`

```
docker-compose up --build
```

### browsing and using API
Once the container is running you should be able to visit [http://0.0.0.0/docs](http://0.0.0.0/docs) to get an overview of the API and to interactively test the endpoints.

You will also find 2 scripts with example curl-requests in the project root. (`./example-request-1.sh` and `./example-request-2.sh`)

## running the tests
```
cd service && \
pip install -r requirements.txt && \
pytest ./test_all.py
```
