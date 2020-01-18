import rospy
import numpy
import cv2 as cv
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
		x1, y1 = 250,250
		try:
			alpha_line = (y_line1 - y_line2) / (x_line1 - x_line2)
		except ZeroDivisionError:
			alpha_line = (y_line1 - y_line2)
		distance1 = last_v
		distance2 = v
		if alpha_robot == numpy.pi / 2:
			if alpha_line == numpy.pi / 2:
				cv.line(img, (x1, y1), (x1, y1 + distance1 - distance2), (255, 0, 0), 2)
				y1 = y1 + distance1 - distance2
				distance1 = distance2
			else:
				cv.line(img, (x1, y1), (x1 + distance1 - distance2, y1), (255, 0, 0), 2)
				x1 = x1 + distance1 - distance2
				distance1 = distance2
		else: 
			if distance1 == distance2:
				if alpha_line == numpy.pi / 2:
					cv.line(img, (x1, y1), (x1 + 20, y1), (255, 0, 0), 2)
					x1 = x1 + 20
			else:
				cv.line(img, (x1, y1), (x1, y1 - 20), (255, 0, 0), 2)
				y1 = y1 - 20
		if distance1 > distance2:	
			if alpha_line == numpy.pi / 2:
				distance3 = (distance1-distance2) / sin(alpha_robot)
				x2 = distance3 * cos(alpha_robot)
				y2 = distance3 * sin(alpha1)
				cv.line(img, (x1, y1), (x1 + round(x2), y1 + round(y2)), (255, 0, 0), 2)
				x1 = x1 + round(x2)
				y1 = y1 - round(y2)
				distance1 = distance2
			else:
				distance3 = (distance1-distance2) / sin(alpha_robot)
				x2 = distance3 * sin(alpha_robot)
				y2 = distance3 * cos(alpha_robot)
				cv.line(img, (x1, y1), (x1 + round(x2), y1 - round(y2)), (255, 0, 0), 2)
				x1 = x1 + round(x2)
				y1 = y1 - round(y2)
				distance1 = distance2
		if distance1 < distance2:
			if alpha_line == numpy.pi / 2:
				distance3 = (distance2-distance1) / sin(alpha_robot)
				x2 = distance3 * cos(alpha_robot)
				y2 = distance3 * sin(alpha_robot)
				cv.line(img, (x1, y1), (x1 + round(x2), y1 - round(y2)), (255, 0, 0), 2)
				x1 = x1 + round(x2)
				y1 = y1 - round(y2)
				distance1 = distance2
			else:	
				distance3 = (distance2-distance1) / sin(alpha_robot)
				x2 = distance3 * sin(alpha_robot)
				y2 = distance3 * cos(alpha_robot)
				cv.line(img, (x1, y1), (x1 - round(x2), y1 - round(y2)), (255, 0, 0), 2)
				x1 = x1 - round(x2)
				y1 = y1 - round(y2)
				distance1 = distance2

		#img update



	def getTrace(self):
		rospy.loginfo('%s',str("getTrace-ALLAH"))
		return self.img
