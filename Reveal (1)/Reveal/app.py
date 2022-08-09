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



app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database() 

################## 

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/new_story', methods=['GET', 'POST'])
def new_story():
    if request.method == 'POST':
        story= {"email" : request.form['email'], "text" : request.form['text'], "name" : request.form['name']}
        print('story',story)
        db.child("Stories").push(story)
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    stories = db.child("Stories").get().val()
    print(stories)
    return render_template("index.html", stories = stories)



################

if __name__ == '__main__':
    app.run(debug=True)