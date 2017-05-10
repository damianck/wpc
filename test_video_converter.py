import unittest
from media.video_converter import VideoConverter
import os


class TestVideoConverter(unittest.TestCase):
        def setUp(self):
                video_output_path= get_absolute_path('example.jpg')
                if os.path.isfile(video_output_path):
                        os.remove(video_output_path)

        def test_transform_to_video(self):
                image_path= get_absolute_path('example.jpg')
                video_output_path= get_absolute_path('example.mov')
                converter=VideoConverter()
                converter.create_video_from_image(image_path, video_output_path)
                assert os.path.exists(video_output_path) #isFile()

        def get_absolute_path(self,path):
                return os.path.join(os.path.dirname(__file__), path)


