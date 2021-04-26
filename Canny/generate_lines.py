
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math

def resize_img(picture):
	try:
		img = cv.imread('image/' + picture, 0)
		x, y = img.shape
		if x / y > 1.33:
			k = 640 / x
			img = cv.resize(img, (640, int(k * y)))
		else:
			k = 480 / y
			img = cv.resize(img, (int(k * y), 480))
		return img
	except AttributeError:
		raise ValueError('%s is not an image' % fname)

def line_length(a,b):
	x1,y1 = a
	x2,y2 = b
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

class Generate_lines():
	def __init__(self, picture = 'test.jpg'):
		self.img = resize_img(picture)

	def return_list(self, minVal = 100, maxVal = 200, maxLength = 50):
		lines_list = list()
		self.lines = 0
		self.point_1 = (0,0) 
		self.point_2 = (0,0)
		parity = 0
		contours,hierarchy = cv.findContours(cv.Canny(self.img,minVal,maxVal), cv.RETR_LIST, cv.CHAIN_APPROX_TC89_KCOS)
		for a in contours:
			for b in a:
				parity += 1
				for x,y in b:
					if parity % 2 == 1:
							point_1 = (x,y) 
					else:
						point_2 = (x,y)
				if parity > 2 and  line_length(point_1,point_2) < maxLength:
					self.lines += 1
					lines_list.append(point_1)
					lines_list.append(point_2)
		return lines_list, self.lines

			
if __name__ == "__main__":
	generate = Generate_lines()
	background = cv.imread('image/background.jpg',0)
	parity = 0
	line_list, lines = generate.return_list()
	for i in line_list:
		parity += 1;
		if parity % 2 == 1:
			point_1 = i
		else:
			point_2 = i
			cv.line(background, (point_1), (point_2), (43, 42, 41), 1)		
	print(lines," ", "линий")
	print(line_list)
	cv.imshow('contour',background)
	cv.waitKey(0)
	cv.destroyAllWindows()
	

	

