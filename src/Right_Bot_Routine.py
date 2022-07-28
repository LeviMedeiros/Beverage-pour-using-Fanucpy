from fanucpy import Robot

def right_bot_rountine(routine):
    RightBot = Robot(
        robot_model="Fanuc",
        host="192.168.5.52",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )

    RightBot.__version__()

    RightBot.connect()
    print(f"Connected to RightBot")
    # move in joint space
    # RightBot.move(
    #     "joint",
    #     vals=[90, 0, 0, 0, 0, 0],
    #     velocity=50,
    #     acceleration=50,
    #     cnt_val=0,
    #     linear=False
    # )

    # move in cartesian space
    if routine == 0:
        RightBot.move(
        "joint",
        vals=[90, 0, 0, 0, 0, -31.965],
        velocity=50,
        acceleration=50,
        cnt_val=0,
        linear=False
    )

    if routine == 1:
        RightBot.move(
        "joint",
        vals=[50, 88.298, -89.138, -1.083, 83.753, -31.965],
        velocity=10,
        acceleration=100,
        cnt_val=0,
        linear=False
    )
    # if routine == 1:
    #     RightBot.move(
    #     "pose",
    #     vals=[525.365, 315.096, -402.999, -112, -50.616, -42.644],
    #     velocity=50,
    #     acceleration=50,
    #     cnt_val=0,
    #     linear=False
    #     )

    if routine == 2:
        RightBot.move(
        "joint",
        vals=[32, 88.298, -89.138, -1.083, 83.753, -31.965],
        velocity=10,
        acceleration=10,
        cnt_val=0,
        linear=False
    )

    if routine == 3:
        RightBot.move(
        "joint",
        vals=[32, 99.95, -89.138, -1.083, 83.753, -31.965],
        velocity=100,
        acceleration=100,
        cnt_val=0,
        linear=False
    )

    if routine == 4:
        RightBot.move(
        "pose",
        vals=[393.732, 466.882, -413.886, -100.106, -57.653, -32.519],
        velocity=10,
        acceleration=100,
        cnt_val=0,
        linear=False
    )

    # get robot state
    print(f"Current pose: {RightBot.get_curpos()}")
    print(f"Current joints: {RightBot.get_curjpos()}")
    print(f"Energy consumption: {RightBot.get_ins_power()}")

if __name__ == '__main__':
    right_bot_rountine(1)