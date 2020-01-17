#!/usr/bin/env python
import rospy
import cv2 as cv
from duckietown_msgs.msg import Twist2DStamped
import Road_map
import GUI

current_milli_time = lambda: int(round(time.time()*1000))

def RobotListener(msg):
	rospy.loginfo('%s',str(msg))
	controller.run_dyty_cycle(current_milli_time(), RobotInfo(msg.v, msg.omega))


class RobotInfo:
	def __init__(self, v, omega):
		self.v = v
		self.omega = omega

class Controller:
	def __init__(self, read_img):
		self.road_map = Roadmap(road_img,x=0,y=0)
		self.gui = GUI()
		self.first = True
	def run_dyty_cycle(self, time_stamp, info):
	 	if self.first == True:
	 		last_step_info = info
	 		last_time_stamp = time_stamp
	 		self. first = False
	 		return
	 	self.road_map.setTrace(time_stamp - last_time_stamp, last_step_info.omega, last_step_info.v, info.v)
	 	last_time_stamp = time_stamp
	 	last_step_info = info
	 	self.gui.redraw(self.road_map)

read_img = cv.imread('graph.jpg',1)
controller = Controller(read_img)

rospy.init_node('self_drive')
rospy.Subscriber('/autobot03/car_cmd_switch_node/cmd', Twist2DStamped, RobotListener)
rospy.spin()