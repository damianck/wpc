import subprocess

class VideoConverter():
        def create_video_from_image(self,image_path, video_output_path):
                cmd="ffmpeg -loop 1 -i %s -t 2 -c:v libx264 -preset ultrafast -pix_fmt yuv420p %s"%(image_path,video_output_path)
                subprocess.call(cmd, shell=True)




