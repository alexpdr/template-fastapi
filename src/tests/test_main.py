"""
File contains tests for the main application file
"""
from unittest import TestCase

from webtest_asgi import TestApp

from src.main import app

TestApp.__test__ = False


class TestMain(TestCase):
    """
    Contains tests for the main application file
    """

    app: TestApp

    def setUp(self):
        """Sets up test env"""
        self.app = TestApp(app)
