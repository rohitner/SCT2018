from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
	return "Hello"

@app.route('/health')
def health():
	health = {'social': 'good', 'mental': 'moderate'}
	return jsonify(health=health)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)