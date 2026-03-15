from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return f"""
    <html>
      <head><title>CCWS CW1 - Task 1d</title></head>
      <body>
        <h1>CCWS Coursework 1 - Task 1d</h1>
        <p><b>Name:</b> Sara Nayab Khalid</p>
        <p><b>Student ID:</b> S2533781</p>
        <p><b>Access time:</b> {now}</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
