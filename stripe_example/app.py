from flask import Flask, render_template, redirect, request, url_for
import stripe

app = Flask(__name__)

public_key = 'pk_test_6pRNASCoBOKtIshFeQd4XMUh'
stripe.api_key ="sk_test_BQokikJOvBiI2HlWgH4olfQ2"

@app.route('/')
def index():
    return render_template('index.html', public_key=public_key)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

# no template, just handles login of connecting to strope for the payment
@app.route('/payment', methods=['POST'])
def payment():
    print('inside 1st')
    #cust info 
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])

    print('inside 2ndst')
    
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=1999,
        currency='usd',
        description='Donations'
    )
    print('Done')
    return redirect(url_for('thank_you'))

if __name__ == '__main__':
    app.run(debug=True)

