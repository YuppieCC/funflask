from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user

from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm, ResetPasswordForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/resetpassword', methods=['GET', 'POST'])
@login_required
def resetpassword():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            if form.old_password.data == form.new_password.data:
                flash('You password already in use.')
                return redirect(url_for('auth.resetpassword'))
            else:
                current_user.password = form.new_password.data
                db.session.add(current_user)
                db.session.commit()
                flash('You password has been changed.')
                return redirect(url_for('main.index'))
        else:
            flash('Invalid password.')
    return render_template('auth/resetpassword.html', form=form)

@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()


