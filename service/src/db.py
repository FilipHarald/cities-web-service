import datetime
import os
from pymongo import MongoClient

MONGO_URL = os.environ.get("MONGO_URL") or "mongodb://root:pass@localhost:27017/"
client = MongoClient(MONGO_URL)

db = client.cities_api_service

def store_request(endpoint_name, req_browser):
    req_data = {
            "time": datetime.datetime.utcnow(),
            "browser": req_browser,
            "endpoint": endpoint_name
            }
    db.requests.insert_one(req_data)

def get_requests():
    return list(db.requests.find({}, {"_id": False}))
