
def create_program(contours):
	axis_z = '177'
	program = ''
	number = 0
	for contour in contours:
		for point in contour:
			number += 1
			program += ('''%s p1 = (+%s.00, +%s.00, +%s.00)\n'''%(number, int(point[0][0] / 2 + 100), int(point[0][1] / 2 + 100), axis_z))
			number += 1
			program += ('''%s Mow p1\n'''%(number))
	return program

if __name__  == "__main__":
	from generate_contours import *


	program = create_program(generate_contours('image/test.jpg', minVal=100, maxVal=200))
	print(program)