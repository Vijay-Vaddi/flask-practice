import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
###########################

from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello123'

bluprint = make_google_blueprint(client_id='', client_secret='', 
                                 offline=True, scope=['profile', 'email'])
# scope is what we need from the google

app.register_blueprint(bluprint, url_prefix= '/login')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():

    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text 
    email = resp.json()['email']

    return render_template('welcome.html', email=email)

@app.route('/login/google')
def login():
    if google.authorized:
        return render_template(url_for('google.login'))
    resp = google.get('/plus/v1/people/me')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html', email=email)

