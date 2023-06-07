#!/usr/bin/env python3
import rospy
from pid_controller import PID
from magang.srv import pidSet, pidSetResponse

def pid_output(input):
    rospy.loginfo(f"P: {input.p}, I: {input.i}, D: {input.d}")
    pid = PID(input.p, input.i, input.d, input.set)
    return pidSetResponse(pid.calculation())

def main():
    rospy.init_node("PID_Service")
    rospy.loginfo("Service is active")

    service = rospy.Service("Calculate PID", pidSet, pid_output)   
    rospy.spin()

if __name__ == '__main__':
    main()