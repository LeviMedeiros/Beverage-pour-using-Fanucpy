from fanucpy import Robot

def right_bot_routine(routine):
    RightBot = Robot(
        robot_model="Fanuc",
        host="192.168.5.52",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )
    RightBot.__version__()
    RightBot.connect()
    # get robot state
    print(f"Current pose: {RightBot.get_curpos()}")
    print(f"Current joints: {RightBot.get_curjpos()}")
    print(f"Energy consumption: {RightBot.get_ins_power()}")
    # move in joint space
    for x in range(1,3):
        RightBot.move(
            "joint",
            vals=[90, 0, 0, 0, 0, 0],
            velocity=50,
            acceleration=50,
            cnt_val=0,
            linear=False
        )

        # RightBot.move(
        #     "joint",
        #     vals=[45, 0, 90, 0, 0, 0],
        #     velocity=50,
        #     acceleration=50,
        #     cnt_val=0,
        #     linear=False
        # )


        print(f"Current pose: {RightBot.get_curpos()}")
        RightBot.move(
            "joint",
            vals=[0, 0, 0, 0, 0, 0],
            velocity=50,
            acceleration=50,
            cnt_val=0,
            linear=False
        )
        print(f"Current pose: {RightBot.get_curpos()}")

    # move in cartesian space
    #RightBot.move(
    #   "pose",
    #    vals=[0.0, -28.0, -35.0, 0.0, -55.0, 0.0],
    #    velocity=max_speed,
    #    acceleration=max_accel,
    #    cnt_val=0,
    #    linear=False
    #)