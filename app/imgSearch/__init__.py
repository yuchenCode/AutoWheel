from flask import Blueprint

imgSearch = Blueprint('imgSearch', __name__)

from . import views