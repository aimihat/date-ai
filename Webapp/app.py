#!/usr/bin/python
# ! -*- coding: utf-8 -*-

import os
import sys
from importlib import reload
import io
import requests
import json
import base64


from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import (LoginManager, login_user, logout_user,
						 login_required, current_user)


from flask import Flask, request, session, g, redirect, url_for, abort, \
	render_template, flash, Markup, jsonify, make_response

from werkzeug.contrib.profiler import ProfilerMiddleware
from xlsxwriter.utility import xl_rowcol_to_cell

# Intitialize and configure Flask app.
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
	SECRET_KEY="#$dsfasdas943JHSs9dueidoijdf",  # secret key for signing sessions
))
app.config.from_envvar('APP_SETTINGS', silent=True)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.before_request
def before_request():
	"""
	Connect to the database before each request
	"""
	with open('session_count.txt', 'r') as f:
		g.session = int([x for x in f.readlines()][0])
	g.version = 1 #Used for updating cached assets in templates

@app.after_request
def after_request(response):
	return response


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		'''
		try:
			user = models.Users.get(models.Users.username == request.form['username'])
		except models.DoesNotExist:
			flash('Your username and password do not match!')
		else:
			if check_password_hash(user.password, request.form['password']):
				login_user(user)
				if user.is_admin:  # Redirects admin user to management page
					return redirect(url_for('user_management'))
				return redirect(request.args.get("next") or url_for('index'))
			else:
				flash('Your username and password do not match!')
		'''
		return redirect(url_for('index'))
	return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out!', 'success')
	return redirect(url_for('index'))

@app.route('/save_image', methods=['POST'])
def save_image():
	#print(request.form['image'].split(',')[1].decode('base64'))
	img_data = base64.b64decode(request.form['image'].split(',')[1])#.split(',')[1])
	directory = 'sessions/'+str(g.session)
	if not os.path.exists(directory):
		os.makedirs(directory)

	i = 0
	while os.path.exists(directory+'/'+str(i)+'.png'):
		i += 1

	with open(directory+'/'+str(i)+'.png', "wb") as fh:
		fh.write(img_data)
		
	return json.dumps(True)

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

@app.route('/audio_save', methods=['POST'])
def audio_save():
	print(request.form)
	return json.dumps(True)

@app.route('/camera')
def camera():
	with open('session_count.txt', 'w') as f:
		f.write(str(g.session+1))
	return render_template('camera.html')

@app.route("/")
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True, host='localhost', port=8200)
