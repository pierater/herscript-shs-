from PIL import Image

'''
So you have already seen our  other crazy filter with loops and variables
Here I have provided you with a few functions that you can use on your image

-- remember! to keep the changes from each function, you must use like so

ex.
im = im.rotate(45)


LIST:
    
    .save('filename.jpg')
    .show() # will display the image
    .rotate(45) # the 45 represents how many degrees you want to rotate the image
    .resize( (100, 150) ) # will resize your image to the given pixel dimensions
    .transpose(FUNCTION)
        where FUNCTION can be:
            Image.FLIP_LEFT_RIGHT
            Image.FLIP_TOP_BOTTOM
            Image.ROTATE_90
            Image.ROTATE_180
            Image.ROTATE_270
            Image.TRANSPOSE
        example:
            im = im.transpose(Image.FLIP_TOP_BOTTOM)

    PIL.ImageChops.invert(im) # inverts the colors of given image

    PIL.ImageChops.offset(im, 100, 200) # will shift the pixels of the image by 100 (x) coordinates or 200 (y) coordinates


REMEMBER:
    Each of these functions can be used in conjunction with the others,
    this means that you can:
        im = im.rotate(23)
        im = im.resize((100, 100))
'''

# This function will add a filter onto the image
def filter3(im):
    # TODO:
    #   (1) Load the image's pixel data
    #   (2) Get the width and height of the image
    #   (3) Create a new Image
    #   (4) Iterate through every pixel in the image and change its color value
    #   (5) Save the new image you created in (3) as "new.png"
    #   (6) Show the image
