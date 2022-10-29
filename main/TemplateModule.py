"""
A solution for HTML templating.

Attributes:
    Flask

Author: Ruixiao Lu
Date: Otc. 2022
"""
from flask import render_template


class Template:
    """
    This is the template module class.
    For more intuitive information, check TemplateModule.html.
    This module is not yet completed, everything depends on how the project goes.
    
    :param app:receives the Flask() app object, currently necessary.
    :param page: receives an HTML page for template.
    :param url: receives a string as an url.
    :param **placeholder: receives a dictionary of keyword for templating. {key: value}.
    """

    def __init__(self, app, page="index.html", url="/", **placeholder):
        self._placeholder = placeholder
        self._app = app
        self._page = page
        self.__render(url)

    def __render(self, url):
        """This function will be called by the constructor"""
        @self._app.route(url)
        def page():
            return render_template(self._page, **self._placeholder)
        return
