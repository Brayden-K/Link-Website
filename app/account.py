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

	if 'backgroundcolor1' in request.form:
		backgroundcolor1 = request.form['backgroundcolor1']
		backgroundcolor2 = request.form['backgroundcolor2']
		bgradius = request.form['bgradius']
		buttonbackgroundcolor = request.form['buttonbackgroundcolor']
		buttontextcolor = request.form['buttonbacktextcolor']
		buttonbordercolor = request.form['buttonbordercolor']
		buttonradius = request.form['buttonradius']
		buttonwidth = request.form['buttonwidth']
		app.db.UpdateLinkSettings(username, backgroundcolor1, backgroundcolor2, bgradius, buttonbackgroundcolor, buttontextcolor, buttonbordercolor, buttonradius, buttonwidth)
		linksettings = app.db.GetLinkSettings(username)
	return render_template('account.html', linksettings=linksettings)