from PIL import Image
import PIL

# this is an example of a filter you will be making!
# 
def filter1(im): # we 'pass in' the image we want to work with, here this 'im' holds our image
	
	pixels = im.load # this gives us all the pixels of an image and put them into a variable called 'pixels'
                    # we can call the variable anything we like, but we named it 'pixels' for readability
	width, height = im.size # we are getting the size (in poxels) of the image we passed in
	im.show() # this does exacly what it says, shows you the image
	newImage = Image.new('L', (width, height) ) # we are creating a new 'empty' image with the same dimensions as the other image

	for x in range(0, width): # this is the begining of our for loop, it means that all the code indented under it will run once for every horizontal pixel
		for y in range(0, height): # this loop is inside the the one above, this 
			r,g,b = im.getpixel((x,y)) # gets the r g b values from a pixel at the given coordinates (x,y)
			value = r*299 / 1000 + g*587/1000 + b*114/1000 # our crazy formular!
			newImage.putpixel((x,y), value)			# here we put the new 'value' that we created into the same (x,y) coordinates that we got our rgb from
			
	newImage.save("new.png") # here we save the new image
	newImage.show() # and show it 

