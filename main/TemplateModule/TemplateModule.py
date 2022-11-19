"""
A solution for HTML templating.
Library used:
    Flask

Author: Ruixiao Lu
Date: Otc. 2022
"""
from flask import render_template


class Template:
    """
    This is the template module class.
    For more intuitive information, check TemplateModule.html and the unit test.
    This module may be modified depends on project needs.

    Attributes:
        _placeholder: A {key: Value} dic indicates the keys to be replaced with values in a given html page.
        _app: A Flaks app object.
        _page: Name of target html page in the folder 'templates'.

    Examples:
        Code.
        <code>
            app = Flask(__name__)
            template = Template(app, 'TemplateModule.html', '/', {'name': 'Jason'})
            app.run()
        </code>

        And html page.
        <html>
            <h1>Hello, {{name}}!!</h1>
            would be
            <h1>Hello, Jason!!</h1>
        </html>
    """

    def __init__(self, app, page="index.html", url="/", **placeholder):
        """
        :param app: receives the Flask() app object, currently necessary.
        :param page: receives an HTML page for template.
        :param url: receives a string as an url for the html page.
        :param placeholder: receives a dictionary of keyword for templating. {key: value}.
        """
        self._placeholder = placeholder
        self._app = app
        self._page = page
        self.__render(url)

    def __render(self, url):
        """This private function will be called by the constructor"""
        @self._app.route(url)
        def page():
            return render_template(self._page, **self._placeholder)
        return
