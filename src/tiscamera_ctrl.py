#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse, SetBool, SetBoolResponse
from phobos.srv import SetInt, SetIntResponse
import tiscamera


class tiscamera_ctrl(object):
    def __init__(self):
         # initalise ros node
        rospy.init_node('tiscamera_ctrl')

        # check required parameters are set
        if (rospy.has_param('~Serial') and rospy.has_param('~Width') and rospy.has_param('~Height') and rospy.has_param('~FPS')):
            # get width/height topic names from parameters
            serial = rospy.get_param('~Serial')
            width = rospy.get_param('~Width')
            height = rospy.get_param('~Height')
            fps = rospy.get_param('~FPS')
            self.cam = tiscamera.Camera(
                serial, width, height, fps, False, False)

            # set inital camera properties based on parameters
            if (rospy.has_param('~Exposure_Auto')):
                rospy.loginfo("setting inital exposure auto")
                exposure_auto = rospy.get_param('~Exposure_Auto')
                self.set_property('Exposure Auto', exposure_auto)
            if (rospy.has_param('~Gain_Auto')):
                rospy.loginfo("setting inital gain auto")
                gain_auto = rospy.get_param('~Gain_Auto')
                self.set_property('Gain Auto', gain_auto)
            if (rospy.has_param('~Exposure')):
                rospy.loginfo("setting inital exposure")
                exposure = rospy.get_param('~Exposure')
                self.set_property('Exposure', exposure)
            if (rospy.has_param('~Gain')):
                rospy.loginfo("setting inital gain")
                gain = rospy.get_param('~Gain')
                self.set_property('Gain', gain)

            # initalise ros services
            # create service to trigger displaying of graph
            rospy.Service('tiscam_set_exposure_auto',
                        SetBool, self.set_exposure_auto)
            rospy.Service('tiscam_set_gain_auto', SetBool, self.set_gain_auto)
            rospy.Service('tiscam_set_exposure', SetInt, self.set_exposure)
            rospy.Service('tiscam_set_gain', SetInt, self.set_gain)

        else:
            rospy.logerr("tiscamera_ctrl: Required parameter(s) not set")
            rospy.signal_shutdown("tiscamera_ctrl: Required parameter(s) not set")

    def spin(self):
        # start ros node
        rospy.spin()

    def set_property(self, property_name, data):
        # get current value
        current_value = self.cam.get_property(property_name)
        rospy.loginfo("Current {} value: {}".format(
            property_name, current_value[1]))
        # set property using data value provided
        success = self.cam.set_property(property_name, data)
        # get value after set to check set was successful
        new_value = self.cam.get_property(property_name)
        msg = "New {} value: {}".format(property_name, new_value[1])
        rospy.loginfo(msg)
        return (success, msg)

    def set_exposure_auto(self, req):
        success, msg = self.set_property("Exposure Auto", req.data)
        return SetBoolResponse(success, msg)

    def set_exposure(self, req):
        success, msg = self.set_property("Exposure", req.data)
        return SetIntResponse(success, msg)

    def set_gain_auto(self, req):
        success, msg = self.set_property("Gain Auto", req.data)
        return SetBoolResponse(success, msg)

    def set_gain(self, req):
        success, msg = self.set_property("Gain", req.data)
        return SetIntResponse(success, msg)


if __name__ == '__main__':
    # initalise ros node
    tiscamera_ctl_node = tiscamera_ctrl()
    try:
        # start ros node
        tiscamera_ctl_node.spin()
    except rospy.ROSInterruptException:
        pass
