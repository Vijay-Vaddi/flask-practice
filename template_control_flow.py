from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
    dic = {'jediname':'Obi-Wan Kenobi', 'rank':'Master General', 'profession':'peace keeper' }
    return render_template('control_flow.html', dic = dic)

#{{}} is used for jinja while {% %} is used to run python control flow inside html. 
#can be used to display list items one by one to a li elements in html etc.
#have to end the loops and statements using {% endfor %} in html


if __name__ == "__main__":
    app.run(debug=True)

