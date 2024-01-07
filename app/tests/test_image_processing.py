import unittest
from unittest.mock import patch, MagicMock
from PIL import Image
import numpy as np
from app.image_processing import resize_image, get_image_data, generate_frames, apply_custom_color_map, visualize_frames


class TestImageProcessing(unittest.TestCase):
    def setUp(self):
        # Sample pixel values for testing
        self.sample_pixel_values = list(range(200))

    def test_resize_image(self):
        resized_pixel_values = resize_image(self.sample_pixel_values)
        self.assertIsInstance(resized_pixel_values, bytes)

        # Assuming the resized image has width 150
        resized_img = Image.frombytes('L', (150, 1), resized_pixel_values)
        self.assertEqual(resized_img.width, 150)

    def test_get_image_data(self):
        # Mocking np.genfromtxt to avoid actual file read in the test
        with patch('numpy.genfromtxt') as mock_genfromtxt:
            mock_genfromtxt.return_value = np.zeros((3, 201))  # Assuming 3 rows of data with 201 columns
            image_data = get_image_data()
            self.assertIsInstance(image_data, np.ndarray)
            self.assertEqual(image_data.shape, (3, 201))

    def test_generate_frames(self):
        # Mocking apply_custom_color_map to avoid actual colormap computation in the test
        with patch('app.image_processing.apply_custom_color_map') as mock_apply_custom_color_map:
            mock_apply_custom_color_map.return_value = [np.zeros(
                (10, 10, 3))] * 3  # Assuming 3 frames of size (10, 10, 3)
            image_mock = MagicMock()
            image_mock.pixel_data = np.zeros(200)

            frames = generate_frames(image_mock)
            self.assertIsInstance(frames, list)
            self.assertEqual(len(frames), 3)

    def test_apply_custom_color_map(self):
        pixel_values = bytes(np.zeros(200).astype('uint8'))
        colored_frames = apply_custom_color_map(pixel_values)
        self.assertIsInstance(colored_frames, list)
        self.assertEqual(len(colored_frames), 200)

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.subplot')
    @patch('matplotlib.pyplot.imshow')
    @patch('matplotlib.pyplot.axis')
    @patch('matplotlib.pyplot.figure')
    def test_visualize_frames(self, mock_figure, mock_axis, mock_imshow, mock_subplot, mock_show):
        frames = [np.zeros((10, 10, 3))] * 5  # Assuming 5 frames of size (10, 10, 3)
        visualize_frames(frames)
        mock_figure.assert_called_once()
        mock_subplot.assert_called()
        mock_imshow.assert_called()
        mock_axis.assert_called()
        mock_show.assert_called_once()


if __name__ == '__main__':
    unittest.main()
