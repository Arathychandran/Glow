from flask import Flask,render_template,redirect,url_for,request
# from flask_mysqldb import MySQL

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'users'

# mysql = MySQL(app)

app=Flask(__name__)
@app.route('/')

def index():

    return render_template('index.html')
@app.route('/new_page', methods=['POST'])
def new_page():
    # Handle form submission and redirect to new page
    return render_template('signin.html')
def getstarted():
    if request .method== 'POST':
       return redirect(url_for('/signin'))

@app.route('/process_signup', methods=['POST'])
def process_signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Perform any processing with the received data (e.g., store in database)
        
        # Redirect to a success page along with the form data
        return redirect(url_for('signup_success', name=name, email=email))

@app.route('/signup_success')
def signup_success():
    name = request.args.get('name')
    email = request.args.get('email')
    password =request.args.get('password',None)
    
    
    return render_template('signup_success.html', name=name, email=email, password=password)
if __name__=='__main__':
    app.run(debug=True)