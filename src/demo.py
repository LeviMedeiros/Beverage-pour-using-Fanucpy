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

max_vel=5
max_accel=5
robot.move(
    "joint",
    vals=[-17.6, 65.7, -40.194, -12.6, 58.787, 99.667],
    velocity=10,
    acceleration=10,
    cnt_val=0,
    linear=False
)
input("yeet")
robot.move(
    "joint",
    vals=[-17.773, 77.962, -44.535, -11.903, 63, 98.475],
    velocity=max_vel,
    acceleration=max_accel,
    cnt_val=0,
    linear=False
)
input("yeet")
robot.move(
    "joint",
    vals=[-16.812, 54.865, -36.146, -14.094, 54.99, 101.505],
    velocity=max_vel,
    acceleration=max_accel,
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