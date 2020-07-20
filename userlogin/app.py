from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import pymongo
import bcrypt

# app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'appdata'
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
app = Flask(__name__)
import db
#test to insert data to the data base
@app.route("/")
def index():
    if 'username' in session:
        return render_template('index.html')

    return render_template('indexx.html')

@app.route('/login', methods =['POST'])
def login():
    users = db.db.users
    login_user = users.find_one({'name':request.form['username']})
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    
    return 'Invalid username/password combination'
@app.route('/register', methods= ['POST','GET'])
def register():
    if request.method == 'POST':
        users = db.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'],'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'
    return render_template('register.html')
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug= True,port=8000)
