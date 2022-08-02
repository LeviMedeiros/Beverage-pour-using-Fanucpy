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

print(f"Beginning Opening Can routine")
robot.move("joint", vals=[-45, 44, -61, 16, 78, 81], velocity=10, acceleration=10,
    cnt_val=25,
    linear=False
)
# input("press enter to continue")
robot.move("joint", vals=[-42, 97, -71.5, 55, 76, 88], velocity=10, acceleration=10,
    cnt_val=0,
    linear=False
)
# input("press enter to continue")
robot.move("joint", vals=[-41.406, 93.404, -74.870, 54.548, 77.785, 98.372], velocity=10, acceleration=10,
    cnt_val=0,
    linear=False
)
# input("press enter to continue")
robot.move("joint", vals=[-40.990, 93.161, -75.437, 54.548, 77.785, 98.371], velocity=10, acceleration=10,
    cnt_val=0,
    linear=False
)
input("press enter to continue")
robot.move("joint", vals=[-40.687, 93.271, -75.882, 54.548, 77.785, 98.371], velocity=10, acceleration=10,
    cnt_val=0,
    linear=False
)

input("press enter to continue")
robot.move("joint", vals=[-40.229, 93.36, -76.365, 54.549, 77.785, 95.971], velocity=10, acceleration=10,
    cnt_val=0,
    linear=False
)

input("press enter to continue")
robot.move("joint", vals=[-40.814, 102, -75, 54, 78, 95.5], velocity=50, acceleration=50,
    cnt_val=0,
    linear=False
)
    # input("press enter to continue")
    #Move to pouring
robot.move("joint", vals=[-49, 95, -87, 54, 78, 95.5], velocity=10, acceleration=10,
    cnt_val=0,
    linear=False
)

# input("press enter to continue") 
robot.move("joint", vals=[-49, 40, -66, 0, 68, 90], velocity=10, acceleration=10,
    cnt_val=50,
    linear=False
)

    # input("press enter to continue") 
robot.move("joint", vals=[46, 35, -32, -22, 35, 117.5], velocity=10, acceleration=10,
    cnt_val=0,
    linear=False
)

# move in joint space


# robot.move("joint", vals=[33, 54, 35, 90, 90, -35], velocity=50, acceleration=80,
#                 cnt_val=0,
#                 linear=False
# )
# input("press enter to continue") 
# robot.move("joint", vals=[11.788, 68.915, -78.836, -28.516, 81.38, 95.896], velocity=10, acceleration=10,
#     cnt_val=0,
#     linear=False
# )
# input("press enter to continue") 
# robot.move("joint", vals=[11.794, 68.324, -78.604, -28.533, 81.174, 96], velocity=10, acceleration=10,
#     cnt_val=0,
#     linear=False
# )

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