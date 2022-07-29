from ast import arg
import multiprocessing
from fanucpy import Robot
from multiprocessing import Process
import time

def left_bot_routine(rightset,leftset):
    max_vel = 5
    max_accel = 5
    
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

    time.sleep(5)
    #Pour half the can out for standard can
    print(f"Waiting for cup to pour into")
    #move to initial pour position
    LeftBot.move("joint", vals=[33.584, 68.944, -18.5, 92.4, 91.342, 1], velocity=max_vel, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    
    print(f"left arm is set to go")
    rightset.wait()
    # LeftBot.move("joint", vals=[45, 35, -32, -22, 35, 46], velocity=max_vel, acceleration=max_accel,
    #     cnt_val=0,
    #     linear=False
    # )
    
    #start pouring
    LeftBot.move("joint", vals=[33.584, 68.944, -18.5, 92.4, 91.342, -58], velocity=max_vel, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    time.sleep(2)
    leftset.set()
    #2nd pouring position
    LeftBot.move("joint", vals=[33.658, 75.74, -0.4, 91.740, 98.84, -118.8], velocity=max_vel, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )        
    #3rd pouring position
    LeftBot.move("joint", vals=[33, 52, 0, 90, 90, -180], velocity=max_vel, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    #shake
    for i in range(1,3):
        LeftBot.move("joint", vals=[33, 52, 0, 90, 90, -180], velocity=100, acceleration=100,
            cnt_val=0,
            linear=False
        )      
        LeftBot.move("joint", vals=[33, 54, -6, 90, 90, -180], velocity=100, acceleration=100,
            cnt_val=0,
            linear=False
        )



def right_bot_routine(rightset,leftset):
    #RightBot.__version__()#What do
    max_vel = 5
    max_accel = 5
    
    RightBot = Robot(
        robot_model="Fanuc",
        host="192.168.5.52",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )
    RightBot.connect()
    time.sleep(3)
    #RECEIVING THE DRINK
    # input("press enter to continue")
    RightBot.move("joint", vals=[-40.693, 36.726, -37.054, 0.125, -2.634, 0],
    velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    #Waiting to be ready to pour
    rightset.set()
    print(f"right arm is set to go")
    leftset.wait()
    rightset.clear()

    #First receiving position
    # input("press enter to continue")
    RightBot.move("joint", vals=[-40.693, 36.429, -36.022, 0.125, 14.261, 0],
    velocity=10, acceleration=10, cnt_val=0, linear=False)        

    #Second receiving position
    # input("press enter to continue")
    RightBot.move("joint", vals=[-40.693, 49.2, -28.94, 0.125, 30.484, 0],
    velocity=1, acceleration=1, cnt_val=0, linear=False)        

    #Third receiving position
    # input("press enter to continue")
    RightBot.move("joint", vals=[-40.693, -24.06, -28.94, 0.125, 30.484, 0],
    velocity=10, acceleration=10, cnt_val=0, linear=False)



if __name__=='__main__':
    print(f"main process has begun")
    max_speed = 100
    max_accel = 100

    rightset = multiprocessing.Event()
    leftset = multiprocessing.Event()
    
    p1 = multiprocessing.Process(target = left_bot_routine,args=(rightset,leftset))
    p2 = multiprocessing.Process(target = right_bot_routine,args=(rightset,leftset))
    p1.start()
    print(f"started left process")
    p2.start()
    print(f"right process started")