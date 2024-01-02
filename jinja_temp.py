from flask import Flask, render_template

app = Flask('__name__')

#jinja tempating will let us directly insert variables 
# from python code to HTML file. 
@app.route('/')
def index():
    jediname = 'Obi-Wan Kenobi'
    rank = 'Master General'
    letters = list(jediname)
    dic = {'jediname':'Obi-Wan Kenobi', 'rank':'Master General', 'profession':'peace keeper' }
    return render_template('basic.html',  jediname=jediname,letters=letters, dic = dic, rank=rank)

#jediname variable set in reder template is passed to the template 
#best practice is to keep both name in python code and html jinja names same to avoid confusion. 

if __name__ == '__main__':
    app.run(debug=True)

