from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from app import db
from .forms import LoginForm, UserForm
from .models import User
from . import users

@users.route('/')
@login_required
def get_users_list():
    users = User.query.filter_by().all()
    return render_template('users.html', context=users)

@users.route('/<int:id>/')
@login_required
def get_user(*args, **kwargs):
    user = User.query.filter_by(id=kwargs['id']).first()
    print(user)
    return render_template('user_details.html', user=user)


@users.route('/delete/<int:id>/')
@login_required
def delete_user(*args, **kwargs):
    user = User.query.filter_by(id=kwargs['id']).first()
    db.session.delete(user)
    db.session.commit()

    flash('You have successfully removed user.')
    return redirect(url_for('users.get_users_list'))


@users.route('/create', methods=['GET', 'POST'])
@login_required
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('You have successfully added new user.')

        return redirect(url_for('users.get_users_list'))

    return render_template('create.html', form=form, title='Add')

@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):

            login_user(user)

            return redirect(url_for('users.get_users_list'))

        else:
            flash('Invalid email or password.')

    return render_template('login.html', form=form, title='Login')

@users.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('users.login'))

