
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from generate_conturs import *
from tkinter import *
import math
from tkinter import filedialog as fd

class Window(Tk):
	def __init__(self):
		super().__init__()
		self.__configure()

	def __configure(self):
		self.title("Mitsubishi_draw")
		top_frame = Frame(self, height = 2, bg = "#3F3C3C")
		top_frame.pack(side = TOP, fill = X)
		self.right_frame = Frame(self, width = 15,height = 10,bg = "#3F3C3C")
		self.right_frame.pack(side = RIGHT, fill = Y)

		self.A = IntVar()
		self.B = IntVar()
		self.C = IntVar()

		Label(top_frame, bg = "#3F3C3C", fg = "white").pack(side = TOP, fill = X)
		Label(text = "Изображение", bg = "#2B2E62", fg = "white").pack(side = TOP, fill = X)
		Button(self.right_frame, text = "Выбрать",height = 3, bg = "#344868", fg = "white", command = self.__choose_file).pack(side = TOP, fill = X)
		Label(self.right_frame, text = "minVal", width = 15,height = 3, bg = "#2B2E62", fg = "white").pack(fill = X)
		Scale(self.right_frame, orient = HORIZONTAL, from_ = 0, to = 255, variable = self.A, command = self.__painting).pack(fill = X)
		Label(self.right_frame, text = "maxVal", width = 15,height = 3, bg = "#2B2E62", fg = "white").pack(fill = X)
		Scale(self.right_frame, orient = HORIZONTAL, from_ = 0, to = 255, variable = self.B, command = self.__painting).pack(fill = X)
		Label(self.right_frame, text = "линий", width = 15,height = 4, bg = "#2B2E62", fg = "white").pack(fill = X)	
		self.label_lines = Label(self.right_frame, text = "0", height = 2, bg = "#3F3C3C", fg = "white")	
		self.label_lines.pack(fill = Y)	
		Button(self.right_frame, text = "Компелировать", height = 3, bg = "#344868", fg = "white").pack(side = BOTTOM, fill = X)
		self.canvas = Canvas( width = 640, height = 480, bg="white")
		self.canvas.pack()

	def __painting(self, _in):
		try:
			lines = 0
			self.canvas.delete("all")
			contours = generate_conturs(self.filename, self.A.get(),self.B.get())
			for contur in contours:
				points = []
				for point in contur:
					points += [point[0][0],point[0][1]]
					lines += 1
				try:
					self.label_lines["text"] = lines	
					self.canvas.create_line(points, width = 2)
				except TclError:
					pass					
		except AttributeError:
			pass
		except NameError:
			pass
		
	def __choose_file(self):
		self.filename = fd.askopenfilename(title="Открыть файл", initialdir = "image",
			filetypes=( 
				("PNG files", "*.png"),
				("JPG files", "*.jpg"),
				("All files", "*.*"),
			)
		)
		self.canvas.delete("all")
		self.A.set(0)
		self.B.set(0)
		self.C.set(0)

if __name__ == "__main__":
	window = Window()
	window.mainloop()
	

