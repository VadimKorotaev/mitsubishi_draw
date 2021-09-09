
def create_axis_x(point):
	axis_x = '''+%s'''%(int(point / 2 + 220)) if int(point / 2 + 220) > 0 else '''%s'''%(int(point / 2 + 220))
	return axis_x

def create_axis_y(point):
	axis_y = '''+%s'''%(int(point / 2 - 50)) if int(point / 2 - 50) > 0 else '''%s'''%(int(point / 2 - 50))
	return axis_y

def create_program(contours, val_z_entry): 
	axis_z_up = '190.00'
	axis_z_down = '184.86'
	program = ''
	number_line = 0
	for contour in contours:
		number_point = 0
		for point in contour:
			number_point += 1
			if number_point == 1:
				number_line += 1
				axis_x = create_axis_x(point[0][1])
				axis_y = create_axis_y(point[0][0])
				axis_z = axis_z_up
				program += ('''%s p1 = (%s.00,%s.00,+%s)\n'''%(number_line, axis_x, axis_y, axis_z))
				number_line += 1
				program += ('''%s Mov p1\n'''%(number_line))
			elif number_point == 2:
				number_line += 1
				axis_x = create_axis_x(point[0][1])
				axis_y = create_axis_y(point[0][0])
				axis_z = axis_z_up
				program += ('''%s p1 = (%s.00,%s.00,+%s)\n'''%(number_line, axis_x, axis_y, axis_z))
				number_line += 1
				program += ('''%s Mov p1\n'''%(number_line))
				number_line += 1
				axis_x = create_axis_x(point[0][1])
				axis_y = create_axis_y(point[0][0])
				axis_z = axis_z_down
				program += ('''%s p1 = (%s.00,%s.00,+%s)\n'''%(number_line, axis_x, axis_y, axis_z))
				number_line += 1
				program += ('''%s Mov p1\n'''%(number_line))
			else:
				number_line += 1 
				axis_x = create_axis_x(point[0][1])
				axis_y = create_axis_y(point[0][0])
				axis_z = axis_z_down 
				program += ('''%s p1 = (%s.00,%s.00,+%s)\n'''%(number_line, axis_x, axis_y, axis_z))
				number_line += 1
				program += ('''%s Mov p1\n'''%(number_line))
		else:
			number_line += 1 
			axis_x = create_axis_x(point[0][1])
			axis_y = create_axis_y(point[0][0])
			axis_z = axis_z_up 
			program += ('''%s p1 = (%s.00,%s.00,+%s)\n'''%(number_line, axis_x, axis_y, axis_z))
			number_line += 1
			program += ('''%s Mov p1\n'''%(number_line))
	return program

if __name__  == "__main__":
	from generate_contours import *


	program = create_program(generate_contours('image/test.jpg', minVal=100, maxVal=200))
	print(program)