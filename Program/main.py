import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

from tkinter import *
from tkinter import filedialog as fd
import tkinter.messagebox as mb
from tkinter.ttk import Progressbar
from PIL import ImageTk
from PIL import Image as Img

from generate_program import *
from generate_contours import *


class UnderpaintedError(Exception):
	pass

class AxisError(Exception):
	pass
		
class Window(Tk):
	def __init__(self):
		super().__init__()
		self.__configure_window()

	def __configure_window(self):

		'''Заголовок'''
		self.title("Mitsubishi_draw")

		'''Верхняя панель'''
		top_frame = Frame(self, height = 2, bg = "#3F3C3C")
		top_frame.pack(side = TOP, fill = X)
		Label(top_frame, bg = "#3F3C3C", fg = "white").pack(side = TOP, fill = X)
		Label(text = "Изображение", bg = "#2B2E62", fg = "white").pack(side = TOP, fill = X)

		'''Нижняя панель'''
		self.bottom_frame = Frame(self, height = 55, bg = "#3F3C3C")
		self.bottom_frame.pack(side = BOTTOM, fill = X)

		self.status = Label(self.bottom_frame, text = "Выберете файл",width = 15,height = 3, bg = "#FCC02E", fg = 'black')
		self.status.pack(side = RIGHT, fill = Y)
		'''ось-X'''
		self.label_x_entry = LabelFrame(self.bottom_frame, bg = "#3F3C3C",fg = "white", text = "Ось X")
		self.label_x_entry.pack(side = LEFT, padx = 5, pady = 5)
		self.x_entry_sign = Entry(self.label_x_entry, width = 1, validate = "key",
								 validatecommand = (self.register(self.__validate_entry_sign),"%P",)) 
		self.x_entry_sign.pack(side = LEFT)
		self.x_entry_1 = Entry(self.label_x_entry, width = 3, validate = "key",
								 validatecommand = (self.register(self.__validate_entry_number_1),"%P")) 
		self.x_entry_1.pack(side = LEFT)
		self.point_x = Label(self.label_x_entry, text =".",bg = "#3F3C3C", fg = "white").pack(side = LEFT, padx = 1)
		self.x_entry_2 = Entry(self.label_x_entry, width = 2, validate = "key",
								 validatecommand = (self.register(self.__validate_entry_number_2),"%P")) 
		self.x_entry_2.pack(side = LEFT)
		'''ось-Y'''
		self.label_y_entry = LabelFrame(self.bottom_frame, bg = "#3F3C3C", fg = "white", text = "Ось Y" )
		self.label_y_entry.pack(side = LEFT, padx = 5, pady = 5)
		self.y_entry_sign = Entry(self.label_y_entry, width = 1, validate = "key",
								 validatecommand = (self.register(self.__validate_entry_sign),"%P")) 
		self.y_entry_sign.pack(side = LEFT)
		self.y_entry_1 = Entry(self.label_y_entry, width = 3, validate = "key",
								 validatecommand = (self.register(self.__validate_entry_number_1),"%P")) 
		self.y_entry_1.pack(side = LEFT)
		
		self.point_y = Label(self.label_y_entry, text =".",bg = "#3F3C3C", fg = "white").pack(side = LEFT, padx = 1)
		self.y_entry_2 = Entry(self.label_y_entry, width = 2, validate = "key",
								 validatecommand = (self.register(self.__validate_entry_number_2),"%P")) 
		self.y_entry_2.pack(side = LEFT)

		'''ось-Z'''
		self.label_z_entry = LabelFrame(self.bottom_frame, bg = "#3F3C3C", fg = "white", text = "Ось Z" )
		self.label_z_entry.pack(side = LEFT, padx = 5, pady = 5)
		self.z_entry_sign = Entry(self.label_z_entry, width = 1, validate = "key",
								 validatecommand = (self.register(self.__validate_entry_sign),"%P")) 
		self.z_entry_sign.pack(side = LEFT)
		self.z_entry_1 = Entry(self.label_z_entry, width = 3, validate = "key",
								 validatecommand = (self.register(self.__validate_entry_number_1),"%P")) 
		self.z_entry_1.pack(side = LEFT)
		self.point_z = Label(self.label_z_entry, text =".",bg = "#3F3C3C", fg = "white").pack(side = LEFT, padx = 1)
		self.z_entry_2 = Entry(self.label_z_entry, width = 2, validate = "key",
								 validatecommand = (self.register(self.__validate_entry_number_2),"%P")) 
		self.z_entry_2.pack(side = LEFT)

		'''предупреждение'''
		self.frame_axis_warning = LabelFrame(self.bottom_frame, bg = "#3F3C3C", fg = "white")
		self.frame_axis_warning.pack(side = LEFT)
		img = Img.open("sourse/warning.png")
		img = img.resize((25, 23), Img.ANTIALIAS)
		img = ImageTk.PhotoImage(img)
		warning_img = Label(self.frame_axis_warning, image=img, bg = "#3F3C3C")
		warning_img.image = img
		warning_img.pack(side = LEFT)
		self.label_axis_warning = Label(self.frame_axis_warning , text = "Будьте осторожны при вводе осей\nво избежание коллизий",
										bg = "#3F3C3C", fg = "white", justify = "left", font = "Arial 8")
		self.label_axis_warning.pack(side = LEFT)


		'''Правая панель'''
		self.right_frame = Frame(self, width = 15,height = 10,bg = "#3F3C3C")
		self.right_frame.pack(side = RIGHT, fill = Y)

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
		Button(self.right_frame, text = "Экспорт",
				height = 3, bg = "#344868", fg = "white", command = self.__save_file).pack(side = BOTTOM, fill = X)

		'''Холст'''
		self.canvas_frame = Frame(self)
		self.canvas_frame.pack(side = BOTTOM, expand = 1) 	
		self.canvas = Canvas(self.canvas_frame, width = 640, height = 480, bg = "white")
		self.canvas.pack()


	def __validate_entry_sign(self, input):
		if input == "+":
			return True
		elif input == "-":
			return True
		elif input == "":
			return True
		else:
			return False
				
	def __validate_entry_number_1(self, input):
		try:
			if len(input) > 3:
				return False 
			x = int(input)
			return True
		except ValueError:
			if input == '':
				return True
			else:
				return False

	def __validate_entry_number_2(self, input):
		try:
			if len(input) > 2:
				return False 
			x = int(input)
			return True
		except ValueError:
			if input == '':
				return True
			else:
				return False

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
			self.underpainted = 0	
		else:
			self.__print_status('Подождите','warning')
			self.underpainted = 1

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

	def __show_warning_collision(self):
		msg = "Во избежание коллизий, первый запуск производится в ручном режиме"
		mb.showwarning("Предупреждение", msg)

	def __show_warning_selection_error(self):
		msg = "файл не экспортирован"
		mb.showwarning("Ошибка экспорта", msg)

	def __show_warning_troble_entry_axis(self):
		msg = "неверно указано значение осей"
		mb.showwarning("Ошибка экспорта", msg)

	def __show_warning_underpainted(self):
		msg = "дождитесь отрисовки изображения"
		mb.showwarning("Ошибка экспорта", msg)

	def __read_entry(self,x_entry_sign, x_entry_1, x_entry_2, y_entry_sign, y_entry_1, y_entry_2, z_entry_sign, z_entry_1, z_entry_2):
		try:
			x_sign = "+" if x_entry_sign == " " else x_entry_sign
			y_sign = "+" if y_entry_sign == " " else y_entry_sign
			z_sign = "+" if z_entry_sign == " " else z_entry_sign
			if len(x_entry_1) < 3: raise AxisError(Exception)
			elif len(x_entry_2) < 2: raise AxisError(Exception)
			elif len(y_entry_1) < 3: raise AxisError(Exception)
			elif len(y_entry_2) < 2: raise AxisError(Exception)
			elif len(z_entry_1) < 3: raise AxisError(Exception)
			elif len(z_entry_1) < 2: raise AxisError(Exception)
			else:
				self.x_val = '%s%s.%s' % (x_sign,x_entry_1,x_entry_2)
				self.y_val = '%s%s.%s' % (y_sign,y_entry_1,y_entry_2)
				self.z_val = '%s%s.%s' % (z_sign,z_entry_1,z_entry_2)
		except AxisError:
			self.__print_status("неверное\nзначение осей !","warning")
			self.__show_warning_troble_entry_axis()

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

	def __create_file(self):
		try:
			if self.underpainted == 1: raise UnderpaintedError(Exception)
			self.__read_entry(self.x_entry_sign.get(), self.x_entry_1.get(), self.x_entry_2.get(), self.y_entry_sign.get(), self.y_entry_1.get(), 
								self.y_entry_2.get(), self.z_entry_sign.get(), self.z_entry_1.get(), self.z_entry_2.get())
			self.program_file = create_program(self.contours, float(self.x_val), float(self.y_val), float(self.z_val))
		except UnderpaintedError:
			self.__show_warning_underpainted()

	def __save_file(self):
		try:
			new_file = fd.asksaveasfile(title="Сохранить файл", initialdir = "programs", defaultextension=".prg",
										filetypes=(("Текстовый файл", "*.prg"),))
			if new_file:
				self.__create_file()
				new_file.write(self.program_file)
				new_file.close()
				self.__print_status("Экспортировано","success")
				self.__show_warning_collision()
		except AttributeError:
			self.__print_status("Выберете файл", "warning")
			self.__show_warning_selection_error()

if __name__ == "__main__":
	window = Window()
	window.mainloop()