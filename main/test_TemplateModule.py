import unittest
from TemplateModule import *
from flask import Flask


class MyTestCase(unittest.TestCase):
    """
    Unit test for TemplateModule.py
    """

    app = None
    tp = None
    placeholder = None
    title = None

    def reset(self):
        # dictionary for keywords to be replaced with content, {keyword: content}
        self.placeholder = {"content2": "this is content2", "content3": "this is content3",
                            "content4": "this is content4", "content5": "this is content5"}

        # flask app object, is necessary
        self.app = Flask(__name__)

        # template title template
        self.title = "Amigo"

        # instantiation of Template class, with given flask app, html page, and keywords to be templated.
        self.tp = Template(self.app, "TemplateModule.html", self.title, **self.placeholder)

    def test_something(self):
        # Running on http://127.0.0.1:5000 as default for a flask app.
        # It will keep running the server until you terminate it manually.
        self.reset()


if __name__ == '__main__':
    unittest.main()
