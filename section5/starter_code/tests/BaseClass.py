'''
Base class for all non-unit tests
'''

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    # Making sure database exists
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Getting a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # Cleaning up database
        with app.app_context():
            db.session.remove()
            db.drop_all()