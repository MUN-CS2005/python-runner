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

class flaskServer:
    """
        This is a flask framework server.
        There is more things that may be implemented into the server. For example, maybe more endpoints may be added.
        When the code is executed it creates a server with 2 pages for now.
        "/": landing page
        "/run_code": page displaying output of python input.

        Attributes:
            No attributes
        """

    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route("/")
        def startPage():
            """Routing "/" as homepage when loading server"""
            return render_template("index.html")


        @self.app.route("/run_code", methods=['POST'])
        def runCode():
            """Routing the "/run_code" page"""
            code = request.form['codestuff']
            test = render_template("index.html").replace('ENTER CODE HERE', code)
            p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
            output = p.stdout
            return test.replace('<!-- OUTPUT PLACEHOLDER -->', output)

    def start(self):
        """Function to start the server"""
        self.app.run(debug=True)

if __name__ == "__main__":
    serverInst = flaskServer()
    serverInst.start()


