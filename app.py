# save this as app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World UPCH!"

@app.route('/send_data', methods=['POST'])
def sent_data():
    if request.is_json:
        data = request.get_json()
        print(data)
        return 'JSON received', 200

