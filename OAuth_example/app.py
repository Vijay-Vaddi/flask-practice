import os


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
###########################

from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello123'

bluprint = make_google_blueprint(client_id='------------.apps.googleusercontent.com',
                                 client_secret='---------------', 
                                 offline=True, scope=[
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ])

# scope is what we need from the google
#client id and secret keys are typically set as environment variable at the command line. 

app.register_blueprint(bluprint, url_prefix= '/login')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    # returns internal server error if not logged in. 
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text 
    email = resp.json()['email']

    return render_template('welcome.html', email=email)

@app.route('/login/google')
def login():
    if google.authorized:
        return render_template(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html', email=email)

if __name__ == "__main__":
    app.run(debug=True)

