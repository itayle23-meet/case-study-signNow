rom flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {



}
pp = Flask(__name__, template_folder='', static_folder='')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database() 

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.htmal')