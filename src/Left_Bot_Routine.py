#Import Robot Library
from fanucpy import Robot

def left_bot_routine(routine):
    #LeftBot.__version__()
    LeftBot = Robot(
        robot_model="Fanuc",
        host="192.168.5.153",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )
    LeftBot.connect() 
    print(f"Connected to left")
    for x in range(1,3): 
        if routine==1:
            LeftBot.move(
                "joint",
                vals=[-90, 0, 0, 0, 0, 0],
                velocity=50,
                acceleration=50,
                cnt_val=0,
                linear=False
            )
            print(f"Current pose: {LeftBot.get_curpos()}")
            LeftBot.move(
                "joint",
                vals=[0, 0, 0, 0, 0, 0],
                velocity=50,
                acceleration=50,
                cnt_val=0,
                linear=False
            )
            print(f"Current pose: {LeftBot.get_curpos()}")
        if routine==2:
            LeftBot.move(
                "joint",
                vals=[-90, 0, 0, 0, 0, 0],
                velocity=75,
                acceleration=75,
                cnt_val=0,
                linear=False
            )
            print(f"Current pose: {LeftBot.get_curpos()}")
            LeftBot.move(
                "joint",
                vals=[0, 0, 0, 0, 0, 0],
                velocity=75,
                acceleration=75,
                cnt_val=0,
                linear=False
            )
            print(f"Current pose: {LeftBot.get_curpos()}")
        if routine==3:
            LeftBot.move(
                "joint",
                vals=[-90, 0, 0, 0, 0, 0],
                velocity=100,
                acceleration=100,
                cnt_val=0,
                linear=False
            )
            print(f"Current pose: {LeftBot.get_curpos()}")
            LeftBot.move(
                "joint",
                vals=[0, 0, 0, 0, 0, 0],
                velocity=100,
                acceleration=100,
                cnt_val=0,
                linear=False
            )
            print(f"Current pose: {LeftBot.get_curpos()}")

