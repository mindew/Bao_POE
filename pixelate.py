# Credits to: https://gist.github.com/scottrogowski/c3c474a04d7c0cd8ddeb

# This script will pixelate most jpg
# and convert the pixelated image into grayscale
# It will both show you the result and save it
# shown image color looks off than what it is supposed to be,
# maybe because of conflict between PIL library and scipy.
# however, when you save the image, it works perfectly fine
# works in python 3

import sys
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
import scipy.misc as misc
import csv

grayvalues = []


def load_img(filename):
    # boilerplate code to open an image and make it editable
    # opens the file and convert it into grayscale by using PIL mode
    img = Image.open(filename)
    data = np.array(img)
    # convert a grayscale image into array of data
    return data


def all_square_pixels(row, col, square_h, square_w):
    # Every pixel for a single "square" (superpixel)
    # Note that different squares might have different dimensions in order to
    # not have extra pixels at the edge not in a square. Hence: int(round())
    for y in range(int(round(row*square_h)), int(round((row+1)*square_h))):
        # renders through row values
        for x in range(int(round(col*square_w)), int(round((col+1)*square_w))):
            # renders through column values
            yield y, x
            # yield reads only once, number of pixels in original image


def make_one_square(img, row, col, square_h, square_w):
    # Sets all the pixels in img for the square given by (row, col) to that
    # square's average color
    pixels = []

    # get all pixels
    for y, x in all_square_pixels(row, col, square_h, square_w):
        pixels.append(img[y][x])

    # get the average color
    av_r = 0
    av_g = 0
    av_b = 0

    for r, g, b in pixels:
        # add rgb values as it goes through for loop
        av_r += r
        av_g += g
        av_b += b
    av_r /= len(pixels)
    av_g /= len(pixels)
    av_b /= len(pixels)

    # set all pixels to that average color
    for y, x in all_square_pixels(row, col, square_h, square_w):
        img[y][x] = (av_r, av_g, av_b)
    # print(av_r, av_g, av_b)
    avg_Gray = int(round(0.2989 * av_r + 0.5879 * av_g + 0.1140 * av_b))
    print(avg_Gray)
    grayvalues.append(avg_Gray)


def rgb2gray(rgb):
    # converts rgb value into grayscale
    # grabs the rgb data from an image and converts it into intensity
    # Y' = 0.2989r + 0.5879g + 0.1140b is used for formula
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5879 * g + 0.1140 * b

    return gray


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        # save user's input on cmd line as filename
    except IndexError:
        filename = input("Choose an image to pixelate ")
        # if there's no input with keyboard, ask what image to pixelate
    img = load_img(filename)
    # load the iamge

    # Figure out the dimensions of each square
    num_cols = int(input("How many squares from left to right? "))
    # width of the square
    square_w = float(img.shape[1]) / num_cols

    # determine the row number based on the width of the square
    num_rows = int(round(img.shape[0] / square_w))
    # height of the square
    square_h = float(img.shape[0]) / num_rows

    # overwrite each square with the average color, one by one
    # basically, part of an image is colored as average color
    # call function for entire image
    for row in range(num_rows):
        for col in range(num_cols):
            make_one_square(img, row, col, square_h, square_w)

csvfile = "/home/minju/Bao_POE/Grayscalve_Vals.csv"
foo = open(csvfile, 'w')
foo.truncate()
foo.close()

with open(csvfile, 'a') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows([[vals] for vals in grayvalues])

    # convert the image into gray scale
    # if you want to use rgb image, just comment this line out
    gray = rgb2gray(img)

    # show the image
    plt.axis('off')
    plt.imshow(gray, cmap='gray')
    plt.show()

    # save the image as filename_pixelated
    filename_parts = filename.rsplit('.', 1)
    filename_parts[0] += '_pixelated'
    filename = '.'.join(filename_parts)
    print("Saving Pixelated Image")

misc.imsave(filename, gray)
