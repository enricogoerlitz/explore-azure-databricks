import os
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    return {}, 200


@app.route('/api/v1/healthcheck', methods=['GET'])
def healthcheck():
    print("Healthcheck request received")

    return jsonify({
        "host": "placeholder",
        "healthcheck": 200,
        "env": {
            "TEST_ENV": os.getenv("TEST_ENV", "not set")
        }
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
