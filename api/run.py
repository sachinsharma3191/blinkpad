import os

from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
from pymongo import MongoClient

from config import *

DEFAULT_PORT = 9000

config = read_config()

host = config.get('database', 'MONGO_DB_HOST')
username = config.get('database', 'MONGO_DB_USER')
password = config.get('database', 'MONGO_DB_PASSWORD')

url = "mongodb+srv://" + username + ":" + password + "@" + host

client = MongoClient(url)
db = client["blinkpad"]
images = db.images
db = client.TaskManager

app = Flask(__name__)
CORS(app)


@app.route("/api/v1/image")
def get_all():
    data = images.find({}, {"_id": 0})
    res = []
    for record in data:
        res.append(record)

    return jsonify(res)


@app.route("/api/v1/image/<img_id>")
def get_count(img_id):
    res = []
    data = images.find({"imageId": int(img_id)}, {"_id": 0})

    if data.count() == 0:
        return jsonify({
            "message": "No  record found for image " + img_id
        }), 404

    for record in data:
        res.append(record)

    return jsonify(res)


@app.route("/api/v1/image", methods=['POST'])
def update_count():
    request_data = request.get_json()

    img_id = request_data["imageId"]
    count = request_data["count"]

    if img_id < 0:
        return "Please provide the values greater than 0", 400

    search_query = {"imageId": img_id}
    update_data = {
        "imageId": img_id,
        "count": count,
        "imageName": request_data["imageName"]
    }

    res = images.update_one(search_query, {"$set": update_data}, upsert=True)
    print(res.matched_count)

    return "Store updated for image " + str(img_id), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
