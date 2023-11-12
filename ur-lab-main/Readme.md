# Universal Robot UR3e Lab

## Requirements
Ubuntu 22.04 with
- Docker engine
- Visual Studio Code (VS Code) with Docker and Dev Container extensions


## Virtual Robot


1. Adjust the permissions to the X server host on your Ubuntu VM:

        xhost +local:root  #for the lazy and reckless

   You need to enter this command after every restart of your  Ubuntu.

1. Start the docker containers inside VS Code with a right-click on `docker-compose.yml` and `Compose Up`. Alternatively, by command line:

        docker compose up

1. In VS code, on the lower left: click on `open a remote window` and select `attach to running container` and select the `ros-ur` container.


1. Inside the container, start the launch file with the terminal

        roslaunch ur_lab virtual_robot.launch
    
    if you want to use the smaller gripper, add the argument `gripper_size:=85` to the command above.


1. You should see the Universal Robot with the joint angles defined in the `kinematics.py`. If the robot is shown in white, relaunch the launch file.

1. Develop your code in `src/ur_lab/src/kinematics.py` The `src/ur_lab` folder is shared between your local machine and the container. Whenever you change something in the code, you can simply relaunch the ROS node. You don't need to build the container or the ROS catkin workspace again.

    
1. If you change your code, stop the ROS node (Ctrl+c / Ctrl+z) and relaunch it with:

        roslaunch ur_lab virtual_robot.launch

   or start the `kinematics.py` in a seperate terminal window
        
        rosrun ur_lab kinematics.py




## Real Robot


It is **mandatory** to get an instruction from your teacher before manipulating the robots!

1. Connect to the wireless network `ur-lab` with the password given by your teacher.

1. Make sure, your network in your VM is set to `bridged` mode.

1. Adjust the permissions to the X server host on your Ubuntu VM:

        xhost +local:root  #for the lazy and reckless

   You need to enter this command after every restart of your  Ubuntu.
 

1. Start the Universal Robot with the teach pendant. 

1. Activate the Universal Robot and set it to *Remote Control* (*Fernsteuerung*).

1. The robot arms are connected to the same network with the following IP addresses:

   - `192.168.1.10` (left robot with 140 mm gripper)
   - `192.168.1.11` (right robot with 85 mm gripper)

1. Start the docker container and connect to it with VS Code.
        
1. Lauch ROS with

        roslaunch ur_lab real_robot.launch

1. To send commands to the robot, you can use the [move_real_robot.py](/src/ur_lab/src/move_real_robot.py) as a template.

        rosrun ur_lab move_real_robot.py

1. You may have to change the IP addresses in the python files `move_real_robot.py` and `ur_primary_client/src/client.py`
and  load the correct gripper with 

        roslaunch ur_lab real_robot.launch gripper_size:=85

Todo (FH):
- add correct dependencies in ros packages
- make it easier to set robot ip / gripper size
