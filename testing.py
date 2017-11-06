from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('identicon.png')
img.thumbnail((64, 64), Image.ANTIALIAS)

plt.imshow(img)
