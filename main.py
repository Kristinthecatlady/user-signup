from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    '''Home'''
    return render_template('table.html', title="User Sign-in App")

def is_valid_un_pw(password):
    '''Validate str; return True if between 3 and 20 char'''

    if len(password) >= 3 and len(password) <= 20:
        if not re.search(r'\s', password):
            return True
    else:
        return False

@app.route('/', methods=['POST'])
def validate_user():
    '''Validate UN, PW and doublecheck, Email'''

    name = request.form['name']
    password = request.form['password']
    pw_check = request.form['pw_check']
    email = request.form['email']

    email_error = ''
    pw_error = ''
    pw_error_check = ''
    un_error = ''
    
    if not is_valid_un_pw(name):
        un_error = 'Not a valid username. Please review username requirements'
        
    if not is_valid_un_pw(password):
        pw_error = 'Not a valid password. Please review password requirements'
        pw = ''
    else:
        if pw_check != password:
            pw_error_check = 'Passwords do not match, please try again.'
            password = ''
            pw_check = ''

    if email:
        if not re.match("([^@|\s]+@[^@]+\.[^@|\s]+)", email):
            email_error = 'Not a valid email'

    if not un_error and not pw_error_check and not pw_error and not email_error:
        return render_template('success.html', title="Welcome User", name=name)
    else:
        return render_template('table.html', pw_error=pw_error,
                               un_error=un_error,
                               pw_error_check=pw_error_check,
                               email_error=email_error, name=name, email=email,
                               title='Sign-In Page')



app.run()