from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('basic.html')
#render basic template from templates and data from static folder. 

if __name__ == '__main__':
    app.run(debug=True)

