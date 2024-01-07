import unittest

from flask import jsonify

from app import app, db
from app.image_processing import generate_frames
from app.models import ImageData


class TestFramesResource(unittest.TestCase):
    def setUp(self):
        app.config.from_object('app.config.TestingConfig')
        self.app = app
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

        # Add test data to the database
        test_data = [
            ImageData(depth=5.0, pixel_data=b'\x00\x01\x02\x03'),
            ImageData(depth=8.0, pixel_data=b'\x04\x05\x06\x07'),
            ImageData(depth=12.0, pixel_data=b'\x08\x09\x0A\x0B'),
        ]
        with self.app.app_context():
            db.session.bulk_save_objects(test_data)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_frames(self):
        # Make a test request to the API within the app context
        with self.app.app_context():
            response = self.client.get('/get_frames?depth_min=4.0&depth_max=15.0')
            self.assertEqual(response.status_code, 200)

            # Validate the response content
            expected_frames = [
                generate_frames(ImageData(depth=5.0, pixel_data=b'\x00\x01\x02\x03')),
                generate_frames(ImageData(depth=8.0, pixel_data=b'\x04\x05\x06\x07')),
                generate_frames(ImageData(depth=12.0, pixel_data=b'\x08\x09\x0A\x0B')),
            ]
            expected_response = jsonify(expected_frames).json

            self.assertEqual(response.json, expected_response)

    # Add more test cases as needed based on different scenarios


if __name__ == '__main__':
    unittest.main()
