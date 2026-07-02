from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/v1/analyze', methods=['GET'])
def analyze_data():
    return jsonify({"status": "success", "signal": "BUY", "asset": "EUR/USD"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
