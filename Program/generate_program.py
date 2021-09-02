
def create_program(contours):
	axis_z_down = '183.12'
	axis_z_up = '180.00'
	program = ''
	number = 0
	for contour in contours:
		for point in contour:
			number += 1
			point_x = '''+%s'''%(int(point[0][0] / 2 + 200)) if int(point[0][0] / 2 + 200) > 0 else '''%s'''%(int(point[0][0] / 2 + 200))
			point_y = '''+%s'''%(int(point[0][1] / 2 - 50)) if int(point[0][1] / 2 - 50) > 0 else '''%s'''%(int(point[0][1] / 2 - 50))
			program += ('''%s p1 = (%s.00,%s.00,+%s)\n'''%(number, point_x, point_y, axis_z_down))
			number += 1
			program += ('''%s Mov p1\n'''%(number))
			number += 1
			point_x = '''+%s'''%(int(point[0][0] / 2 + 200)) if int(point[0][0] / 2 + 200) > 0 else '''%s'''%(int(point[0][0] / 2 + 200))
			point_y = '''+%s'''%(int(point[0][1] / 2 - 50)) if int(point[0][1] / 2 - 50) > 0 else '''%s'''%(int(point[0][1] / 2 - 50))
			program += ('''%s p1 = (%s.00,%s.00,+%s)\n'''%(number, point_x, point_y, axis_z_up))
			number += 1
			program += ('''%s Mov p1\n'''%(number))
	return program

if __name__  == "__main__":
	from generate_contours import *


	program = create_program(generate_contours('image/test.jpg', minVal=100, maxVal=200))
	print(program)