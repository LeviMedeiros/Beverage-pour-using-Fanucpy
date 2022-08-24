from ast import arg
import multiprocessing
from fanucpy import Robot
from multiprocessing import Process
import time

def left_bot_routine(rightset,leftset):
    pour_speed = 5
    pour_accel = 5
    
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
    pour_speed = 5
    pour_accel = 5
    # time.sleep(5)
    #Pour half the can out for standard can
    print(f"Waiting for cup to pour into")
    #move to initial pour position
    LeftBot.move("joint", vals=[33, 68.944, -18.5, 92.4, 91.342, 1], velocity=10, acceleration=10,
        cnt_val=0,
        linear=False
    )
    
    print(f"left arm is set to go")
    rightset.wait()
    
    #start pouring
    LeftBot.move("joint", vals=[33, 68.944, -18.5, 92.4, 91.342, -58], velocity=10, acceleration=10,
        cnt_val=0,
        linear=False
    )
    #time.sleep(2)
    leftset.set()
    
    #2nd pouring position
    LeftBot.move("joint", vals=[33, 75.74, -0.4, 91.740, 98.84, -118.8], velocity=4, acceleration=4,
        cnt_val=0,
        linear=True
    )    
    time.sleep(2)    #Delay to let liquid flow
    #3rd pouring position
    LeftBot.move("joint", vals=[33, 52, 0, 90, 90, -180], velocity=7, acceleration=7,
        cnt_val=0,
        linear=False
    )
    time.sleep(4)  #Delay to let liquid flow
    for i in range(1,3): #shake
        LeftBot.move("joint", vals=[33, 52, 0, 90, 90, -180], velocity=100, acceleration=80,
            cnt_val=0,
            linear=False
        )      
        LeftBot.move("joint", vals=[33, 54, -6, 90, 90, -180], velocity=100, acceleration=80,
            cnt_val=0,
            linear=False
        )
    time.sleep(2) #Delay to let any last drops fall out

    #Leave pouring safely
    LeftBot.move("joint", vals=[33, 54, 35, 90, 90, -35], velocity=100, acceleration=80,
            cnt_val=0,
            linear=False
    )



def right_bot_routine(rightset,leftset):
    #RightBot.__version__()#What do
    
    RightBot = Robot(
        robot_model="Fanuc",
        host="192.168.5.52",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )
    RightBot.connect()
    
    RightBot.move("joint", vals=[-40, 36.726, -60, 0.125, -2.634, 0],
    velocity=4, acceleration=4, cnt_val=0, linear=False)

    RightBot.move("joint", vals=[-40, 36.726, -37.054, 0.125, -2.634, 0],
    velocity=4, acceleration=4, cnt_val=0, linear=False)

    #First receiving position
    rightset.set()
    print(f"right arm is set to go")
    leftset.wait()
    rightset.clear()

    #Second receiving position
    time.sleep(7) #Delay to avoid collision
    RightBot.move("joint", vals=[-40, 36.429, -36.022, 0.125, 4, 0],
    velocity=1, acceleration=1, cnt_val=0, linear=False)     
    time.sleep(7)   
    RightBot.move("joint", vals=[-40, 36.429, -36.022, 0.125, 14.261, 0],
    velocity=1, acceleration=1, cnt_val=0, linear=False)      
    #D
    time.sleep(4)
    time.sleep(0.1)
    time.sleep(1.5)
    RightBot.move("joint", vals=[-40, 51.341, -27.073, 0.125, 30.484, 0],
    velocity=3, acceleration=3, cnt_val=0, linear=False)        

    time.sleep(2) #delay to wait for arm to reach position
    time.sleep(4) #delay while pouring
    time.sleep(2) #delay to avoid interference
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