
def create_program(contours):
	axis_z_down = '183.12'
	axis_z_up = '180.00'
	program = ''
	number_line = 0
	number_contour = 0
	for contour in contours:
		number_contour += 1
		for point in contour:
			number_line += 1
			axis_z = axis_z_down if number_contour / 2 == 1 else axis_z_up
			point_x = '''+%s'''%(int(point[0][1] / 2 + 220)) if int(point[0][1] / 2 + 220) > 0 else '''%s'''%(int(point[0][1] / 2 + 220))
			point_y = '''+%s'''%(int(point[0][0] / 2 - 50)) if int(point[0][0] / 2 - 50) > 0 else '''%s'''%(int(point[0][0] / 2 - 50))
			program += ('''%s p1 = (%s.00,%s.00,+%s)\n'''%(number_line, point_x, point_y, axis_z))
			number_line += 1
			program += ('''%s Mov p1\n'''%(number_line))
	return program

if __name__  == "__main__":
	from generate_contours import *


	program = create_program(generate_contours('image/test.jpg', minVal=100, maxVal=200))
	print(program)