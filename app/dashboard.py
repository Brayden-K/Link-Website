from flask import render_template, jsonify, request, redirect, session, flash, url_for
from app import app
from app.decorators import login_required

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
	if request.method == 'POST':
		if 'update' in request.form:
			# return request.form
			id = request.form['id']
			label = request.form['label']
			link = request.form['link']
			icon = request.form['icon']
			if 'nsfw' in request.form:
				nsfw = True
			else:
				nsfw = False
			if 'publish' in request.form:
				publish = True
			else:
				publish = False
			if 'highlight' in request.form:
				if request.form['highlight'] == 'None':
					highlight = None
					highlightname = None
				else:
					highlight = request.form['highlight'].split(':')[0]
					highlightname = request.form['highlight'].split(':')[1]
			else:
				highlightname = None
			if 'effect' in request.form:
				if request.form['effect'] == 'None':
					effect = None
					effectname = None
				else:
					effect = request.form['effect'].split(':')[0]
					effectname = request.form['effect'].split(':')[1]
			else:
				effect = None
				effectname = None
			app.db.UpdateLink(id, label, link, icon, nsfw, publish, highlight, effect, highlightname, effectname)
		if 'delete' in request.form:
			id = request.form['id']
			app.db.DeleteLink(id)
		if 'create' in request.form:
			owner = session['username']
			link = request.form['link']
			icon = request.form['icon']
			label = request.form['label']
			if 'nsfw' in request.form:
				nsfw = True
			else:
				nsfw = False
			if 'publish' in request.form:
				publish = True
			else:
				publish = False
			app.db.CreateLink(owner, link, icon, nsfw, publish, label)
	highlightoptions = app.db.GetOptions('highlight')
	effectoptions = app.db.GetOptions('effect')
	links = app.db.GetAllLinksByUsername(session['username'])
	return render_template('dashboard.html', links=links, highlightoptions=highlightoptions, effectoptions=effectoptions)