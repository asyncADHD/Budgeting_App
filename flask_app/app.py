from flask import Flask, render_template, request, redirect, url_for
from App_Functions.DB_Functions import DB_Functions

app = Flask(__name__)
app.config['DEBUG'] = True
loggen_in = False 
DB_Functions.create_db_if_none()

# Define the route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the request is a POST request (i.e. the user has submitted the form)
    if request.method == 'POST':
        button = request.form['button']
        # Get the user name and password from the form
        username = request.form['username']
        password = request.form['password']
        result = DB_Functions.find_user_in_table(username)
        if button =='login':
            password_match = DB_Functions.check_if_pass_eq_hash(username, password)
            if password_match == True:
                return redirect(url_for('landing'))
 

        # Check if the user name and password are correct
        if button == 'signup':
            return redirect(url_for('signup'))
        else:
            # If the login is unsuccessful, show an error message
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    # If the request is a GET request (i.e. the user is visiting the login page for the first time)
    else:
        return render_template('login.html')

# Define the route for the home page
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/home')
def landing():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        button = request.form['button']
        username = request.form['username']
        password = request.form['password']
        confimed_password = request.form['confimed_password']
        admin_code = request.form['admincode']
        adm_hashed_pass = b"|\xbc\x11'\x17z(\x00\xce \xad\xb9?\xef\x08\xd4<l\xec?\x96\x08\xc7\xd8u\x80\xbb\x179\xd3\xa7\xb6"
        check_adm_code = DB_Functions.adm_hash(admin_code)
        if button == 'signup':
            if adm_hashed_pass == check_adm_code:
                if password == confimed_password:
                    DB_Functions.add_hash_pass_to_db(username, password)
            else:
                error = "Invalid Admin Code'"
                return render_template('signup.html', error=error)
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(port=8000,debug=True)
    
