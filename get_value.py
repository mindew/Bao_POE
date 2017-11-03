from PIL import Image

img = Image.open('heart_pixelated.jpg').convert('L')
width, height = img.size

data = list(img.getdata())    # convert image data to a list of integers
# convert that to 2D list (list of integers)
data = [data[offset:offset+width] for offset in range(0, width*height, width)]

for y in range(height):
    row = (data[y][x] for x in range(width))
    print(''.join('{:3}'.format(value) for value in row))
