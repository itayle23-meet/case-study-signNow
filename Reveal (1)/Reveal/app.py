from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
"apiKey": "AIzaSyDr67EonBHtLJzJIbjz22BA9735oa49tFI",
"authDomain": "signnow-9d696.firebaseapp.com",
"projectId": "signnow-9d696",
"storageBucket": "signnow-9d696.appspot.com",
"messagingSenderId": "816100294913",
"appId": "1:816100294913:web:bd12d0a1a6e3d24757db00",
"measurementId": "G-LBZHTSE7CY",
"databaseURL": "https://signnow-9d696-default-rtdb.europe-west1.firebasedatabase.app/"
}



app = Flask(__name__, template_folder='', static_folder='')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database() 

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)