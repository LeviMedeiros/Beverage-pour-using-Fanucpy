from ast import arg
import multiprocessing
from fanucpy import Robot
from multiprocessing import Process
import time

def left_bot_routine(rightset,leftset):
    pour_speed = 5
    pour_accel = 5
    
    #LeftBot.__version__()
    +
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
    LeftBot.move("joint", vals=[33, 68.944, -18.5, 92.4, 91.342, 1], velocity=pour_speed, acceleration=pour_accel,
        cnt_val=0,
        linear=False
    )
    
    print(f"left arm is set to go")
    rightset.wait()
    # LeftBot.move("joint", vals=[45, 35, -32, -22, 35, 46], velocity=pour_speed, acceleration=pour_accel,
    #     cnt_val=0,
    #     linear=False
    # )
    
    #start pouring
    LeftBot.move("joint", vals=[33, 68.944, -18.5, 92.4, 91.342, -58], velocity=pour_speed, acceleration=pour_accel,
        cnt_val=0,
        linear=False
    )
    time.sleep(2)
    leftset.set()
    
    #2nd pouring position
    LeftBot.move("joint", vals=[33, 75.74, -0.4, 91.740, 98.84, -118.8], velocity=pour_speed, acceleration=pour_accel,
        cnt_val=0,
        linear=False
    )    
    time.sleep(4)    
    #3rd pouring position
    LeftBot.move("joint", vals=[33, 52, 0, 90, 90, -180], velocity=pour_speed, acceleration=pour_accel,
        cnt_val=0,
        linear=False
    )
    #shake
    time.sleep(4)
    for i in range(1,3):
        LeftBot.move("joint", vals=[33, 52, 0, 90, 90, -180], velocity=100, acceleration=80,
            cnt_val=0,
            linear=False
        )      
        LeftBot.move("joint", vals=[33, 54, -6, 90, 90, -180], velocity=100, acceleration=80,
            cnt_val=0,
            linear=False
        )
    time.sleep(2)
    LeftBot.move("joint", vals=[33, 54, 35, 90, 90, -35], velocity=100, acceleration=80,
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
    time.sleep(3)
    #RECEIVING THE DRINK
    #Waiting to be ready to pour
    # input("press enter to continue")
    RightBot.move("joint", vals=[-40, 36.726, -37.054, 0.125, -2.634, 0],
    velocity=pour_speed, acceleration=pour_accel, cnt_val=0, linear=False)

    #First receiving position
    rightset.set()
    print(f"right arm is set to go")
    leftset.wait()
    rightset.clear()

    #Second receiving position
    # input("press enter to continue")
    #Delay to avoid collision
    time.sleep(0.5)
    RightBot.move("joint", vals=[-40, 36.429, -36.022, 0.125, 14.261, 0],
    velocity=2, acceleration=2, cnt_val=0, linear=False)        
    
    time.sleep(4)
    #Third receiving position
    # input("press enter to continue")  
    time.sleep(0.1)
    time.sleep(0.5)
    RightBot.move("joint", vals=[-40, 51.341, -27.073, 0.125, 30.484, 0],
    velocity=3, acceleration=3, cnt_val=0, linear=False)        

    
    # input("press enter to continue")
    time.sleep(2)
    time.sleep(4)
    time.sleep(2)
    RightBot.move("joint", vals=[-40, -24.06, -28.94, 0.125, 30.484, 0],
    velocity=10, acceleration=10, cnt_val=0, linear=False)



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