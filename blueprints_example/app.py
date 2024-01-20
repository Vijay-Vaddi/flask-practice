# same level as project folder, not inside. 

from adoption_site_project import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    
