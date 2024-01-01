from flask import Flask

app = Flask(__name__)
#create an instance of the class Flask and sending __name__ sending name of the module, essentially checking if we're running the script DIRECTLY.

# decorator directly links that page to what ever route you're on, ie the url of that page.  
@app.route('/') #127.0.0.1:5000
def index():
    return '<h1>Hello there!</h1>'

#the url extensions parameter that are passed into the decorator are called views. 
#the functions under decorators are called view functions.  

@app.route('/info') #127.0.0.1:5000/info
def info():
    return '<h2>General Kenobi!! You are a bold one</h2>'

#dynamic routing 
@app.route('/Jedi/<name>')
def pages(name):
    return '<h1>Master Jedi {}</h1>'.format(name)

#if you're running the script then run your application app.run()
if __name__ == '__main__':
    app.run()

