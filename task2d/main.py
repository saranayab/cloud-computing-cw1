from flask import Flask, abort
from datetime import datetime

app = Flask(__name__)

CHOSEN_PATH = "view"  # URLs will be /view/1, /view/2, /view/3

IMAGES = {
    1: {
        "title": "Image 1 – Multi-Color Parrot",
        "url": "https://storage.googleapis.com/sara-bucket/image1.jpg",
        "caption": "This image is retrieved from the Cloud Storage bucket using its public URL, confirming correct object access configuration."
    },
    2: {
        "title": "Image 2 – Landscape View",
        "url": "https://storage.googleapis.com/sara-bucket/image2.jpg",
        "caption": "This image demonstrates integration between App Engine and Cloud Storage by serving an HTML response that embeds the stored object."
    },
    3: {
        "title": "Image 3 – Blue Human Eye",
        "url": "https://storage.googleapis.com/sara-bucket/image3.jpg",
        "caption": "This image confirms that multiple objects stored in the bucket can be accessed publicly and served through dynamic routing using different URL paths."
    }
}

@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Task 2d - Routes</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 30px; }}
            a {{ text-decoration: none; }}
            .box {{ max-width: 700px; margin: 0 auto; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Task 2d – Dynamic Image Routes</h1>
            <p>Select an image route below:</p>
            <ul>
                <li><a href="/{CHOSEN_PATH}/1">/{CHOSEN_PATH}/1</a></li>
                <li><a href="/{CHOSEN_PATH}/2">/{CHOSEN_PATH}/2</a></li>
                <li><a href="/{CHOSEN_PATH}/3">/{CHOSEN_PATH}/3</a></li>
            </ul>
        </div>
    </body>
    </html>
    """

@app.route(f"/{CHOSEN_PATH}/<int:image_id>")
def show_image(image_id: int):
    if image_id not in IMAGES:
        abort(404)

    item = IMAGES[image_id]
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{item['title']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin: 30px; }}
            img {{ max-width: 520px; width: 100%; border-radius: 10px; margin-top: 15px; }}
            .box {{ max-width: 700px; margin: 0 auto; }}
            .meta {{ color: #555; font-size: 14px; margin-top: 10px; }}
            a {{ display: inline-block; margin-top: 15px; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>{item['title']}</h1>
            <img src="{item['url']}" alt="{item['title']}">
            <p>{item['caption']}</p>
            <p class="meta">Path: /{CHOSEN_PATH}/{image_id} | Request time: {now}</p>
            <a href="/">← Back to home</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
