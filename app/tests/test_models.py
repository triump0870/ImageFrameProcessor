import os
import unittest
from unittest.mock import patch

from flask import Flask

from app import db
from app.models import ImageData, save_to_database


class TestImageDataModel(unittest.TestCase):
    def setUp(self):
        # Create an in-memory database for testing
        os.environ['FLASK_ENV'] = 'testing'
        self.app = Flask(__name__)
        self.app.config.from_object('app.config.TestingConfig')
        db.init_app(self.app)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        del os.environ['FLASK_ENV']
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_image_data_model(self):
        # Create a sample ImageData instance
        image_data = ImageData(depth=10.5, pixel_data=b'\x00\x01\x02\x03')
        # Save the instance to the in-memory database
        with self.app.app_context():
            db.session.add(image_data)
            db.session.commit()

            # Retrieve the instance from the database
            retrieved_image_data = ImageData.query.first()

        # Assert that the retrieved instance matches the original one
        self.assertIsNotNone(retrieved_image_data)
        self.assertEqual(retrieved_image_data.depth, 10.5)
        self.assertEqual(retrieved_image_data.pixel_data, b'\x00\x01\x02\x03')

    @patch('app.models.db.session.add')
    @patch('app.models.db.session.commit')
    def test_save_to_database(self, mock_add, mock_commit):
        # Mocking the add and commit methods to avoid actual database operations in the test
        depth = 10.5
        pixel_data = b'\x00\x01\x02\x03'

        save_to_database(depth, pixel_data)

        mock_add.assert_called_once()
        mock_commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
