from flask import Blueprint

auth =Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "Login"

@auth.route('/sign-up')
def login():
    return "Login"

@auth.route('/logout')
def logout():
    return "Logout"