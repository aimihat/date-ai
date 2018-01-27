#!/usr/bin/python
# ! -*- coding: utf-8 -*-

import os
import sys
from importlib import reload
import json
import datetime
import sqlite3
import csv
import io
import requests
import json
import subprocess

from flask import Flask, request, session, g, redirect, url_for, abort, \
	render_template, flash, Markup, jsonify, make_response

# for login
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import (LoginManager, login_user, logout_user,
						 login_required, current_user)

import numpy as np
import pandas as pd
from pandas import DataFrame
from functools import wraps
from collections import OrderedDict
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


@login_manager.user_loader
def load_user(userid):
	try:
		return models.Users.get(models.Users.id == userid)
	except models.DoesNotExist:
		return None


@app.before_request
def before_request():
	"""
	Connect to the database before each request
	"""
	g.user = current_user
	g.version = 1 #Used for updating cached assets in templates

@app.after_request
def after_request(response):
	"""
	Close the database connection after each request
	"""
	try:
		g.conn.close()
		g.stats.close()
	except:
		pass
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


def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

@app.route('/camera')
def camera():
	return render_template('camera.html')
@app.route("/")
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8200)
