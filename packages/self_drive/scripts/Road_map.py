import rospy
import numpy
import cv2 as cv
import math
class Roadmap():
	def  __init__(self, read_img, x, y):
		#parse_map_img(read_img)
		self.img = read_img #cv.imread('43225aba74ba46ba733f83ec5084e73d.jpg')
		self.robot_x = x
		self.robot_y = y

	def getTangent(self):
		return 0,1,0,3
	def setTrace(self, time, alpha_robot, last_v, v):
		rospy.loginfo('%s',str("setTrace-ALLAH"))
		img = self.img
		x_line1,y_line1,x_line2,y_line2 = self.getTangent()
		x1= int(250)
		y1= int(250)
		try:
			alpha_line = int(math.ceil((y_line1 - y_line2) / (x_line1 - x_line2)))
		except ZeroDivisionError:
			alpha_line = int(math.ceil((y_line1 - y_line2)))
		distance1 = int(math.ceil(last_v))
		distance2 = int(math.ceil(v))
		if alpha_robot == numpy.pi / 2:
			if (abs(alpha_line) == numpy.pi) and (abs(alpha_line) == 0):
				cv.line(img, ( int(math.ceil(x1)), int(math.ceil(y1)) ), ( int(math.ceil(x1)), int(math.ceil(y1 + distance1 - distance2)) ), (255, 0, 0), 2)
				
				y1 = int(math.ceil(y1)) + distance1 - distance2
				
				distance1 = int(math.ceil(distance2))
			else:
				cv.line(img, (int(math.ceil(x1)), int(math.ceil(y1))), (int(math.ceil(x1 + distance1 - distance2), int(math.ceil(y1)))), (255, 0, 0), 2)
				
				x1= x1 + distance1 - distance2 
				
				distance1 = int(math.ceil(distance2))
		else: 
			if distance1 == distance2:
				if (abs(alpha_line) == numpy.pi) and (abs(alpha_line) == 0):
					cv.line(img, (x1, y1), (x1 + 20, y1), (255, 0, 0), 2)
					x1 = int(math.ceil(x1 + 20))
			else:
				cv.line(img, ( int(math.ceil(x1)), int(math.ceil(y1)) ), ( int(math.ceil(x1)), int(math.ceil(y1 - 20)) ), (255, 0, 0), 2, 8)
				y1 = int(math.ceil(y1 - 20))
		if (distance1 > distance2) and (abs(alpha_robot) != numpy.pi) and (abs(alpha_robot) != 0):	
			if alpha_line == numpy.pi / 2:
				distance3 = int(math.ceil( (distance1-distance2) / math.sin(alpha_robot) ))
				x2 = int(math.ceil(distance3 * math.cos(alpha_robot)))
				y2 = int(math.ceil(distance3 * math.sin(alpha1)))
				cv.line(img, (int(math.ceil(x1)), int(math.ceil(y1))), (int(math.ceil(x1 + round(x2))), int(math.ceil(y1 + round(y2)))), (255, 0, 0), 2)
				x1 = int(math.ceil(x1 + round(x2)))
				y1 = int(math.ceil(y1 - round(y2)))
				distance1 = int(math.ceil(distance2))
			else:
				distance3 = int(math.ceil( (distance1-distance2) / math.sin(alpha_robot) ) )
				x2 = int(math.ceil(distance3 * math.sin(alpha_robot)))
				y2 = int(math.ceil(distance3 * math.cos(alpha_robot)))
				cv.line(img, (int(math.ceil(x1)), int(math.ceil(y1))), (int(math.ceil(x1 + round(x2))), int(math.ceil(y1 - round(y2)))), (255, 0, 0), 2)
				x1 = int(math.ceil(x1 + round(x2)))
				y1 = int(math.ceil(y1 - round(y2)))
				distance1 = int(math.ceil(distance2))
		if (distance1 < distance2) and (abs(alpha_robot) != numpy.pi) and (abs(alpha_robot) != 0):
			if (alpha_line == numpy.pi) and (alpha_robot != 0):
				distance3 = int(math.ceil( (distance2-distance1) / math.sin(alpha_robot) ))
				x2 = int(math.ceil(distance3 * math.cos(alpha_robot)))
				y2 = int(math.ceil(distance3 * math.sin(alpha_robot)))
				cv.line(img, (int(math.ceil(x1)), int(math.ceil(y1))), ( int(math.ceil(x1 + round(x2))), int(math.ceil(y1 - round(y2))) ), (255, 0, 0), 2)
				x1 = int(math.ceil(x1 + round(x2)))
				y1 = int(math.ceil(y1 - round(y2)))
				distance1 = int(math.ceil(distance2))
			elif (abs(alpha_robot) != numpy.pi) and (abs(alpha_robot) != 0):	
				distance3 = int(math.ceil((distance2-distance1) / math.sin(alpha_robot)))
				x2 = int(math.ceil(distance3 * math.sin(alpha_robot)))
				y2 = int(math.ceil(distance3 * math.cos(alpha_robot)))
				cv.line(img, ( int(math.ceil(x1)), int(math.ceil(y1)) ), ( int(math.ceil(x1 - round(x2))), int(math.ceil(y1 - round(y2) )) ), (255, 0, 0), 2)
				x1 = int(math.ceil(x1 - round(x2)))
				y1 = int(math.ceil(y1 - round(y2)))
				distance1 = int(math.ceil(distance2))

		#img update



	def getTrace(self):
		rospy.loginfo('%s',str("getTrace-ALLAH"))
		return self.img
