from flaskblog import app, db
from flask import url_for, redirect, render_template, flash, request
from flask_login import logout_user, current_user, login_required
from flaskblog.forms.update_account import UpdateAccountForm
from flaskblog.messages import account_msgs, status_msgs

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(account_msgs.success_update_account(), status_msgs.success)

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file = image_file, form = form)
