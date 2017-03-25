# coding=utf-8
from flask import render_template, abort
from . import main
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404)
    return render_template('user.html', user=user)
