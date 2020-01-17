#!/usr/bin/env python
import rospy
from duckietown_msgs.msg import Twist2DStamped
def RobotListener(msg):
	rospy.loginfo('%s',str(msg))
rospy.init_node('self_drive')
rospy.Subscriber('/autobot03/car_cmd_switch_node/cmd', Twist2DStamped, RobotListener)
rospy.spin()