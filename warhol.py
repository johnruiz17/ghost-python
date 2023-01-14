"""
File: warhol.py
---------------
This program takes an image and duplicates it six times, each duplicate being filtered differently to create
an image that is similar to one of Andy Warhol's paintings. The final image is a 3 x 2 Warhol style painting.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

# Name of file that we will use to create the warhol image
IMAGE_FILE = 'images/simba.jpg'


def create_filtered_image(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol program. It creates an
    image object from the image in the file IMAGE_FILE, and then recolors the image
    object.  The parameters to this function are:
      red_scale: A number to multiply each pixels' red component by
      green_scale: A number to multiply each pixels' green component by
      blue_scale: A number to multiply each pixels' blue component by
    This function should return a newly generated image with the appropriately
    scaled color values of the pixels.
    """

    image = SimpleImage(IMAGE_FILE)

    # For each pixel in the image, multiplies red, green, and blue values by their respective scales.
    for pixel in image:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale

    return image


def make_warhol():
    """
    This function generates a Warhol-style picture based on the original image in the
    file IMAGE_FILE.  The Warhol image contains "patches" that are different colored
    versions of the original image.  This function returns the Warhol image.
    """

    # Warhol starts as a blank image that has three times the width and two times the height of the original image.
    image = SimpleImage(IMAGE_FILE)
    width = image.width
    height = image.height
    warhol_width = width * 3
    warhol_height = height * 2
    warhol = SimpleImage.blank(warhol_width, warhol_height)

    # Create six distinct images for the final Warhol image.
    image_1 = create_filtered_image(0, 2, 1)
    image_2 = create_filtered_image(0, 0, 2)
    image_3 = create_filtered_image(1, 0, 1)
    image_4 = create_filtered_image(2, 2, 3)
    image_5 = create_filtered_image(0, 1, 1)
    image_6 = create_filtered_image(3, 2, 0)

    # For each pixel in Warhol, conditionally set pixel based on current x and y values.
    for y in range(warhol_height):
        for x in range(warhol_width):
            if y < height:                                      # row 1
                if x < width:                                   # column 1
                    pixel = image_1.get_pixel(x, y)
                    warhol.set_pixel(x, y, pixel)
                elif width < x < width * 2:                     # column 2
                    pixel = image_2.get_pixel(x - width, y)
                    warhol.set_pixel(x, y, pixel)
                elif width * 2 < x < width * 3:                 # column 3
                    pixel = image_3.get_pixel(x - (width * 2), y)
                    warhol.set_pixel(x, y, pixel)
            elif height < y < height * 2:                       # row 2
                if x < width:                                   # column 1
                    pixel = image_4.get_pixel(x, y - width)
                    warhol.set_pixel(x, y, pixel)
                elif width < x < width * 2:                     # column 2
                    pixel = image_5.get_pixel(x - width, y - width)
                    warhol.set_pixel(x, y, pixel)
                elif width * 2 < x < width * 3:                 # column 3
                    pixel = image_6.get_pixel(x - (width * 2), y - width)
                    warhol.set_pixel(x, y, pixel)

    return warhol


def main():
    """
    This program tests your create_filtered_image and make_warhol functions by calling
    those functions and displaying the resulting images.  Feel free to modify this code
    when you are writing your program.  For example, the call to the create_filtered_image
    function is provided to test that function by itself.  Feel free to delete that portion
    of the code when you have the create_filtered_image working, and then just focus on
    the make_warhol function.
    """

    warhol_image = make_warhol()
    if warhol_image != None:
        warhol_image.show()




if __name__ == '__main__':
    main()
