from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

from db import *

app = Flask(__name__)
CORS(app)

client = create_client()
db = client["blinkpad"]
images = db.images


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
        print(record)
        res.append(record)

    return jsonify(res)


@app.route("/api/v1/image", methods=['POST'])
def update_count():
    request_data = request.get_json()

    img_id = request_data["imageId"]
    count = request_data["count"]

    if not img_id or not count:
        return "Please provide the valid body params", 400

    if img_id < 0 or count < 0:
        return "Please provide the values greater than 0", 400

    searchQuery = {"imageId": img_id}
    updateData = {
        "imageId": img_id,
        "count": count,
        "imageName": request_data["imageName"]
    }

    res = images.update_one(searchQuery, {"$set": updateData}, upsert=True)
    print(res.matched_count)

    return "Store updated for image " + str(img_id), 200


if __name__ == '__main__':
    app.run(debug=True)
