from flask import render_template, url_for, flash, redirect, request
from flaskblog.forms.login import LoginForm
from flaskblog.messages import login_msgs, status_msgs
from flaskblog import app, bcrypt
from flaskblog.database.repositories.user_repository import UserRepository
from flask_login import login_user, current_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = UserRepository.get_by_email(form.email.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(login_msgs.fail_not_valid_credentials(), status_msgs.fail)
    return render_template('login.html', title='Login', form=form)