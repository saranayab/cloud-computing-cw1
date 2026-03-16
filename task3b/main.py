from flask import Flask, jsonify
from datetime import datetime, timezone
import requests

app = Flask(__name__)

BUCKET_NAME = "sara-bucket"
STUDENT_ID = "S2533781"

IMAGE_MAP = {
    "1": "image1.jpg",
    "2": "image2.jpg",
    "3": "image3.jpg"
}

@app.route("/")
def home():
    return jsonify({
        "message": "Task 3b metadata service",
        "available_routes": [
            "/info/1",
            "/info/2",
            "/info/3"
        ]
    })

@app.route("/info/<image_id>")
def get_image_metadata(image_id):
    if image_id not in IMAGE_MAP:
        return jsonify({
            "error": "Invalid image id. Use 1, 2, or 3."
        }), 404

    object_name = IMAGE_MAP[image_id]
    api_url = f"https://storage.googleapis.com/storage/v1/b/{BUCKET_NAME}/o/{object_name}"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        metadata = response.json()

        result = {
            "file_name": metadata.get("name"),
            "content_type": metadata.get("contentType"),
            "file_size_bytes": metadata.get("size"),
            "time_created": metadata.get("timeCreated"),
            "student_id": STUDENT_ID,
            "request_time": datetime.now(timezone.utc).isoformat()
        }

        return jsonify(result)

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Failed to fetch metadata from Cloud Storage API",
            "api_url": api_url,
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
