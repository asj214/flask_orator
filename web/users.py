from datetime import datetime
from flask import Blueprint, session, request, redirect, render_template, url_for
from forms import UserForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

from models import User

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/login', methods=['GET', 'POST'])
def login():

    if 'auth' in session:
        return redirect(url_for('index'))

    form = LoginForm()
    redirect_url = request.args.get('redirect_url', url_for('index'))

    if form.validate_on_submit():

        user = User.where('email', form.email.data).first()
        redirect_url = form.redirect_url.data

        if user is not None and check_password_hash(user.password, form.password.data):

            user.update(last_login_at=datetime.now()) 

            session['auth'] = {
                'id': user.id,
                'email': user.email,
                'name': user.name
            }

            return redirect(redirect_url)

    return render_template('users/login.html', form=form, redirect_url=redirect_url)

@user_controller.route('/logout', methods=['GET'])
def logout():
    if 'auth' in session:
        session.pop('auth', None)
    return redirect(url_for('user_controller.login'))

@user_controller.route('/create', methods=['GET', 'POST'])
def create():
    form = UserForm()
    if form.validate_on_submit():

        user = User()
        user.email=form.email.data,
        user.name=form.name.data,
        user.password=generate_password_hash(form.password.data)
        user.save()

        return redirect(url_for('user_controller.login'))
    return render_template('users/form.html', form=form)