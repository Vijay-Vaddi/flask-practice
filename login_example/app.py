from myproject import app, db
from flask import render_template, redirect, url_for, flash, abort, request
from flask_login import login_user, login_required, logout_user
from myproject.forms import RegisterForm, LoginForm
from myproject.models import User

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/welcome')
@login_required
def welcome():
    
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():

    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        try:
            if user:
                if user.check_password(form.password.data): #and user is not None:
                    login_user(user)
                    flash("Logged in succcessfully")

                    next = request.args.get('next')

                    if next is None or not next[0]=='/': #if not on this domain??
                        next = url_for('welcome')

                    return redirect(next)
        except:
            flash('User not found. Please register')
            return redirect(url_for('register'))
    return render_template('/login.html', form=form)


@app.route('/register', methods=['GET','POST'])
def register():

    form = RegisterForm() 

    if form.validate_on_submit():
        
        user = User(email=form.email.data, 
                    user_name=form.user_name.data,
                    password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registering!")
        return redirect(url_for('login'))
    return render_template('/register.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)

