
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
import generate_lines as gl
from tkinter import *



root = Tk()

def paintig(img = 'test.jpg', minVal = 100, maxVal = 200, maxLength = 50):
	generate = gl.Generate_lines(img)
	line_list, lines  = generate.return_list(minVal, maxVal, maxLength)
	c = Canvas(root, width=640, height=480, bg='white')
	c.pack()
	parity = 0
	for i in line_list:
		parity += 1;
		if parity % 2 == 1:
			point_1 = i
		else:
			point_2 = i
			c.create_line(point_1, point_2)
	return lines


if __name__ == "__main__":
	lines = paintig("img_1.jpg", 100, 200, 20)
	print (lines)
	root.mainloop()



