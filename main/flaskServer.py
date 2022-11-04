"""
flask endpoint routing
Libraries used:
    flask,
    subprocess

By Kevin Tanaka(kytanaka - 202049565)
Date: Nov, 2022
"""
from flask import Flask, render_template, request
from subprocess import PIPE, STDOUT, run

app = Flask(__name__)


@app.route("/")
def startpage():
    """Routing "/" as homepage when loading server"""
    return render_template("index.html")


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
