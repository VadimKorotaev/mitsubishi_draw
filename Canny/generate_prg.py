
def create_file(contours):
	axis_z = '0'
	file = open('paint.prg', 'w')
	for contur in contours:
		for point in contur:
			file.write ('''
p1 =(+%s.00,+%s.00,+%s.00)
Mov p1'''%(point[0][0],point[0][1],axis_z))
	file.close()

if __name__  == "__main__":
	from generate_contours import *

	contours = generate_contours('/home/vadim/git/mitsubishi_draw/Canny/image/test.jpg', 100, 200)
	create_file(contours)