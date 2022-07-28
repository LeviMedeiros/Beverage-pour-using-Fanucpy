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

# move in joint space
robot.move("joint", vals=[13.048, 68.563, -80.078, -30.874, 82.578, 95.335], velocity=10, acceleration=10,
    cnt_val=0,
    linear=False
)
input("press enter to continue") 
robot.move("joint", vals=[11.788, 68.915, -78.836, -28.516, 81.38, 95.896], velocity=10, acceleration=10,
    cnt_val=0,
    linear=False
)
input("press enter to continue") 
robot.move("joint", vals=[11.794, 68.324, -78.604, -28.533, 81.174, 96], velocity=10, acceleration=10,
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
print(f"Current pose: {robot.get_curpos()}")
print(f"Current joints: {robot.get_curjpos()}")
print(f"Energy consumption: {robot.get_ins_power()}")