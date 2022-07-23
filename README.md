# Running the service

## starting with docker

### build and start
```
docker build -t ca-filip . && docker run -d --name cities-service -p 80:80 ca-filip
```

### browsing and using API
Once the container is running you should be able to visit [http://0.0.0.0/docs](http://0.0.0.0/docs) to get an overview of the API and to interactively test the endpoints.

You will also find 2 scripts with example curl-requests in the project root. (`./example-request-1.sh` and `./example-request-2.sh`)

## running the tests
1. `pip install -r requirements.txt`
2. `pytest ./test_all.py`
