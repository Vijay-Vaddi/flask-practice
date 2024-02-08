from user import User
from flask_jwt_extended import create_access_token
from flask import jsonify

users = [User(1, 'Vijay', 'mypassword'),
         User(2,'Pradeep', 'secret')]


# create mapping in order to access users based off id/username
# dictionary comprehension
username_table = {u.username: u for u in users} #{'vijay': User obj of vijay}
userid_table = {u.id: u for u in users} 

# authenticate to check username/pass and return user

def login(username,password):
    
    user = username_table.get(username, None) #.get returns none for no key error unlike username_table[username] 
    if user and password == user.password:
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token)
    else: 
        return jsonify({'msg':'wrong password bro'}), 401

