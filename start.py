import time
import asyncio
# import random
# Third party modules
# from PIL import ImageGrab, Image
from PIL import Image
# import sys, os

from settings import new_width, new_height

def colored_print(text,fg=(255,255,255,255),bg=(0,0,0,255), p_end="\n"):
    print(f"\x1b[48;2;{bg[0]};{bg[1]};{bg[2]}m\x1b[38;2;{fg[0]};{fg[1]};{fg[2]}m {text} \x1b[39m\x1b[49m", end=p_end)

async def display_update():

    image = Image.open(f'./apple/frame_{frame_count}.jpg') # Can be many different formats.
    image = image.resize((new_width, new_height))
    pix = image.load()
    print("\033[F" * (100), end = "")
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            colors = pix[x,y]

            ####### UNCOMMENT FOR MAKING STUFF IN 2 DIFFERENT GRADIENTS (like bad apple video):

            # if colors[0] > 127:
            #     colored_print(" ",bg=(x+y,x,y), p_end="")
            # elif colors[0] <= 127:
            #     colored_print(" ",bg=(new_width-x,new_height-y,new_width-x + new_height), p_end="")
            # else:
            colored_print(" ",bg=pix[x,y], p_end="")
        print("")




if __name__ == "__main__":
    start_time = time.time()
    frame_count = 0
    print("\n")

    while True:
        if (time.time() - start_time) * 30 > frame_count:
            frame_count += 1
            asyncio.run(display_update())


    print("Stopped")
