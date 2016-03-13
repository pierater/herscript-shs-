


from filter1 import filter1
#from filter3 import filter3
#from filter2 import filter2

from PIL import Image



def main(im):
	
	choice = '1'
	while(choice != 'q'):

		print "=============================================="
		#im = raw_input("FileName: ")

		im = Image.open(im)

		print "c) Select Picture"
		print "1) filter 1"
		print "2) filter 2"
		print "3) filter 3"
		print "q) quit"

		choice = raw_input("Choice: ")

		if(choice == '1'):
			filter1(im)
		elif(choice == '2'):
			filter2(im)
		elif(choice == '3'):
			filter3(im)
		elif(choice == 'q' or choice == 'Q'):
			break
		elif(choice == 'c' or choice == 'C'):
			im = raw_input("FileName: ")
		else:
			print "Choice not recodnised, try again"
		

im = raw_input("FileName: ")
main(im)

	

	
