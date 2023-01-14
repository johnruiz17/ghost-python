"""
File: ghost.py
--------------
This program takes a list of similar images and creates a new image where the the people from the other images are
removed. This program accomplishes this by comparing each pixel in the list of images and determining which pixels
are the outliers by applying the distance formula to determine the distance between a current pixel and the average
of all the pixels. Each pixel that is closest to the average in each pixel location is is chosen as the best pixel
and used to create the final image. The program leaves traces of the removed pixels creating a ghostlike effect.
"""

import os
import sys

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    This Doctest creates a simple green image and tests against
    a pixel of RGB values (0, 0, 255)
    >>> green_im = SimpleImage.blank(20, 20, 'green')
    >>> green_pixel = green_im.get_pixel(0, 0)
    >>> get_pixel_dist(green_pixel, 0, 255, 0)
    0
    >>> get_pixel_dist(green_pixel, 0, 255, 255)
    65025
    >>> get_pixel_dist(green_pixel, 5, 255, 10)
    125
    """
    return ((pixel.red - red) ** 2) + ((pixel.green - green) ** 2) + ((pixel.blue - blue) ** 2)


def get_best_pixel(pixel_list):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across
    all pixels.

    Input:
        a list of pixels to be averaged and compared.  You can assume this list is never empty
    Returns:
        best (Pixel): pixel closest to RGB averages

    This doctest creates a red, green, and blue pixel and runs some simple tests.
    >>> green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    >>> red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    >>> blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    >>> best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    >>> best1.red, best1.green, best1.blue
    (0, 0, 255)
    >>> best2 = get_best_pixel([green_pixel, green_pixel, blue_pixel])
    >>> best2.red, best2.green, best2.blue
    (0, 255, 0)
    >>> best3 = get_best_pixel([red_pixel, red_pixel, red_pixel])
    >>> best3.red, best3.green, best3.blue
    (255, 0, 0)
    """

    # Calculate the averages based on the pixel list that is passed in.
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    color_distances = []

    for pixel in pixel_list:
        red_sum += pixel.red
        green_sum += pixel.green
        blue_sum += pixel.blue

    average_red = red_sum // 3
    average_green = green_sum // 3
    average_blue = blue_sum // 3

    # Make a list of color distances and find the one with the lowest value.
    for pixel in pixel_list:
        color_distance = get_pixel_dist(pixel, average_red, average_green, average_blue)
        color_distances.append(color_distance)

    lowest_color_distance = min(color_distances)

    # Return the pixel with the lowest color distance.
    for pixel in pixel_list:
        if get_pixel_dist(pixel, average_red, average_green, average_blue) == lowest_color_distance:
            return pixel


def create_ghost(image_list):
    """
    Given a list of image objects, this function creates and returns a Ghost
    solution image based on the images passed in. All the images passed
    in will be the same size.

    Input:
        a list images to be processed.  You can assume this list is never empty.
    Returns:
        a new Ghost solution image
    """

    # Create a blank image with the width and height of one of the original images.
    width = image_list[0].width
    height = image_list[0].height
    image = SimpleImage.blank(width, height)

    # For each pixel, create a list of pixels from the list of images and set the best pixel to final image.
    for pixel in image:
        x = pixel.x
        y = pixel.y
        pixel_list = []

        # For each image, get a corresponding pixel and append to pixel_list.
        for img in image_list:
            current_pixel = img.get_pixel(x, y)
            pixel_list.append(current_pixel)

        best_pixel = get_best_pixel(pixel_list)
        image.set_pixel(x, y, best_pixel)

    return image

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def jpgs_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(directory, filename))
    return filenames


def load_images(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(directory)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # DO NOT MODIFY
    args = sys.argv[1:]

    if len(args) != 1:
        print('Please specify directory of images on command line')
        return

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    result = create_ghost(images)
    if result:
        print("Displaying image!")
        result.show()
    else:
        print("No image to display!")


if __name__ == '__main__':
    main()
