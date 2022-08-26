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
robot.move("joint", vals=[-45, 44, -61, 16, 78, 81], velocity=35, acceleration=max_accel,
    cnt_val=25,
    linear=False
)
robot.move("joint", vals=[-42, 97, -71.5, 55, 76, 88], velocity=20, acceleration=max_accel,
    cnt_val=0,
    linear=False
)

#Carefully getting under the can tab
robot.move("joint", vals=[-41.964, 94.750, -74.545, 54.499, 77.357, 97.165], velocity=max_vel, acceleration=max_accel,
    cnt_val=0,
    linear=False
)
input("press enter to continue")
robot.move("joint", vals=[-40.933, 94.345, -76.010, 52.209, 78.032, 98.522], velocity=max_vel, acceleration=max_accel,
    cnt_val=0,
    linear=False
)
input("press enter to continue")
robot.move("joint", vals=[-40.933, 94.436, -76.011, 52.208, 78.032, 112.325], velocity=max_vel, acceleration=max_accel,
    cnt_val=0,
    linear=False
)
robot.move("joint", vals=[-41.173, 94.436, -76.011, 52.208, 78.032, 117.725], velocity=15, acceleration=20,
    cnt_val=0,
    linear=False
)
robot.move("joint", vals=[-41.399, 94.436, -76.011, 52.208, 78.032, 134.885], velocity=15, acceleration=20,
    cnt_val=0,
    linear=False
)
#Move to pouring
robot.move("joint", vals=[-49, 95, -76, 52, 78, 111], velocity=20, acceleration=20,
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