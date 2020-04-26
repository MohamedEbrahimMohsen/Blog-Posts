from flaskblog import app
from flask import url_for, redirect, render_template
from flask_login import logout_user, current_user, login_required

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
