import cv2 as cv
from Road_map import Roadmap 
import rospy
class GUI:
	def __init__(self):
		pass
	def redraw(self, road_map):
		rospy.loginfo('%s',str("redraw-ALLAH"))
		cv.imwrite("/data/road_map.jpg", road_map.getTrace())
		cv.imshow('road_map.jpg', road_map.getTrace())
		cv.waitKey(0)
