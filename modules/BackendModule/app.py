from flask import Flask
from flask import request

app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route(‘/users/<user_id>’, methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
	    """return the information of user"""
        userId = request.args.get('user_id')
    if request.method == 'POST':
	    """modify/update the information for <user_id>"""
        data = request.form # a multidict containing POST data
    if request.method == 'DELETE':
	    """delete user with ID <user_id>"""
        userId = request.args.get('user_id')
    else:
        # Error 405 Method Not Allowed