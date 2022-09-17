from flask import render_template, jsonify, request, redirect, session, flash, url_for
from app import app
from app.decorators import login_required

@app.route('/u/<username>')
def links(username):
    links = app.db.GetLinksByUsername(username)
    settings = app.db.GetLinkSettings(username)
    owner = app.db.GetUserByUsername(username)
    return render_template('links.html', links=links, linksettings=settings, owner=owner)

@app.route('/editlinks', methods=['GET', 'POST'])
@login_required
def editlinks():
    username = session['username']
    if 'default' in request.form:
        app.db.ResetDefaultLinkSettings(username)
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
        buttonbackgroundhovercolor = request.form['buttonbackgroundhovercolor']
        namecolor = request.form['namecolor']
        if 'backgroundimage' in request.form:
            backgroundimage = request.form['backgroundimage']
        app.db.UpdateLinkSettings(username, backgroundcolor1, backgroundcolor2, bgradius, buttonbackgroundcolor, buttontextcolor, buttonbordercolor, buttonradius, buttonwidth, buttonbackgroundhovercolor, namecolor, backgroundimage)
        linksettings = app.db.GetLinkSettings(username)
    return render_template('editlinks.html', linksettings=linksettings)