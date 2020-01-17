#! /usr/bin/env python
import rospy 
import cv2 as cv
import time
from duckietown_msgs.msg import Twist2DStamped

#service client 
#import MSG

##- push to dt-ros-commons/packages/duckietown_msgs/msg/
#Image processing module IPM
#MSG - Command from RobotDriver to IPM
#TURN_FRONT
#TURN_LEFT
#TURN_RIGHT

#RobotState from IPM to RobotDriver 
#State = TURNING/LINE_FOLLOWING/INTERSECTION_DETECTED
#float velocity
#float angle

from enum import Enum
class Command(Enum):
    TURN_FRONT
    TURN_LEFT
    TURN_RIGHT

class RobotState(Enum):
    TURNING
    LINE_FOLLOWING
    INTERSECTION_DETECTED  
    

current_milli_time = lambda: int(round(time.time() * 1000))      

class RobotInfo:
    def __init__(self): 
        self.time_stamp = 0 #measured time

def RobotListener(msg):
        rospy.loginfo('%s', str(msg))
        #save msg info
        #controller.run_dyty_cycle(current_milli_time(), RobotInfo(msg))           


class RobotDriver:

    def start_line_following(self): pass
    def make_turn(self): pass


class Roadmap:
    class Vertex:
        def __init__(self):
            return
    class Edge:
        #start_vertex
        #end_vertex
        #weight (road length) 
        def __init__(self):
            return

    def __init__(self, road_img): 
        self.start, self.fin  = Vertex() 
        parse_map_img(road_img)

    #returns start edge
    def get_start_edge(self):
        pass
    #returns array of vertexes
    def get_vertex_neighbours(self,vertex):
        pass

    def setTrace(self, time, alpha, velocity): pass
    def getTrace(): pass

class GUI:
    def __init__(self, road_img): pass
    def redraw(self, road_map): pass

        
class Controller:
    def __init__(self, road_img):
        self.road_map = Roadmap(road_img)
         #beginning vertex of the current edge.
         #we assume that we always start from the same point of road
        #self.edge = self.road_map.get_start_edge() #Roadmap.Edge - current edge
        self.robot_driver = RobotDriver() 
        self.robot_info = RobotInfo()
        self.gui = GUI()
        self.first = True

    def run_dyty_cycle(self, time_stamp, info):
        if self.first == True:
            last_step_info = info #STATE + COORDS (V, a)
            last_time_stamp =  time_stamp
            self.first = False
            return
        #MONITORING
        self.road_map.setTrace(time_stamp - last_time_stamp, 
                                   last_step_info.alpha, last_step_info.velocity)
        last_time_stamp =  time_stamp
        last_step_info = info
        self.gui.redraw()
            

            #STEERING
            #while(True):
            #self.robot_driver.start_line_following() #sends msg to CameraImgParserNode
            #if ( self.robot_driver.vertex_detected() == True ):
            #     neighbrs = self.road_map.get_vertex_neighbours(self.edge.fin) 
            #     #array of heqghbours - edges
            #     # random choice of next vertex              
            #     self.edge = neighbrs[i]
            #     robot_driver.turn(self.edge) #FOR FUTURE DISCUSSION, wait until turn        
            #     while (robot_driver.turning()):


#road_img = cv.imread('graph.jpg', 1)
#controller = Controller(road_img)
rospy.init_node('self_drive')
rospy.Subscriber('/autobot03/car_cmd_switch_node/cmd', Twist2DStamped, RobotListener)
rospy.spin()
    #        
    #def __init__(self, listnr): 
    #    self.listener = listnr
    #    rospy.init_node('RobotDriver')
    #    rospy.Subscriber('!!!!', Msg, RobotListener)
    #    self.start = false


    #def get_time_stamp(self): return self.time_stamp
    #def get_robot_info(): pass
        #return RobotInfo
