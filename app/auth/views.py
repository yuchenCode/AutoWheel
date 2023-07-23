from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import auth
# from .forms import NameForm
from .. import db
from ..models import User


@auth.route('/login', methods=['POST', 'GET'])
def login():  # put application's code here
    return render_template('auth/login.html')
