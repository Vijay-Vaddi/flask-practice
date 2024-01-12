from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route('/')
def valid_username_index():
    return render_template('/valid_username/valid_username_index.html')

@app.route('/valid_username_result')    
def valid_username_result():
    name = request.args.get('name')
    lower = bool(re.search(r'[a-z]', name))
    upper = bool(re.search(r'[A-Z]', name))
    digit = bool(re.search(r'[0-9]$',name))

    return render_template('/valid_username/valid_username_result.html', lower=lower, upper=upper, digit=digit, name=name)

if __name__ == '__main__':
    app.run(debug=True)

