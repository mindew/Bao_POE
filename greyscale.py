from PIL import Image
import numpy as NP

im = Image.open('heart_pixelated.jpg')
width, height = im.size

total = 0
for i in range(0, width):
    for j in range(0, height):
        total += img.getpixel((i,j))[0]
