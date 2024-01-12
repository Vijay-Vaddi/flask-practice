from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/jedi/<name>')
def jedi_name(name):
    return render_template('jedi.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)





# to keep one code/file for common things across pages like nav bars, template inheritance can be used as a solution. 
# to do this, we set up a base.html for reusable aspects of our site 
# then use {% extend 'base.html'%} and {% block %} statements to extend  