from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth' , __name__)


@auth.route('/signin')
def signin():
    if request.method == 'POST' :
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password = request.form.get('password')

        if len(email) < 4 :
            flash('Email must be greater than 3 characters',category='error')
        if len(firstname) < 2 :
            flash('Firstname must be greater than 1 characters',category='error')
        if len(password) < 7 :
            flash('Password must be atleast than 7 characters',category='error')
        else:
            flash('Account created',category='success')
        
    return render_template('signin.html')

