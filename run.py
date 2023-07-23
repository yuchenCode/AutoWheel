from flask import request

from app import create_app, db
from flask_migrate import Migrate

"""
Entrance of this web project
"""

app = create_app('development')

# app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
# babel = Babel(app)
# @babel.localeselector
# def get_locale():
#     return request.accept_languages.best_match(['zh', 'en'])


# -------- Remote Server Deployment Configuration -------- #
HOST = '127.0.0.1'
PORT = 7080
# -------------------------------------------------------- #

if __name__ == '__main__':
    # app.run(host=HOST, port=PORT, debug=True, ssl_context='adhoc')
    app.run(host=HOST, port=PORT, debug=True)

