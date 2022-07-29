from fanucpy import Robot

def right_bot_rountine(routine):
    max_vel = 10
    max_accel = 10

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
        vals=[90, 0, 0, 0, 0, 0],
        velocity=max_vel,
        acceleration=max_accel,
        cnt_val=0,
        linear=False
    )

    if routine == 1:
    #     RightBot.move(
    #     "joint",
    #     vals=[50, 88.298, -89.138, -1.083, 83.753, -31.965],
    #     velocity=max_vel,
    #     acceleration=max_accel,
    #     cnt_val=0,
    #     linear=False
    # )

        RightBot.move("joint", vals=[-37.623, 53.923, -19.32, 0, 28.34, -43.638],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        RightBot.move("joint", vals=[-37.836, 48.825, -17.922, 0, 28.34, -14.931],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        RightBot.move("joint", vals=[-43.928, 45, -17.924, 0, 17, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        RightBot.move("joint", vals=[-17, 62, -29.5, -1.5, 28.5, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        RightBot.move("joint", vals=[29, 62, -25.5, -1.5, 25, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        RightBot.move("joint", vals=[35.046, 67.638, -18.708, -1.619, 18.898, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        RightBot.move("joint", vals=[35.847, 72.399, -20.837, -1.619, 20.848, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    # get robot state
    print(f"Current pose: {RightBot.get_curpos()}")
    print(f"Current joints: {RightBot.get_curjpos()}")
    print(f"Energy consumption: {RightBot.get_ins_power()}")

if __name__ == '__main__':
    right_bot_rountine(2)