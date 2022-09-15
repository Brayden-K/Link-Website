from flask import session
from app import app
import os

app.debug = True
app.config['ENVIRONMENT'] = os.getenv('ENVIRONMENT')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MYSQLHOST'] = os.getenv('MYSQLHOST')
app.config['MYSQLUSER'] = os.getenv('MYSQLUSER')
app.config['MYSQLPASS'] = os.getenv('MYSQLPASS')
app.config['MYSQLDB'] = os.getenv('MYSQLDB')
app.config['TWITCHCLIENTID'] = os.getenv('TWITCHCLIENTID')
app.config['TWITCHSECRET'] = os.getenv('TWITCHSECRET')
app.config['TWITCHREDIRECTURI'] = os.getenv('TWITCHREDIRECTURI')



from app.database import MySQL

# Initialize Our DB
app.db = MySQL(app.config['MYSQLHOST'], app.config['MYSQLUSER'], app.config['MYSQLPASS'], app.config['MYSQLDB'])

@app.context_processor
def inject_settings() -> dict:
    """
    Sets our global settings
    settings: Global settings from DB
    """
    settingsquery = app.db.query('SELECT * from settings', querytype='select', fetchall=False)
    if session:
        user = app.db.GetUserByUsername(session['username'])
        settings = {
            'settings': settingsquery,
            'user': user
        }
    else:
        settings = {
            'settings': settingsquery,
            'user': None
        }
    return settings