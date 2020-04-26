from flask import render_template, url_for, flash, redirect
# from models import User, Post
from flaskblog import app

@app.route('/about')
def about():
    return render_template('about.html', title='About')
