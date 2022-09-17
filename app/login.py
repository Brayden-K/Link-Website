from flask import render_template, jsonify, request, redirect, session, flash, url_for
from app import app
import requests, datetime

@app.route('/login')
def login():
	# Check if logged in
	if not session:
		# Get code from twitch
		if not 'code' in request.args:
			scopes = 'user:read:email+user:read:follows+user:read:subscriptions'
			return redirect(f"https://id.twitch.tv/oauth2/authorize?response_type=code&client_id={app.config['TWITCHCLIENTID']}&redirect_uri={app.config['TWITCHREDIRECTURI']}&scope={scopes}&state=c3ab8aa609ea11e793ae92361f002671")
		elif 'error' in request.args:
			return redirect(url_for('index'))
		elif 'code' in request.args:
			# Handle code
			code = request.args.get('code')
			payload = {
				'client_id': app.config['TWITCHCLIENTID'],
				'client_secret': app.config['TWITCHSECRET'],
				'code': code,
				'grant_type': 'authorization_code',
				'redirect_uri': app.config['TWITCHREDIRECTURI']
			}
			r = requests.post('https://id.twitch.tv/oauth2/token', data=payload)
			# Get user info
			if 'access_token' in r.json():
				access_token = r.json()['access_token']
				headers = {
					'Authorization': f'Bearer {access_token}',
					'Client-Id': app.config['TWITCHCLIENTID']
				}
				user = requests.get('https://api.twitch.tv/helix/users', headers=headers).json()['data'][0]
				try:
					username = user['display_name']
				except:
					return user
				if app.db.CheckRegistered(username): 
					# Login
					session['loggedin'] = True
					session['username'] = username
					return redirect(url_for('dashboard'))
				else:
					# Register
					created_at = datetime.date.today()
					email = user['email']
					twitchid = user['id']
					profile_image_url = user['profile_image_url']
					broadcaster_type = user['broadcaster_type']
					twitch_created_at = user['created_at'].split('T')[0]
					app.db.Register(username, email, twitchid, profile_image_url, broadcaster_type, twitch_created_at, created_at)
					session['loggedin'] = True
					session['username'] = username
					return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    """
    Logout page
    Clears session
    Returns to home
    """
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('index', user=None))