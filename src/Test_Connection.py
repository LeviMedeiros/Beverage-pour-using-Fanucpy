import multiprocessing
from pathlib import PureWindowsPath
from fanucpy import Robot
from multiprocessing import Process

def left_bot_routine():
    
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
    for x in range(1,5): 
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



def right_bot_routine():
    #RightBot.__version__()#What do
    RightBot = Robot(
        robot_model="Fanuc",
        host="192.168.5.52",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )
    RightBot.connect()

    print(f"Connected to right")
    for x in range(1,5):
        RightBot.move(
            "joint",
            vals=[90, 0, 0, 0, 0, 0],
            velocity=50,
            acceleration=50,
            cnt_val=0,
            linear=False
        )
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



if __name__=='__main__':
    print(f"main process has begun")
    max_speed = 100
    max_accel = 100 
    
    p1 = multiprocessing.Process(target = left_bot_routine)
    p2 = multiprocessing.Process(target = right_bot_routine)
    p1.start()
    print(f"started left process")
    p2.start()
    print(f"right process started")