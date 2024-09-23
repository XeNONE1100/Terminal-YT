
a python program that allows to play videos with RGB text

showcase (old version): https://youtu.be/lPYZlZw9rvg

if you want to play a video by changing background color (closest to original video) use:

$ python3 player.py

if you want to play a video using colored ascii characters use:

$ python3 player-ascii.py

if you want to change the video, use:

$ python3 generate.py [video link]


the video resulution automatically scales to the terminal size
increase / decrease pixels displayed by zooming in / out of the terminal
( ! BIG RESOLUTIONS WILL BE VERY LAGGY ! )

also this code may not run if you dont have a gpu due to numba
(i didnt test it so if it breaks, just remove numba from imports and remove the @ njit thingies)

external libraries used:
pillow [PIL] (loading images! no displaying)
pygame (used only for audio)
numba (for improving performance)