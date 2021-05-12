
def create_program(contours):
	axis_z = '0'
	program = ''
	for contur in contours:
		for point in contur:
			program +=  ('''
p1 =(+%s.00,+%s.00,+%s.00)
Mov p1'''%(point[0][0],point[0][1],axis_z))
	return program

if __name__  == "__main__":
	from generate_contours import *


	program = create_program(generate_contours('image/test.jpg', minVal=100, maxVal=200))
	print(program)