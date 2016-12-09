#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import app, db, Admin
from flask import render_template


@app.route('/hello', methods=['GET'])
def getMainPage():
	allAdmins = Admin.query.all()
	for item in allAdmins:
		print item.id, item.name, item.password
	return render_template('admin/admin-template.html', data=allAdmins)