import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/Drone_Sim/ros_ws/install/px4_microxrce_nav'
