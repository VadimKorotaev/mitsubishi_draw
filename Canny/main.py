
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

from tkinter import *
from tkinter import filedialog as fd
from ttk import Progressbar

from generate_contours import *
from generate_prg import * 

class Window(Tk):
	def __init__(self):
		super().__init__()
		self.__configure_window()

	def __configure_window(self):
		self.title("Mitsubishi_draw")
		top_frame = Frame(self, height = 2, bg = "#3F3C3C")
		top_frame.pack(side = TOP, fill = X)
		self.right_frame = Frame(self, width = 15,height = 10,bg = "#3F3C3C")
		self.right_frame.pack(side = RIGHT, fill = Y)


		Label(top_frame, bg = "#3F3C3C", fg = "white").pack(side = TOP, fill = X)
		Label(text = "Изображение", bg = "#2B2E62", fg = "white").pack(side = TOP, fill = X)
		Button(self.right_frame, text = "Выбрать",
				height = 3, bg = "#344868", fg = "white", command = self.__choose_file).pack(side = TOP, fill = X)
		Label(self.right_frame, text = "minVal",
				width = 15,height = 3, bg = "#2B2E62", fg = "white").pack(fill = X)
		self.A = IntVar()
		self.B = IntVar()
		Scale(self.right_frame, orient = HORIZONTAL,
				from_ = 0, to = 255, variable = self.A, command = self.__painting_contous).pack(fill = X)
		Label(self.right_frame, text = "maxVal",
				width = 15,height = 3, bg = "#2B2E62", fg = "white").pack(fill = X)
		Scale(self.right_frame, orient = HORIZONTAL, 
				from_ = 0, to = 255, variable = self.B, command = self.__painting_contous).pack(fill = X)
		Label(self.right_frame, text = "линий",
				width = 15,height = 4, bg = "#2B2E62", fg = "white").pack(fill = X)	
		self.label_lines = Label(self.right_frame, text = "0", height = 2, bg = "#3F3C3C", fg = "white")	
		self.label_lines.pack(fill = Y)	
		self.bar = Progressbar(self.right_frame,)
		self.bar.pack(side = BOTTOM, fill = X)
		Button(self.right_frame, text = "Экспорт",
		height = 3, bg = "#344868", fg = "white", command = self.___create_program_prg).pack(side = BOTTOM, fill = X)
		self.canvas = Canvas(width = 640, height = 480, bg="white")
		self.canvas.pack()

	def __painting_contous(self, _in):
		try:
			self.canvas.delete("all")
			self.contours = generate_contours(self.filename, self.A.get(),self.B.get())
			lines = 0
			for contur in self.contours:
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

	def ___create_program_prg(self):
		try:
			create_file(self.contours)
		except AttributeError:
			pass
		
	def __choose_file(self):
		self.filename = fd.askopenfilename(title = "Открыть файл", initialdir = "image",
			filetypes = ( 
				("PNG files", "*.png"),
				("JPG files", "*.jpg"),
				("All files", "*.*"),
			)
		)
		self.canvas.delete("all")
		self.A.set(0)
		self.B.set(0)


if __name__ == "__main__":
	window = Window()
	window.mainloop()
	

