from Beverage_Pour.First_test import RightBot

def right_bot_routine():
    # get robot state
    print(f"Current pose: {RightBot.get_curpos()}")
    print(f"Current joints: {RightBot.get_curjpos()}")
    print(f"Energy consumption: {RightBot.get_ins_power()}")
    # move in joint space
    RightBot.move(
        "joint",
        vals=[19.0, 66.0, -33.0, 18.0, -30.0, -33.0],
        velocity=100,
        acceleration=100,
        cnt_val=0,
        linear=False
    )
    # move in cartesian space
    RightBot.move(
        "pose",
        vals=[0.0, -28.0, -35.0, 0.0, -55.0, 0.0],
        velocity=50,
        acceleration=50,
        cnt_val=0,
        linear=False
    )