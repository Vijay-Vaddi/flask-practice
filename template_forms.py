from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./puppies/puppies_home.html')


@app.route('/puppies_signup')
def puppies_signup():
    return render_template('./puppies/puppies_signup.html')


@app.route('/puppies_thankyou')
def puppies_thankyou():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('./puppies/puppies_thankyou.html' , first=first, last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('./puppies/puppies_404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

