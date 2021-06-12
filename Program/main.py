
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

from tkinter import *
from tkinter import filedialog as fd
import tkinter.messagebox as mb
from ttk import Progressbar

from generate_program import *
from generate_contours import *


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
		self.bottom_frame = Frame(self, height = 55,bg = "#3F3C3C")
		self.bottom_frame.pack(side = BOTTOM, fill = X) 
		self.canvas_frame = Frame(self)
		self.canvas_frame.pack(side = BOTTOM, expand=1) 
		


		Label(top_frame, bg = "#3F3C3C", fg = "white").pack(side = TOP, fill = X)
		Label(text = "Изображение", bg = "#2B2E62", fg = "white").pack(side = TOP, fill = X)
		Button(self.right_frame, text = "Выбрать",
				height = 3, bg = "#344868", fg = "white", command = self.__choose_file).pack(side = TOP, fill = X)
		Label(self.right_frame, text = "minVal",
				width = 15,height = 3, bg = "#2B2E62", fg = "white").pack(fill = X)
		self.A = IntVar()
		self.B = IntVar()
		Scale(self.right_frame, orient = HORIZONTAL,
				from_ = 0, to = 255, variable = self.A, command = self.__updating_scale).pack(fill = X)
		Label(self.right_frame, text = "maxVal",
				width = 15,height = 3, bg = "#2B2E62", fg = "white").pack(fill = X)
		Scale(self.right_frame, orient = HORIZONTAL, 
				from_ = 0, to = 255, variable = self.B, command = self.__updating_scale).pack(fill = X)
		Label(self.right_frame, text = "линий",
				width = 15,height = 4, bg = "#2B2E62", fg = "white").pack(fill = X)	
		self.label_lines = Label(self.right_frame, text = "0", height = 2, bg = "#3F3C3C", fg = "white")	
		self.label_lines.pack(fill = Y)	
		self.status = Label(self.right_frame, text = "Выберете файл",width = 15,height = 3, bg = "#FCC02E", fg = 'black')
		self.status.pack(side = BOTTOM, fill = X)
		Button(self.right_frame, text = "Экспорт",
		height = 3, bg = "#344868", fg = "white", command = self.__save_file).pack(side = BOTTOM, fill = X)
		self.canvas = Canvas(self.canvas_frame, width = 640, height = 480, bg="white")
		self.canvas.pack()
	
	def __updating_scale(self, __in):
		try:
			self.__start_painting_contours(self.file_name, self.A.get(), self.B.get())
		except AttributeError:
			self.__print_status('Выберете файл','warning')

	def __start_painting_contours(self, file_name, A, B):
		try:
			if file_name == '': raise AttributeError()
			contours = generate_contours(file_name, A, B)
			self.canvas.delete("all")
			self.after(50, self.__painting_contours, 0, contours, 0)
			self.contours = contours
		except AttributeError:
			self.__print_status('Выберете файл','warning')			
		except NameError:
			pass	

	def __painting_contours(self, i, contours, lines):
		try:
			contour = contours[i]
			i += 1
			points = []
			for point in contour:
				points += [point[0][0],point[0][1]]
				lines += 1
			try:
				self.canvas.create_line(points, width = 2)
				self.label_lines["text"] = lines
			except TclError:
				pass
			self.after(1, self.__painting_contours, i, contours, lines)	
		except IndexError:
			self.__print_status('Отрисовано','success')	
		else:
			self.__print_status('Подождите','warning')

	def __print_status(self,text,status):
		self.status['text'] = text
		if status == 'success':
			self.status['bg'] = '#009460'
			self.status['fg'] = 'white'
		elif status == 'warning':
			self.status['bg'] = '#FCC02E'
			self.status['fg'] = 'black'
		elif status == 'trouble':
			self.status['bg'] = '#CE1126'
			self.status['fg'] = 'white'

	def __show_warning(self):
		msg = "Во избежание коллизий, первый запуск производится в ручном режиме"
		mb.showwarning("Предупреждение", msg)

	def __choose_file(self):
		try:
			self.file_name = fd.askopenfilename(title = "Открыть файл", initialdir = "image",
				filetypes = ( 
					("PNG files", "*.png"),
					("JPG files", "*.jpg"),
					("All files", "*.*"),
				)
			)
			self.canvas.delete("all")
			self.A.set(0)
			self.B.set(0)
			self.label_lines["text"] = '0'
		except AttributeError:
			self.__print_status('Выберете файл','warning')

	def __save_file(self):
			new_file = fd.asksaveasfile(title="Сохранить файл", initialdir = "programs", defaultextension=".prg",
										filetypes=(("Текстовый файл", "*.prg"),))
			if new_file:
				new_file.write(create_program(self.contours))
				new_file.close()
				self.__print_status('Экспортировано','success')
				self.__show_warning()


if __name__ == "__main__":
	window = Window()
	window.mainloop()
	