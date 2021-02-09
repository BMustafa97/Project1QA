import sys
sys.path.append('/Users/Admin/PycharmProjects/Project1QA')   #alter with path changes
from app import app, db, Todo
import unittest
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///testdb.sqlite"
        return app
    # Pass in configurations for test database
    def setUp(self):
        db.drop_all()
        db.create_all()
        #sample data
        test_todo = Todo(id='1', task='workout', complete=False)
        db.session.add(test_todo)
        db.session.commit()

    #  Will be called before every test

    def tearDown(self):
        db.drop_all()

class TestPages(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add1(self):
        response = self.client.get(url_for('add'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
#below checks if data has been entered correctly or not
    def test_add(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'workout', response.data)

