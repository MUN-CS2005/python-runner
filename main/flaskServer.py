"""
flask endpoint routing
Libraries used:
    flask,
    subprocess

By Kevin Tanaka(kytanaka - 202049565)
Date: Nov, 2022
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from subprocess import PIPE, STDOUT, run

app = Flask(__name__)
app.secret_key = "testing"

@app.route("/", methods=['POST', 'GET'])
def login():
    """Routing "/" as homepage when loading server"""
    if request.method == "POST":
        print("here")
        user = request.form["username"]
        passw = request.form["password"]
        if len(user) == 0:
            flash("Please input your username", "info")
            return render_template("landingpage.html")
        #elif user not in database:
        #    flash("No such username in our database, please register!", "info")
        #    return render_template("landingpage.html")
        elif len(passw) == 0:
            flash("Wrong password", "info")
            return render_template("landingpage.html")
        else:
            print(f"/index/{user}")
            return redirect(url_for((f"/index/{user}"), usr=user))
    else:
        return render_template("landingpage.html")

@app.route("/<usr>", methods=['POST'])
def client(usr):
    #return f"<h1>{usr}</h1>"
    return render_template("index.html")

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form["username"]
        pw = request.form["password"]
        checkpw = request.form["check"]
        print(username)
        if len(username) == 0:
            flash("Please input your username!", "info")
            return redirect(url_for("register"))
        #elif username already in database:
        #    flash("This username is already claimed!", "info")
        elif len(pw) == 0:
            flash("Please choose a password!", "info")
            return redirect(url_for("register"))
        elif pw != checkpw:
            flash("Passwords did not match! Please try again.", "info")
            return redirect(url_for("register"))
        else:
            #Create user account in database
            return render_template("landingpage.html")
    else:
        return render_template("register.html")

@app.route("/changepw", methods=['POST', 'GET'])
def resetpw():
    return render_template("changepw.html")

@app.route("/index/<usr>", methods=['POST', 'GET'])
def index(usr):
    #if request.method == "POST":
    test = render_template("index.html").replace("<!-- OUTPUT PLACEHOLDERNAMEOFTHEACCOUNTUSER -->", usr)
    return test

@app.route("/run_code", methods=['POST'])
def runcode():
    """Routing the "/run_code" page"""
    code = request.form['codestuff']
    test = render_template("index.html").replace('ENTER CODE HERE', code)
    p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
    output = p.stdout
    return test.replace('<!-- OUTPUT PLACEHOLDER -->', output)


if __name__ == "__main__":
    app.run(debug=True)
