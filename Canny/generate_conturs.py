
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *

def resize_img(picture):
	try:
		img = cv.imread(picture, 0)
		x, y = img.shape
		if x / y > 1.33:
			k = 640 / x
			img = cv.resize(img, (640, int(k * y)))
		else:
			k = 480 / y
			img = cv.resize(img, (int(k * y), 480))
		return img
	except AttributeError:
		pass

def generate_conturs(img, minVal = 100, maxVal = 200):
	img = resize_img(img)
	contours, _ = cv.findContours(cv.Canny(img,minVal,maxVal), cv.RETR_LIST, cv.CHAIN_APPROX_TC89_KCOS)
	return contours


if __name__ == "__main__":
	root = Tk()
	canvas = Canvas(root, width = 640, height = 480, bg="white")
	canvas.pack()
	contours = generate_conturs('/home/vadim/git/mitsubishi_draw/Canny/image/test.jpg', minVal = 100, maxVal = 200)
	for contur in contours:
		points = []
		for point in contur:
			points += [point[0][0],point[0][1]]
			print(points)
			print('---------------------------')
		try:
			canvas.create_line(points, width = 2)
		except TclError:
			pass
			
	root.mainloop()
		
					

	

