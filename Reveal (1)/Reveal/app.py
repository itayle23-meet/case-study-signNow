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

@app.route('/home_a', methods=['GET', 'POST'])
def home_a():
    return render_template('index_a.html')

@app.route('/home_h', methods=['GET', 'POST'])
def home_h():
    return render_template('index_h.html')


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

@app.route('/new_story_a', methods=['GET', 'POST'])
def new_story_a():
    if request.method == 'POST':
        story_a = {"email_a" : request.form['email_a'], "text_a" : request.form['text_a'], "name_a" : request.form['name_a']}
        print('story_a',story_a)
        db.child("Stories_a").push(story_a)
        return redirect(url_for('index_a'))
    return redirect(url_for('index_a'))

@app.route('/index_a', methods=['GET', 'POST'])
def index_a():
    stories_a = db.child("Stories_a").get().val()
    print(stories_a)
    return render_template("index_a.html", stories_a = stories_a)

@app.route('/new_story_h', methods=['GET', 'POST'])
def new_story_h():
    if request.method == 'POST':
        story_h= {"email_h" : request.form['email_h'], "text_h" : request.form['text_h'], "name_h" : request.form['name_h']}
        print('story_h',story_h)
        db.child("Stories_h").push(story_h)
        return redirect(url_for('index_h'))
    return redirect(url_for('index_h'))

@app.route('/index_h', methods=['GET', 'POST'])
def index_h():
    stories_h = db.child("Stories_h").get().val()
    print(stories_h)
    return render_template("index_h.html", stories_h= stories_h)


################

if __name__ == '__main__':
    app.run(debug=True)