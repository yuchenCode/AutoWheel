from flask import render_template, session, redirect, url_for
from . import imgSearch


@imgSearch.route('/imgSearch/login')
def imgSearch():
    return render_template('imgSearch/img_search.html')
#
#
# @auth.route('/auth/register')
# def register():
#
#     return render_template('auth/register.html')
