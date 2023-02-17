from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, WillowLoginForm, RegistrationForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/songs')
def songChallenge():
    user = {'username': 'Miguel'}
    posts = [{'title': 'Back in the USSR','artist': 'The Beatles'}, {'title': 'Billy Jean','artist': 'Michael Jackson'}]
    return render_template('songs.html', title = "song list!", user = user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/willowlogin', methods=['GET', 'POST'])
def willowlogin():
    form = WillowLoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('willow'))
    return render_template('houselogin.html', title='Willow Sign In', form=form)

@app.route('/willow')
def willow():
    user = {'username': 'Miguel'}
    houses = [{'address': '2 River Terrace','sqft': '3490'}, {'address': '23 Greenwood Plaza','sqft': '2300'}]
    return render_template('houses.html', title = "willow homepage", user = user, houses = houses)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# @app.route('houses', methods=['GET', 'POST'])
# def willow():
#     user = {'username': 'Miguel'}
