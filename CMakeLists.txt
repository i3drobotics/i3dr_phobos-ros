cmake_minimum_required(VERSION 2.8.3)
project(i3dr_phobos)

find_package(catkin REQUIRED roscpp std_msgs tf rospy message_generation)

include_directories(
    ${catkin_INCLUDE_DIRS}
)

catkin_package(
    CATKIN_DEPENDS
)

link_directories()
add_definitions(-std=c++11)