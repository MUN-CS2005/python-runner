"""
flask endpoint routing
Libraries used:
    flask,
    subprocess

By Kevin Tanaka(kytanaka - 202049565)
Date: Nov, 2022
"""
from subprocess import PIPE, STDOUT, run
from flask import Flask, render_template, request, redirect, url_for, session
from main.database.user import User
from main.LogData import LogData

app = Flask(__name__)
app.secret_key = "testing"

LOGFILE = "log.txt"
logger = LogData.Logdata(LOGFILE)


@app.route("/", methods=['POST', 'GET'])
def home():
    """
    Routing for main page
    """
    username = session.get('username')
    if username and User.has_user(username):
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
        User(user, new_password, current_user.code).save()
        return render_template("login.html")
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
        if User.has_user(user):
            return render_template("register.html", error_username_unavailable=True)
        if password != check:
            return render_template("register.html", error_passwords_do_not_match=True)
        User.create(user, password)
        return redirect(url_for('home'))
    return render_template('register.html')


@app.route("/run_code", methods=['POST'])
def run_code():
    """Routing the "/run_code" page"""
    code = request.form['codestuff']
    python_result = run("python", stdout=PIPE, shell=True, stderr=STDOUT,
                        input=code, encoding='ascii', check=False)
    output = python_result.stdout
    try:
        logger.record_log("runcode()", session.get('username'))
    except TypeError:
        return render_template("index.html", code=code, output=output,
                               username=session.get('username'))
    return render_template("index.html", code=code, output=output, username=session.get('username'))


@app.route("/save_code", methods=['POST'])
def save_code():
    """
        saves the code when the save button is pushed
        output is not preserved
        if username is not found does not save code
    """
    username = session.get('username')
    code = request.form['codestuff']
    if username:
        user = User.get(username)
        user.code = code
        user.save()
    else:
        print("unable to find user")
    return render_template("index.html", code=code, username=session.get('username'))


@app.route("/load_code", methods=['POST'])
def load_code():
    """
        loads the code from the database and puts it into
        codestuff when the load button is pushed
        output is not preserved
        if username is not found keeps current code

    """
    username = session.get('username')
    if username:
        user = User.get(username)
        code = user.code
    else:
        print("unable to find User")
        code = request.form['codestuff']
    return render_template("index.html", code=code, username=session.get('username'))


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
        return render_template("login.html", error=True)
    return render_template('login.html')


@app.route("/logout", methods=['POST'])
def logout():
    """Route for logging out a user"""
    session.clear()
    return redirect(url_for('login'))


if __name__ == "__main__":
    User.create_table()
    app.run(debug=True)
