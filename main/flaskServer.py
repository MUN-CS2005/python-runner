"""
flask endpoint routing
Libraries used:
    flask,
    subprocess

By Kevin Tanaka(kytanaka - 202049565)
Date: Nov, 2022
"""
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from subprocess import PIPE, STDOUT, run
from database.user import User

app = Flask(__name__)
app.secret_key = "testing"


class regform(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=16)], render_kw={"placeholder": "Username:"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=16)], render_kw={"placeholder": "Password:"})
    confirmation = PasswordField(validators=[InputRequired(), Length(min=4, max=16)], render_kw={"placeholder": "Repeat Password:"})
    submit = SubmitField("Register")

    def isusernamevalid(self, username, password, confirmation):
        pass
        #if username already in database:
        #    raise ValidationError("Username already in use. Please try again.")
        #elif password != confirmation:
        #    raise ValidationError("Passwords do not match! Try again.")


class loginform(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=16)],
                                render_kw={"placeholder": "Username:"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=16)],
                                 render_kw={"placeholder": "Password:"})
    submit = SubmitField("Login")


class changeform(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=16)],
                           render_kw={"placeholder": "Username:"})
    oldpw = PasswordField(validators=[InputRequired(), Length(min=4, max=16)],
                             render_kw={"placeholder": "Old Password:"})
    newpw = PasswordField(validators=[InputRequired(), Length(min=4, max=16)],
                             render_kw={"placeholder": "New Password:"})
    submit = SubmitField("Update")

@app.route("/", methods=['POST', 'GET'])
def home():
    form = loginform()
    if form.validate_on_submit():
        #if password i correct and user is in database
        return redirect(url_for("index", usr=form.username.data))
    return render_template("landingpage.html", form=form)


@app.route("/<usr>", methods=['POST', "GET"])

def index(usr):
    test = render_template("index.html").replace("<!-- OUTPUT PLACEHOLDERNAMEOFTHEACCOUNTUSER -->", usr)
    return test

@app.route("/register", methods=['POST', 'GET'])
def registration():
    form = regform()

    if form.validate_on_submit():
        #User.create(username=form.username.data, password=hash)
        return render_template("landingpage.html", form=form)
    return render_template("register.html", form=form)


@app.route("/changepw", methods=['POST', 'GET'])
def updatepw():
    form = changeform()
    if form.validate_on_submit():
        #return render_template("landingpage.html", form=form)
        pass
    return render_template("changepw.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
