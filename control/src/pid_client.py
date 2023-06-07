#!/usr/bin/env python3
import rospy
import pid_controller
from magang.srv import pidSet, pidSetResponse


def pid_input(p, i, d, set):
    rospy.init_node("PID_Client")
    rospy.wait_for_service("PID")
    rospy.loginfo("Client has been started")
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            get_pid = rospy.ServiceProxy("Calculate PID", pidSet)
            response = get_pid(p, i ,d, set)
            rospy.loginfo(f"Output PID = {response.output}")
            rate.sleep()
        except rospy.ServiceException as e:
            print("Service call failed: ", e)

if __name__ == '__main__':
    pid_input(2, 3, 1, 10)