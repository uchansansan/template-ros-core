import cv2 as cv
from Road_map import Roadmap 

class GUI:
	def __init__(self):
		pass
	def redraw(self, road_map):
		cv.imwrite("road_map.png", road_map.getTrace())