"""
flask endpoint routing
Libraries used:
    flask,
    subprocess

By Kevin Tanaka(kytanaka - 202049565)
Date: Nov, 2022
"""
from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from subprocess import PIPE, STDOUT, run
from database.user import User

app = Flask(__name__)
app.secret_key = "testing"


@app.route("/", methods=['POST', 'GET'])
def home():
    username = session.get('username')
    print(username)
    if username:
        user = User.get(username)
        session['code'] = user.code
        return render_template("index.html", code=user.code, username=username)
    return redirect(url_for('login'))

# @app.route("/register", methods=['POST', 'GET'])
# def registration():
#     form = regform()
#
#     if form.validate_on_submit():
#         #User.create(username=form.username.data, password=hash)
#         return render_template("login.html", form=form)
#     return render_template("register.html", form=form)


# @app.route("/changepw", methods=['POST', 'GET'])
# def updatepw():
#     form = changeform()
#     if form.validate_on_submit():
#         #return render_template("login.html", form=form)
#         pass
#     return render_template("changepw.html", form=form)


@app.route("/run_code", methods=['POST'])
def runcode():
    """Routing the "/run_code" page"""
    code = request.form['codestuff']
    p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
    output = p.stdout
    return render_template("index.html", code=code, output=output, username = session.get('username'))


@app.route("/login", methods=['POST', 'GET'])
def login():
    """ Auth Handler """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        if not username or not password:
            return render_template("login.html", error=True)
        if User.has_user(username):
            user = User.get(username)
            if user.password != password:
                return render_template("login.html", error=True)
            session['username'] = user.username
            return redirect(url_for('home'))
        else:
            return render_template("login.html", error=True)
    else:
        return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
