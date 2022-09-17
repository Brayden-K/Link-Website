from flask import render_template, jsonify, request, redirect, session, flash, url_for
from app import app
from app.decorators import login_required

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	username = session['username']
	linksettings = app.db.GetLinkSettings(username)
	if not linksettings:
		linksettings = app.db.SetDefaultLinkSettings(username)
	if request.method == "POST":
		if 'highlight' in request.form:
			highlight = True
		else:
			highlight = False
		app.db.UpdateAccount(username, highlight)
	return render_template('account.html', linksettings=linksettings)