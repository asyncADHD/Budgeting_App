from flask import Flask, render_template, request, redirect, url_for
from App_Functions.DB_Functions import DB_Functions

app = Flask(__name__)
app.config['DEBUG'] = True
loggen_in = False 
# Create a dictionary to store the registered users and their passwords
users = {'user1': 'password1', 'user2': 'password2'}
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
 

        # Check if the user name and password are correct
        if button == 'signup':
            return redirect(url_for('signup'))
        elif username in users and users[username] == password:
            # If the login is successful, redirect to the home page
            return redirect(url_for('landing'))
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
    return render_template('landing.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        button = request.form['button']
        username = request.form['username']
        password = request.form['password']
        confimed_password = request.form['confimed_password']

        if password == confimed_password:
            DB_Functions.add_hash_pass_to_db(username, password)
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=1)
    

    