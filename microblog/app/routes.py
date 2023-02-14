from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, WillowLoginForm

@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/songs')
def songChallenge():
    user = {'username': 'Miguel'}
    posts = [{'title': 'Back in the USSR','artist': 'The Beatles'}, {'title': 'Billy Jean','artist': 'Michael Jackson'}]
    return render_template('songs.html', title = "song list!", user = user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
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
# @app.route('houses', methods=['GET', 'POST'])
# def willow():
#     user = {'username': 'Miguel'}
