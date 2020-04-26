from flask import render_template, url_for, flash, redirect
# from models import User, Post
from flaskblog.seed_data import blog_data
from flaskblog import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=blog_data.posts)