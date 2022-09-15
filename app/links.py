from flask import render_template, jsonify, request, redirect, session, flash, url_for
from app import app
from app.decorators import login_required

@app.route('/u/<username>')
def links(username):
    links = app.db.GetLinksByUsername(username)
    settings = app.db.GetLinkSettings(username)
    return render_template('links.html', links=links, linksettings=settings)