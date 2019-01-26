from flask import render_template, request, Response
from flask import json
from flask_jwt_extended import (
	create_access_token, create_refresh_token, 
	jwt_required, jwt_refresh_token_required, 
	get_jwt_identity, decode_token
)

import datetime
from datetime import timedelta
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Hasan'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
	
	
@app.route('/v1/user', methods=['POST'])
def user():
	if request.method == 'POST':
		data = request.get_json()
		username = data['username']
		print('Use Name: "{username}"'.format(username = username))
		print('Data Received: "{data}"'.format(data=data))
		
		response = app.response_class(
			response = json.dumps({ "id": 1, "result": "success" }),
			status = 201,
			mimetype = 'application/json'
		)
		return response

	
@app.route('/v1/authenticate', methods=['POST'])
def authenticate():
	if request.method == 'POST':
		data = request.get_json()
		print('Data Received: "{data}"'.format(data=data))
		
		access_token = create_access_token(identity = data['username'], expires_delta=None)
		
		payload = decode_token(access_token)
		expire_time = payload['exp']
		utc = datetime.datetime.utcfromtimestamp(expire_time)
		
		response = app.response_class(
			response = json.dumps({"token":access_token, "expire_at":utc}),
			status = 200,
			mimetype = 'application/json'
		)
		return response


@app.route('/v1/refresh-token', methods=['POST'])
def refreshToken():
	if request.method == 'POST':
		data = request.get_json()
		print('Data Received: "{data}"'.format(data=data))
		
		extend = timedelta(seconds=1800)
		
		access_token = create_access_token(identity = data['username'], expires_delta = extend)
		
		payload = decode_token(access_token)
		expire_time = payload['exp']
		utc = datetime.datetime.utcfromtimestamp(expire_time)
		
		response = app.response_class(
			response = json.dumps({"token":access_token, "expire_at":utc}),
			status = 200,
			mimetype = 'application/json'
		)
		return response
	
	
	
	
	
	
	
	
	
	
	
	
