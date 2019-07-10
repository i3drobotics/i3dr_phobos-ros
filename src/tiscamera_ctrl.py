#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse, SetBool, SetBoolResponse
from i3dr_phobos.srv import SetInt, SetIntResponse
import tiscamera

class tiscamera_ctrl(object):
    def __init__(self):
         # initalise ros node
        rospy.init_node('tiscamera_ctrl')

        # check required parameters are set
        if (rospy.has_param('~Serial') and rospy.has_param('~Width') and rospy.has_param('~Height') and rospy.has_param('~FPS')):
            # get width/height topic names from parameters
            self.serial = rospy.get_param('~Serial')
            self.width = rospy.get_param('~Width')
            self.height = rospy.get_param('~Height')
            self.fps = rospy.get_param('~FPS')
            self.cam = tiscamera.Camera(
                self.serial, self.width, self.height, self.fps, False, False)

            # set inital camera properties based on parameters
            # initalise rosservice for each camera property given in parameters
            if (rospy.has_param('~Exposure_Auto')):
                rospy.loginfo("setting inital exposure auto")
                exposure_auto = rospy.get_param('~Exposure_Auto')
                self.set_property('Exposure Auto', exposure_auto)
                rospy.Service('tiscam_set_exposure_auto',
                              SetBool, self.set_exposure_auto)
            if (rospy.has_param('~Gain_Auto')):
                rospy.loginfo("setting inital gain auto")
                gain_auto = rospy.get_param('~Gain_Auto')
                self.set_property('Gain Auto', gain_auto)
                rospy.Service('tiscam_set_gain_auto',
                              SetBool, self.set_gain_auto)
            if (rospy.has_param('~Exposure')):
                rospy.loginfo("setting inital exposure")
                exposure = rospy.get_param('~Exposure')
                self.set_property('Exposure', exposure)
                rospy.Service('tiscam_set_exposure', SetInt, self.set_exposure)
            if (rospy.has_param('~Gain')):
                rospy.loginfo("setting inital gain")
                gain = rospy.get_param('~Gain')
                self.set_property('Gain', gain)
                rospy.Service('tiscam_set_gain', SetInt, self.set_gain)

        else:
            # required parameters not set
            rospy.logerr("tiscamera_ctrl: Required parameter(s) not set")
            rospy.signal_shutdown(
                "tiscamera_ctrl: Required parameter(s) not set")

    def spin(self):
        # start ros node
        rospy.spin()

    def set_property(self, property_name, data):
        # set camera property using data

        # initalise return values
        success = False
        msg = ""
        try:
            # get current value
            current_value = self.cam.get_property(property_name)
            rospy.loginfo("Current {} value: {}".format(
                property_name, current_value[1]))
            # set property using data value provided
            self.cam.set_property(property_name, data)
            # get value after set to check set was successful
            new_value = self.cam.get_property(property_name)
            msg = "New {} value: {}".format(property_name, new_value[1])
            rospy.loginfo(msg)
        except:
            # failed to set property
            # usually due to missing property in tiscamera
            # check property exists using tcam-ctrl -p <SERIAL>
            success = False
            msg = "[ERROR] Unable to set tiscamera property"
            rospy.logerr(msg)
        return (success, msg)

    def set_exposure_auto(self, req):
        # callback request to set exposure auto
        success, msg = self.set_property("Exposure Auto", req.data)
        return SetBoolResponse(success, msg)

    def set_exposure(self, req):
        # callback request to set exposure
        success, msg = self.set_property("Exposure", req.data)
        return SetIntResponse(success, msg)

    def set_gain_auto(self, req):
        # callback request to set gain auto
        success, msg = self.set_property("Gain Auto", req.data)
        return SetBoolResponse(success, msg)

    def set_gain(self, req):
        # callback request to set gain
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
