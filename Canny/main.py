
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
import generate_lines as gl
from tkinter import *



class Window(Tk):

	def __init__(self):

		super().__init__()
		self.title("Mitsubishi_draw")
		top_frame = Frame(self, height = 2, bg = "#3F3C3C")
		top_frame.pack(side = TOP, fill = X)
		self.right_frame = Frame(self, width = 15,height = 10,bg = "#3F3C3C")
		self.right_frame.pack(side = RIGHT, fill = Y)
		
		
		Label(top_frame, bg = "#3F3C3C", fg = "white").pack(side = TOP, fill = X)
		Label(text = "Изображение", bg = "#2B2E62", fg = "white").pack(side = TOP, fill = X)
		Button(self.right_frame, text = "Выбрать",height = 3, bg = "#344868", fg = "white").pack(side = TOP, fill = X)
		Label(self.right_frame, text = "minVal", width = 15,height = 3, bg = "#2B2E62", fg = "white").pack(fill = X)
		Scale(self.right_frame, orient = HORIZONTAL, from_ = 0, to = 255).pack(fill = X)
		Label(self.right_frame, text = "maxVal", width = 15,height = 3, bg = "#2B2E62", fg = "white").pack(fill = X)
		Scale(self.right_frame, orient = HORIZONTAL, from_ = 0, to = 255).pack(fill = X)
		Label(self.right_frame, text = "maxLenght", width = 15,height = 3, bg = "#2B2E62", fg = "white").pack(fill = X)
		Scale(self.right_frame, orient = HORIZONTAL, from_ = 0, to = 255).pack(fill = X)
		Label(self.right_frame, text = "линий", width = 15,height = 2, bg = "#2B2E62", fg = "white").pack(fill = X)	
		self.label_lines = Label(self.right_frame, text = "0", height = 2, bg = "#3F3C3C", fg = "white")	
		self.label_lines.pack(fill = Y)	
		Button(self.right_frame, text = "Компелировать",height = 3, bg = "#344868", fg = "white").pack(side = BOTTOM, fill = X)
		self.canvas = Canvas( width = 640, height = 480, bg="white")
		self.canvas.pack()


	def painting(self, img = 'test.jpg', minVal = 100, maxVal = 200, maxLength = 50):
		generate = gl.Generate_lines(img)
		line_list, self.lines  = generate.return_list(minVal, maxVal, maxLength)

		parity = 0
		for i in line_list:
			parity += 1;
			if parity % 2 == 1:
				point_1 = i
			else:
				point_2 = i
				self.canvas.create_line(point_1, point_2)
		self.label_lines["text"] = self.lines


	

	
if __name__ == "__main__":
	window = Window()
	window.painting("img_1.jpg", 100, 200, 20)
	window.mainloop()
	

