from PIL import Image
<<<<<<< HEAD
import numpy as np

im = Image.open('heart.jpg', mode = 'r')


Image.show(im)
=======
import numpy as NP

im = Image.open('heart_pixelated.jpg')
width, height = im.size

total = 0
for i in range(0, width):
    for j in range(0, height):
        total += img.getpixel((i,j))[0]
>>>>>>> 75f07672cdb33a891d35f026ec2e8db70e174f79
