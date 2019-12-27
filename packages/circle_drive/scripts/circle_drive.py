#!/usr/bin/env python
import os
import rospy
from duckietown import DTROS
from duckietown_msgs.msg import Twist2DStamped

class MyNode(DTROS):

    def __init__(self, node_name):
        super(MyNode, self).__init__(node_name=node_name)
        self.pub = rospy.Publisher("~car_cmd", Twist2DStamped, queue_size=1)

    def run(self):
        # publish message every 1 second
        rate = rospy.Rate(0.5) # 1Hz
        while not rospy.is_shutdown():
            msg = Twist2DStamped()
            msg.v = 0.0
            msg.omega = 0.5
            rospy.loginfo("Publishing message")
            self.pub.publish(msg)
            rate.sleep()
            msg.omega = 0.0
            rospy.loginfo("Publishing message -")
            self.pub.publish(msg)
            rate.sleep()

if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='circle_drive_node')
    # run node
    node.run()
    # keep spinning
    rospy.spin()
