#!/usr/bin/env python3

'''
FLASK APP
'''
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    '''Index route'''
    return jsonify({
        "message": "Bienvenue"
    })


@app.route('/users', methods=['POST'])
def users():
    '''ROUTE TO REGISTER NEW USER'''
    data = request.form
    email = data.get('email')
    password = data.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    '''Run the app'''
    app.run(host="0.0.0.0", port="5000")
