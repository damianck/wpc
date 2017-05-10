import unittest
from media.video_converter import VideoConverter
import os


class TestVideoConverter(unittest.TestCase):
        def test_transform_to_video(self):
                image_path= os.path.join(os.path.dirname(__file__), 'example.jpg')
                video_output_path= os.path.join(os.path.dirname(__file__), 'example.mov')
                converter=VideoConverter()
                converter.create_video_from_image(image_path, video_output_path)
                assert os.path.exists(video_output_path) #isFile()


