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

    :param app: receives the Flask() app object, currently necessary.
    :param page: receives a HTML page for template.
    :param title: receives a string to template {{title}} keyword.
    :param **placeholder: receives a dictionary of keyword for templating. {key: value}.
    """

    def __init__(self, app, page="index.html", title=None, **placeholder):
        self._placeholder = placeholder
        self._app = app
        self._page = page
        self.__render(title)
        self.__run()

    def __render(self, title):
        """This function will be called by the constructor"""
        @self._app.route('/')
        @self._app.route('/<ch>')
        def page(ch=title):
            attributes = {
                'title': ch,
                'attributes': self._placeholder
            }
            return render_template(self._page, **attributes)
        return

    def __run(self):
        """This function will be called by the constructor"""
        self._app.run()
        return
