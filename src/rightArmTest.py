from fanucpy import Robot

robot = Robot(
    robot_model="Fanuc",
    host="192.168.5.52",
    port=18735,
    ee_DO_type="RDO",
    ee_DO_num=7,
)

robot.__version__()

robot.connect()

# move in joint space
robot.move(
    "joint",
    vals=[90, 0, 0, 0, 0, 0],
    velocity=50,
    acceleration=50,
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