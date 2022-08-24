from fanucpy import Robot

robot = Robot(
    robot_model="Fanuc",
    host="192.168.5.153",
    port=18735,
    ee_DO_type="RDO",
    ee_DO_num=7,
)

robot.__version__()

robot.connect()

max_vel = 10
max_accel = 10
print(f"Beginning Opening Can routine")
#Move to the starting position for opening the can
robot.move("joint", vals=[-45, 44, -61, 16, 78, 81], velocity=max_vel, acceleration=max_accel,
    cnt_val=25,
    linear=False
)
robot.move("joint", vals=[-42, 97, -71.5, 55, 76, 88], velocity=max_vel, acceleration=max_accel,
    cnt_val=0,
    linear=False
)

#Carefully getting under the can tab
robot.move("joint", vals=[-41.322, 94.139, -74.925, 54.349, 77.784, 97.342], velocity=max_vel, acceleration=max_accel,
    cnt_val=0,
    linear=False
)
input("press enter to continue")
robot.move("joint", vals=[-40.629, 93.832, -75.905, 53.488, 78.217, 98.255], velocity=max_vel, acceleration=max_accel,
    cnt_val=0,
    linear=False
)
input("press enter to continue")
robot.move("joint", vals=[-40, 94.525, -76.672, 53.054, 78.613, 98.921], velocity=max_vel, acceleration=max_accel,
    cnt_val=0,
    linear=False
)
robot.move("joint", vals=[-40, 94.525, -76.672, 53.054, 78.613, 110], velocity=15, acceleration=20,
    cnt_val=0,
    linear=False
)
robot.move("joint", vals=[-41.1, 94.793, -76.141, 53.054, 78.613, 125], velocity=15, acceleration=20,
    cnt_val=0,
    linear=False
)
#Quickly drop the can to pop it open
# input("press enter to continue")
# robot.move("joint", vals=[-40.323, 101.418, -75.619, 53.228, 77.982, 98.061], velocity=25, acceleration=50,
#     cnt_val=0,
#     linear=False
# )
# robot.move("joint", vals=[-40.814, 102, -75, 54, 78, 95.5], velocity=50, acceleration=50,
#     cnt_val=0,
#     linear=False
# )
# input("press enter to continue")
#Move to pouring
robot.move("joint", vals=[-49, 95, -87, 54, 78, 95.5], velocity=20, acceleration=20,
    cnt_val=0,
    linear=False
)
# input("press enter to continue") 
robot.move("joint", vals=[-49, 40, -66, 0, 68, 90], velocity=20, acceleration=20,
    cnt_val=50,
    linear=False
)

# input("press enter to continue") 
robot.move("joint", vals=[46, 35, -32, -22, 35, 117.5], velocity=20, acceleration=20,
    cnt_val=0,
    linear=False
)

# open gripper
#robot.gripper(True)

# close gripper
#robot.gripper(False)

# move in cartesian space
#robot.move(
#    "pose",
#    vals=[0.0, -28.0, -35.0, 0.0, -55.0, 0.0],
#    velocity=50,
#    acceleration=50,
#    cnt_val=0,
#    linear=False
#)

# get robot state
# print(f"Current pose: {robot.get_curpos()}")
# print(f"Current joints: {robot.get_curjpos()}")
# print(f"Energy consumption: {robot.get_ins_power()}")