from flask import render_template, jsonify, request, redirect, session, flash, url_for
from app import app
from app.decorators import login_required
from app.errors import page_not_found

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/u/<username>')
def links(username):
    return render_template('links.html', user=username)