from ast import arg
import multiprocessing
from fanucpy_low_latency import Robot
from multiprocessing import Process
import time

def left_bot_routine(rightset,leftset):    
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
    for i in range(1,3):
        LeftBot.move("joint", vals=[0,0,0,0,0,0], velocity=100, acceleration=80,
            cnt_val=0,
            linear=False
        )      
        LeftBot.move("joint", vals=[90,0,0,0,0,0], velocity=100, acceleration=80,
            cnt_val=0,
            linear=False
        )



def right_bot_routine(rightset,leftset):
    #RightBot.__version__()#What do
    pour_speed = 5
    pour_accel = 5
    
    RightBot = Robot(
        robot_model="Fanuc",
        host="192.168.5.52",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )
    RightBot.connect()
    print(f"Connected to right")
    for i in range(1,3):
        RightBot.move("joint", vals=[0,0,0,0,0,0], velocity=100, acceleration=80,
            cnt_val=0,
            linear=False
        )      
        RightBot.move("joint", vals=[90,0,0,0,0,0], velocity=100, acceleration=80,
            cnt_val=0,
            linear=False
        )


if __name__=='__main__':
    print(f"main process has begun")
    max_speed = 100
    pour_accel = 100

    rightset = multiprocessing.Event()
    leftset = multiprocessing.Event()
    
    p1 = multiprocessing.Process(target = left_bot_routine,args=(rightset,leftset))
    p2 = multiprocessing.Process(target = right_bot_routine,args=(rightset,leftset))
    p1.start()
    print(f"started left process")
    p2.start()
    print(f"right process started")