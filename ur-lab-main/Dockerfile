# Build:
#  docker build --rm -t robo/ros-ur .

FROM ros:noetic
LABEL maintainer "Florian Herzog <florian.herzog@hslu.ch>"

SHELL ["/bin/bash","-c"]
ENV CATKIN_WS=/root/catkin_ws
RUN mkdir -p $CATKIN_WS/src

# install universal robot ros repository
RUN apt-get update && apt-get install -y git subversion pip \
     ros-$ROS_DISTRO-universal-robots \
     ros-$ROS_DISTRO-rviz \
     && rm -rf /var/lib/apt/lists/*

# download robotiq gripper visualization
RUN cd ${CATKIN_WS}/src \
     && svn export https://github.com/ros-industrial/robotiq/trunk/robotiq_2f_140_gripper_visualization \
     && svn export https://github.com/ros-industrial/robotiq/trunk/robotiq_2f_85_gripper_visualization 

COPY src ${CATKIN_WS}/src

# Build the catkin workspace
RUN cd ${CATKIN_WS} \
     && apt update -qq \
     && source /opt/ros/${ROS_DISTRO}/setup.bash \
     && rosdep update \
     && rosdep install --from-paths src --ignore-src -y \
     && catkin_make


RUN chmod +x /root/catkin_ws/src/ur_lab/src/move_real_robot.py \
     && chmod +x /root/catkin_ws/src/ur_lab/src/kinematics.py \
     && chmod +x /root/catkin_ws/src/ur_primary_client/src/client.py 

RUN echo 'source /opt/ros/${ROS_DISTRO}/setup.bash' >> /root/.bashrc
RUN echo 'source /root/catkin_ws/devel/setup.bash' >> /root/.bashrc


