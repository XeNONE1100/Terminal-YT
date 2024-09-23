from shutil import get_terminal_size

from pygame import mixer
from time import time
from sys import stdout
from PIL import Image, UnidentifiedImageError

from settings import FPS

CHARACTERS = " .;coO?$0P8"


def display_update(frame):
    new_width, new_height = get_terminal_size()
    pix = Image.open(f'./frames/frame_{frame}.jpg').resize((new_width, new_height)).load()

    text = "\u001B[0;0H" # goto pos 0,0 (top left)
    for y in range(new_height):
        for x in range(new_width):
            px = pix[x,y]


            text += f"\x1b[48;2;{px[0]};{px[1]};{px[2]}m "


    stdout.write(text)
    stdout.flush()




if __name__ == "__main__":

    is_loaded = False

    file = 'audio.mp3'
    stdout.write("\x1b[48;2;0;0;0m") # make background black
    mixer.pre_init(44100, -16, 2, 512)
    mixer.init(buffer=64)
    while not is_loaded:
        try:
            image = Image.open('./frames/frame_60.jpg')
            is_loaded = True
        except (FileNotFoundError,UnidentifiedImageError):
            # sleep(0.2)
            pass
    start_time = time()
    frame_count = 0
    print("\n")
    a = True
    while True:
        # print("WORKING")
        if (time() - start_time) * FPS > frame_count:
            if (time() - start_time) * FPS > frame_count +1:
                frame_count += 5
            frame_count += 1
            display_update(frame_count)
        if a:
            mixer.music.load(file)
            mixer.music.play()
            a = False


    print("Stopped")
