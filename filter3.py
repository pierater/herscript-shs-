
from PIL import Image


def filter3(im):
	
	pixels = im.load
	width, height = im.size
	im.show()
	newImage = Image.new('L', (width, height) )

	for x in range(0, width):
		for y in range(0, height):
			r,g,b = im.getpixel((x,y))
			value = r*299 / 1000 + g*587/1000 + b*114/1000
			newImage.putpixel((x,y), value)			
			
	newImage.save("new.png")
	newImage.show()

