# -*- coding: utf-8 -*-
from flask import Flask, url_for, render_template, request, redirect, session
import dbHelper
UPLOAD_FOLDER = 'static/img/upload_img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(import_name=__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route("/", methods=['GET', 'POST'])
def home():
    err = ''
    success = ''
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if session.get('logged_in'):
        return redirect(url_for('admin'))
    if request.method == 'GET':
        return render_template('login.html')
    else:
        condition = False
        name = request.form['username']
        passw = request.form['password']

        try:
            user = dbHelper.User(name, passw, True)
            if user.check_user():
                session['logged_in'] = True
                if 'rememberMe' in request.form:
                    session.permanent = True
                else:
                    session.permanent = False
                return redirect(url_for('admin'))
            else:
                condition = True
                err = "Oops, the credentials don't match"
                return render_template('login.html', err=err, condition=condition)
        except:
            err = 'Something strange happened while trying to log in'
            return render_template('404.html', err=err, condition=condition)

@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', err=e), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html', err=e), 403

@app.errorhandler(410)
def page_gone(e):
    return render_template('410.html', err=e), 410

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html', err=e), 500

if __name__ == "__main__":
    app.secret_key = "HopKIdf78/*9*PO72xQ89Fg??"
    app.run(debug=True)