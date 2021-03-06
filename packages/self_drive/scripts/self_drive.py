#!/usr/bin/env python
import rospy
import time
import cv2 as cv
from duckietown_msgs.msg import Twist2DStamped
from Road_map import *
from GUI import *
import threading 

current_milli_time = lambda: int(round(time.time()*1000))

def RobotListener(msg):
	global controller 
	rospy.loginfo('MESSAGE %s',str(msg))
	#rospy.loginfo('MESSAGE %s',str('ALLLAHAHASKLHLADHALDHLKA'))
	controller.run_dyty_cycle(current_milli_time(), RobotInfo(msg.v, msg.omega))


class RobotInfo:
	def __init__(self, v, omega):
		self.v = v
		self.omega = omega

class Controller:
	def __init__(self, read_img):
		rospy.loginfo('%s',str("ALLAH"))
		self.road_map = Roadmap(read_img,x=0,y=0)
		self.gui = GUI()
		self.first = True
		self.last_step_info = RobotInfo(0,0)
		self.last_time_stamp = 0
		self.mutex = threading.Lock()
		rospy.init_node('self_drive')
		self.listener = rospy.Subscriber('/autobot03/car_cmd_switch_node/cmd', Twist2DStamped, RobotListener)

	def run_dyty_cycle(self, time_stamp, info):
		rospy.loginfo('%s',str("dyty_cycle"))
	 	if self.first == True:
	 		self.last_step_info = info
	 		self.last_time_stamp = time_stamp
	 		self.first = False
	 		return
	 	self.road_map.setTrace(time_stamp - self.last_time_stamp, self.last_step_info.omega, self.last_step_info.v, info.v)
	 	self.last_time_stamp = time_stamp
	 	self.last_step_info = info
		self.mutex.acquire()
	 	self.gui.redraw(self.road_map)
		self.mutex.release()



read_img = cv.imread('graph.jpg',1)
controller = Controller(read_img)

rospy.spin()
