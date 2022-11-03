import unittest
import main.TemplateModule as TemplateModule
from flask import Flask


class TestTemplateModule(unittest.TestCase):
    """
    Unit test for TemplateModule.py
    """

    app = None
    tp = None
    placeholder = None
    url = None

    def reset(self):
        # dictionary for keywords to be replaced with content, {keyword: content}
        self.placeholder = {"title": "User", "content2": "this is content2", "content3": "this is content3",
                            "content4": "this is content4", "content5": "this is content5"}

        # flask app object, is necessary
        self.app = Flask(__name__)

        # template title template
        self.url = "/"

        # instantiation of Template class, with given flask app, html page, and keywords to be templated.
        self.tp = TemplateModule.Template(self.app, "TemplateModule.html", self.url, **self.placeholder)

        # run the flask web app
        self.app.run()

    def test_something(self):
        # Running on http://127.0.0.1:5000 as default for a flask app.
        # It will keep running the server until you terminate it manually.
        # you may terminate the program in both 'Run' and 'Python Console' tabs.
        self.reset()


if __name__ == '__main__':
    unittest.main()
