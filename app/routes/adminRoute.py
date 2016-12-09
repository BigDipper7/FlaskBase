#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import app, db, Admin
from flask import render_template


@app.route('/hello', methods=['GET'])
def getMainPage():
	return render_template('admin/admin-template.html', data=None)