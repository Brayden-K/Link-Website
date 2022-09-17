from flask import Flask

app = Flask(__name__)

from app import config
from app import routes
from app import login
from app import account
from app import links
from app import dashboard