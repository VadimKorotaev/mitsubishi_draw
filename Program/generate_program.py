
def create_axis_x(point, val_x_entry):
	axis_x = float(point / 3) + float(val_x_entry)
	axis_x = '+%s' % ('{:.2f}'.format(axis_x)) if axis_x >= 0 else '%s' % ('{:.2f}'.format(axis_x))
	return axis_x

def create_axis_y(point, val_y_entry):
	axis_y = float(point / 3) + float(val_y_entry)
	axis_y = '+%s' % ('{:.2f}'.format(axis_y)) if axis_y >= 0 else '%s' % ('{:.2f}'.format(axis_y))
	return axis_y

def create_program(contours, val_x_entry, val_y_entry, val_z_entry): 
	axis_z_up = float(val_z_entry) + 5 
	axis_z_down = float(val_z_entry) 
	axis_z_up = '+%s' % ('{:.2f}'.format(axis_z_up)) if axis_z_up >= 0 else '%s' % ('{:.2f}'.format(axis_z_up))
	axis_z_down = '+%s' % ('{:.2f}'.format(axis_z_down)) if axis_z_down >= 0 else '%s' % ('{:.2f}'.format(axis_z_down))
	program = ''
	number_line = 0
	print(contours)
	for contour in contours:
		number_point = 0
		for point in contour:
			number_point += 1
			if len(contour) - number_point == 0:
				number_line += 1
				axis_x = create_axis_x(point[0][1], val_x_entry)
				axis_y = create_axis_y(point[0][0], val_y_entry)
				axis_z = axis_z_up
				program += ('''%s p1 = (%s,%s,%s)\n'''%(number_line, axis_x, axis_y, axis_z))
				number_line += 1
				program += ('''%s Mvs p1\n'''%(number_line))
				number_line += 1
				axis_x = create_axis_x(point[0][1], val_x_entry)
				axis_y = create_axis_y(point[0][0], val_y_entry)
				axis_z = axis_z_down
				program += ('''%s p1 = (%s,%s,%s)\n'''%(number_line, axis_x, axis_y, axis_z))
				number_line += 1
				program += ('''%s Mvs p1\n'''%(number_line))
			elif len(contour) - number_point == len(contour)-1:
				number_line += 1
				axis_x = create_axis_x(point[0][1], val_x_entry)
				axis_y = create_axis_y(point[0][0], val_y_entry)
				axis_z = axis_z_down
				program += ('''%s p1 = (%s,%s,%s)\n'''%(number_line, axis_x, axis_y, axis_z))
				number_line += 1
				program += ('''%s Mvs p1\n'''%(number_line))
				number_line += 1
				axis_x = create_axis_x(point[0][1], val_x_entry)
				axis_y = create_axis_y(point[0][0], val_y_entry)
				axis_z = axis_z_up
				program += ('''%s p1 = (%s,%s,%s)\n'''%(number_line, axis_x, axis_y, axis_z))
				number_line += 1
				program += ('''%s Mvs p1\n'''%(number_line))
			else:
				number_line += 1 
				axis_x = create_axis_x(point[0][1], val_x_entry)
				axis_y = create_axis_y(point[0][0], val_y_entry)
				axis_z = axis_z_down 
				program += ('''%s p1 = (%s,%s,%s)\n'''%(number_line, axis_x, axis_y, axis_z))
				number_line += 1
				program += ('''%s Mvs p1\n'''%(number_line))

	return program

if __name__  == "__main__":
	from generate_contours import *


	program = create_program(generate_contours('image/test.jpg', minVal=100, maxVal=200))
	print(program)