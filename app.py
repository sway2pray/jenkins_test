import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/v1/analyze', methods=['GET'])
def analyze_data():
    return jsonify({"status": "success", "signal": "BUY", "asset": "EUR/USD"})


if __name__ == '__main__':
    app_host = os.getenv('APP_HOST', '127.0.0.1')
    app_port = int(os.getenv('APP_PORT', 8888))
    app.run(host=app_host, port=app_port)
