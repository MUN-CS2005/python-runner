"""
flask endpoint routing
Libraries used:
    flask,
    subprocess

By Kevin Tanaka(kytanaka - 202049565)
Date: Nov, 2022
"""
from flask import Flask, render_template, request, redirect, url_for, session
from subprocess import PIPE, STDOUT, run
from main.database.user import User
from main.LogData import LogData


app = Flask(__name__)
app.secret_key = "testing"

logfile = "log.txt"
logger = LogData.Logdata(logfile)


@app.route("/", methods=['POST', 'GET'])
def home():
    username = session.get('username')
    if username:
        user = User.get(username)
        session['code'] = user.code
        logger.record_log("home()", str(user.username), str(session['code']))
        return render_template("index.html", code=user.code, username=username)
    return redirect(url_for('login'))


@app.route("/change_password", methods=['POST', 'GET'])
def update():
    """
    Routing the "/change_password" page
    If user does not exist in database, or if password do not match,
    it raises an error and displays it
    """
    if request.method == 'POST':
        user = request.form['username']
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        if not User.has_user(user):
            return render_template("change_password.html", error_username_not_found=True)
        current_user = User.get(user)
        if old_password != current_user.password:
            return render_template("change_password.html", error_password_do_not_match=True)
        else:
            User(user, new_password, current_user.code).save()
            return render_template("login.html")
    else:
        return render_template("change_password.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    """
    Routing the "/register" page
    If user does not input anything, or username is unavailable, or passwords do not match,
    it raises an error and displays it
    """
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        check = request.form['confirm']
        if not user or not password:
            return render_template("register.html", error_no_credentials=True)
        elif User.has_user(user):
            return render_template("register.html", error_username_unavailable=True)
        elif password != check:
            return render_template("register.html", error_passwords_do_not_match=True)
        else:
            User.create(user, password)
            return redirect(url_for('home'))
    else:
        return render_template('register.html')


@app.route("/run_code", methods=['POST'])
def runcode():
    """Routing the "/run_code" page"""
    code = request.form['codestuff']
    p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
    output = p.stdout
    logger.record_log("runcode()", session.get('username'))
    return render_template("index.html", code=code, output=output, username=session.get('username'))


@app.route("/login", methods=['POST', 'GET'])
def login():
    """ Auth Handler """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        logger.record_log("login()", str(username))
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
    User._create_table()
    app.run(debug=True)
