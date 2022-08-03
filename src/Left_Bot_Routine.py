#Import Robot Library
from fanucpy import Robot
import time

def left_bot_routine(routine,leftset,rightset):
    max_vel = 10
    max_accel = 10
    
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
    
    #ROUTINE TO ZERO ARM IF NECESSARY
    if routine == 0: #Zero Arm
        LeftBot.move(
        "joint",
        vals=[0, 0, 0, 0, 0, 90],
        velocity=max_vel,
        acceleration=max_accel,
        cnt_val=0,
        linear=False
    )

    #CAN PICK UP ROUTINES
    if routine==1: #Pick up left can
        #Pick up can
        print(f"Picking up left can")
        LeftBot.move(
            "joint",
            vals=[-18, 71, -41.5, -12, 60, 99],
            velocity=max_vel,
            acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        LeftBot.move(
            "joint",
            vals=[-18, 83, -42, -12, 60.5, 99],
            velocity=max_vel,
            acceleration=max_accel,
            cnt_val=0,
            linear=False
        )

        LeftBot.move(
            "joint",
            vals=[-18, 63, -45, -12.5, 55.5, 100],
            velocity=max_vel,
            acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        print(f"Can picked up")

    if routine==2: #Pick up center can
        print(f"Picking up center can")
        LeftBot.move("joint", vals=[-23.306, 70.171, -45.003, -11.646, 60.79, 98.604],
            velocity=50, acceleration=50, cnt_val=0, linear=False)
       
        LeftBot.move("joint", vals=[-23.306, 79.978, -45.005, -11.646, 60.79, 98.603],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        LeftBot.move("joint", vals=[-23.306, 40, -45.017, -11.646, 60.79, 98.603],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    
    if routine==3: #Pick up right can
        print(f"Picking up right can")
        print(f"Current pose: {LeftBot.get_curpos()}")
        LeftBot.move("joint", vals=[-28.901, 64.667, -45.005, -11.646, 60.79, 98.604],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        LeftBot.move("joint", vals=[-28.901, 75.382, -45.005, -11.646, 60.79, 98.604],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        LeftBot.move("joint", vals=[-28.901, 40, -45.005, -11.646, 60.79, 98.604],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)


        print(f"Current pose: {LeftBot.get_curpos()}")
    
    #OPENING ROUTINE
    if routine==1 or routine==2 or routine==3: #Open Can
        print(f"Beginning Opening Can routine")
        #Move to the starting position for opening the can
        LeftBot.move("joint", vals=[-45, 44, -61, 16, 78, 81], velocity=max_vel, acceleration=max_accel,
            cnt_val=25,
            linear=False
        )
        LeftBot.move("joint", vals=[-42, 97, -71.5, 55, 76, 88], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        
        #Carefully getting under the can tab
        LeftBot.move("joint", vals=[-41.406, 93.404, -74.870, 54.548, 77.785, 98.372], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        LeftBot.move("joint", vals=[-40.990, 93.161, -75.437, 54.548, 77.785, 98.371], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        LeftBot.move("joint", vals=[-40.687, 93.271, -75.882, 54.548, 77.785, 98.371], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        LeftBot.move("joint", vals=[-40.229, 93.36, -76.365, 54.549, 77.785, 95.971], velocity=10, acceleration=10,
            cnt_val=0,
            linear=False
        )
        #Quickly drop the can to pop it open
        LeftBot.move("joint", vals=[-40.814, 102, -75, 54, 78, 95.5], velocity=50, acceleration=50,
            cnt_val=0,
            linear=False
        )
        # input("press enter to continue")
        #Move to pouring
        LeftBot.move("joint", vals=[-49, 95, -87, 54, 78, 95.5], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        # input("press enter to continue") 
        LeftBot.move("joint", vals=[-49, 40, -66, 0, 68, 90], velocity=max_vel, acceleration=max_accel,
            cnt_val=50,
            linear=False
        )

        # input("press enter to continue") 
        LeftBot.move("joint", vals=[46, 35, -32, -22, 35, 117.5], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )

    #POURING ROUTINES
    if routine == 1 or routine==2:#Pour into cup for small sized can
        pour_speed = 5
        pour_accel = 5
        # time.sleep(5)
        #Pour half the can out for standard can
        print(f"Waiting for cup to pour into")
        #move to initial pour position
        LeftBot.move("joint", vals=[33, 68.944, -18.5, 92.4, 91.342, 1], velocity=pour_speed, acceleration=pour_accel,
            cnt_val=0,
            linear=False
        )
        
        print(f"left arm is set to go")
        rightset.wait()
        
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
        time.sleep(4)    #Delay to let liquid flow
        #3rd pouring position
        LeftBot.move("joint", vals=[33, 52, 0, 90, 90, -180], velocity=pour_speed, acceleration=pour_accel,
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

    #DROPPING ROUTINES
    if routine != 0: #Drop can and return to starting position
        #Leave pouring safely
        # LeftBot.move("joint",vals=[0, 3, -15, 90, 90, -180], velocity=max_vel,acceleration = max_accel,
        #     cnt_val=25,
        #     linear=False
        # )
        LeftBot.move("joint", vals=[45, -5, -15, 21, 20, 90], velocity=30, acceleration=30,
            cnt_val=25,
            linear=False
        )
        LeftBot.move("joint", vals=[30, -5, -25, 21, 20, 90], velocity=30, acceleration=30,
            cnt_val=25,
            linear=False
        )
        #Prepare to drop can
        LeftBot.move("joint", vals=[15, 66, -86, -28, 83, 93], velocity=30, acceleration=30,
            cnt_val=0,
            linear=False
        )

        LeftBot.move("joint", vals=[13.048, 68.563, -80.078, -30.874, 82.578, 95.335], velocity=30, acceleration=30,
            cnt_val=0,
            linear=False
        )
        #Drop can
        LeftBot.move("joint", vals=[11.788, 68.915, -78.836, -28.516, 81.38, 95.896], velocity=10, acceleration=5,
            cnt_val=0,
            linear=False
        )
        LeftBot.move("joint", vals=[11.794, 66.296, -77.752, -28.6, 80.425, 96.423], velocity=10, acceleration=5,
            cnt_val=0,
            linear=False
        )

        #leave to safe spot
        LeftBot.move("joint", vals=[15, 66, -86, -28, 83, 93], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )

        LeftBot.move("joint", vals=[-3, 70, -95, -28, 83, 93], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        LeftBot.move("joint", vals=[-10, 0, 0, 0, 0, 90], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
    

if __name__ == "__main__":
    left_bot_routine(2)