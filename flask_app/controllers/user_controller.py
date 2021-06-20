from flask_app import app

from ..models.user import User

from flask import render_template, redirect, request

@app.route('/')
def home():
    return redirect('/friendships')

@app.route('/friendships')
def friendships_display():
    all_friends=User.get_all_friendships()
    all_users=User.get_all()
    return render_template('index.html', all_friends=all_friends, all_users=all_users)

@app.route('/friendships/create', methods=['POST'])
def create_friendship():
    data={
        'user_id':request.form['user_id'],
        'friend_id':request.form['friend_id']
    }
    User.create_friendship(data)
    return redirect('/friendships')

@app.route('/friendships/newuser', methods=['POST'])
def create_user():
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name']
    }
    User.create_user(data)
    return redirect('/friendships')