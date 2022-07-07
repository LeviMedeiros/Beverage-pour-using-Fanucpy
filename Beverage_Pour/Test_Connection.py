from fanucpy import Robot

robot = Robot(
    robot_model="Fanuc",
    host="192.168.1.100",
    port=18735,
    ee_DO_type="RDO",
    ee_DO_num=7,
)

robot.__version__()
robot.connect()
# get robot state
print(f"Current pose: {robot.get_curpos()}")