from flask import Flask, jsonify, request
from flask_cors import CORS
from sct import runmain

import pickle as pk
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
	return "Hello"

@app.route('/api/health')
def health():
	try:
		userID = data['user']
		fbid = mappings[userID]
		with open('data_{}.pkl'.format(fbid), 'rb') as f:
			stored_data = pk.load(f)
	except Exception as e:
		stored_data = {'loginStatus': 'fail'}
		print("yahan ke error",e)
	health = {'social': 'good', 'mental': 'moderate'}
	return jsonify(health=health)


@app.route('/api/login', methods=['POST'])
def login():
	try:
		data = json.loads(request.data.decode('utf-8'))
		print(data)
		try:
			userID = data['user']
			fbid = mappings[userID]
			with open('data_{}.pkl'.format(fbid), 'rb') as f:
				stored_data = pk.load(f)
		except Exception as e:
			stored_data = {'loginStatus': 'fail'}
			print("yahan ke error",e)
		finally:
			return jsonify(stored_data)
	except Exception as e:
		print(e)
		return jsonify({'loginStatus':'fail'})


@app.route('/store_user', methods=['POST'])
def store_user():
	try:
		print(json.loads(request.data.decode('utf-8')))
		data = json.loads(request.data.decode('utf-8'))
		
		with open('{}.pkl'.format(data['userID']), 'wb') as f:
			pk.dump(data,f)
		return jsonify({'stat':'success'})
	except Exception as e:
		print(e)
		return jsonify({'stat':'fail'})

if __name__ == "__main__":
	with open('mappings.pkl','rb') as f:
		mappings = pk.load(f)
	app.run(host="0.0.0.0", port=5000, debug=True)