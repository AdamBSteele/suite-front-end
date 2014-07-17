
# -*- coding: utf-8 -*-

import os

from flask import Blueprint, render_template, send_from_directory, abort, redirect, url_for, request, flash
from flask import current_app as app
from flask.ext.babel import gettext as _

from flask.ext.login import login_required, current_user
from .forms import CreateEchoForm
from .models import Echo
import json

echo = Blueprint('echo', __name__, url_prefix='/echo')


@echo.route('/add_echo', methods=['POST'])
@login_required
def add_echo():
	user = current_user
	form = CreateEchoForm()
	if form.validate_on_submit():
		form.add_echo(user)
		flash(_("Your echo has been added"),'success')
	msg = Echo()
	return redirect(url_for('user.index'))

@echo.route('/<int:id>', methods=['GET'])
def get(id):
	msg = Echo()
	msg = msg.get_by_id(id)
	form = ResponseEchoForm(offset = 0)
	return re

@echo.route('/responses/<int:id>', methods=['GET'])
def get_responses(id):
	msg = Echo()
	echos =  msg.get_responses(id)
	echos = [{'id':x.echo_id,'text':x.text,'response':x.response} for x in echos]
	return json.dumps(echos)

