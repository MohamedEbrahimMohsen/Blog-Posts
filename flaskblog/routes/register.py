from flask import render_template, url_for, flash, redirect
from flaskblog.models.user import User
from flaskblog.models.post import Post
from flaskblog.forms.register import RegisterationForm
from flaskblog.messages import register_msgs, status_msgs
from flaskblog import app, bcrypt
from flaskblog.database.repositories.UserRepository import UserRepository
from flask_login import current_user

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: 
        return redirect(url_for('home'))

    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        UserRepository.create(user)
        flash(register_msgs.success_account_created(), status_msgs.success)
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

def addNewUser(user):
    pass
    