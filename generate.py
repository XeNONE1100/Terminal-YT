

# import random
import subprocess
import time, sys
from settings import FPS




# Third party modules
# from PIL import ImageGrab, Image
try:
    video_url = sys.argv[1]
except IndexError:
    video_url = input("input video url: ")


video_url = video_url.split("&pp=")[0]
subprocess.Popen("rm -rf frames", shell=True).wait()
subprocess.Popen("rm video.mp4", shell=True).wait()
subprocess.Popen("rm video.mkv", shell=True).wait()
# subprocess.Popen("rm video_max.mp4", shell=True).wait()
subprocess.Popen("rm audio.mp3", shell=True).wait()
subprocess.Popen("mkdir frames", shell=True).wait()
if FPS != 15:
    subprocess.Popen("yt-dlp -o audio.mp3 -f ba --audio-format mp3 -x " + video_url, shell=True)
    subprocess.Popen("yt-dlp -o video.mkv -f wv -S +size,+br,+res --remux-video mkv " + video_url, shell=True).wait()
    # subprocess.Popen("ffmpeg -i video_max.mkv -filter:v fps={fps} video.mkv", shell=True).wait()
    time.sleep(1)
    # subprocess.Popen("ffmpeg -i video.mkv ./frames/frame_%d.jpg", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    subprocess.Popen(f"ffmpeg -i video.mkv -filter:v fps={FPS} ./frames/frame_%d.jpg", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    # time.sleep(1)
    # subprocess.Popen("python3 player.py", shell=True).wait()
else:
    subprocess.Popen("yt-dlp -o audio.mp3 -f ba --audio-format mp3 -x " + video_url, shell=True)
    subprocess.Popen("yt-dlp -o video.mkv -f wv --remux-video mkv " + video_url, shell=True).wait()
    # subprocess.Popen(f"ffmpeg -i video_max.mp4 -filter:v fps={fps} video.mp4", shell=True).wait()
    subprocess.Popen(f"ffmpeg -i video.mkv -filter:v fps={FPS} ./frames/frame_%d.jpg", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)