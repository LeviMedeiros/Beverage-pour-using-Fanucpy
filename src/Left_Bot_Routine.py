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
            vals=[-18.001, 83.411, -42.087, -11.99, 60.581, 98.977],
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
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)
       
        LeftBot.move("joint", vals=[-23.447, 80.623, -45.005, -11.493, 60.764, 98.491],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        LeftBot.move("joint", vals=[-23.306, 40, -45.017, -11.646, 60.79, 98.603],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    
    if routine==3: #Pick up right can
        print(f"Picking up right can")
        print(f"Current pose: {LeftBot.get_curpos()}")
        LeftBot.move("joint", vals=[-28.901, 64.667, -45.005, -11.646, 60.79, 98.604],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        LeftBot.move("joint", vals=[-28.9, 75.881, -45.206, -11.624, 60.985, 98.555],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        LeftBot.move("joint", vals=[-28.901, 40, -45.005, -11.646, 60.79, 98.604],
            velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)


        print(f"Current pose: {LeftBot.get_curpos()}")
    
    #OPENING ROUTINE
    if routine==1 or routine==2 or routine==3: #Open Can
        max_vel = 10
        max_accel = 10
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
        LeftBot.move("joint", vals=[-41.322, 94.139, -74.925, 54.349, 77.784, 97.342], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        input("press enter to continue")
        LeftBot.move("joint", vals=[-40.629, 93.832, -75.905, 53.488, 78.217, 98.255], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        input("press enter to continue")
        LeftBot.move("joint", vals=[-40, 94.525, -76.672, 53.054, 78.613, 98.921], velocity=max_vel, acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        LeftBot.move("joint", vals=[-40, 94.525, -76.672, 53.054, 78.613, 110], velocity=15, acceleration=20,
            cnt_val=0,
            linear=False
        )
        LeftBot.move("joint", vals=[-41.1, 94.793, -76.141, 53.054, 78.613, 125], velocity=15, acceleration=20,
            cnt_val=0,
            linear=False
        )
        #Quickly drop the can to pop it open
        # input("press enter to continue")
        # LeftBot.move("joint", vals=[-40.323, 101.418, -75.619, 53.228, 77.982, 98.061], velocity=25, acceleration=50,
        #     cnt_val=0,
        #     linear=False
        # )
        # LeftBot.move("joint", vals=[-40.814, 102, -75, 54, 78, 95.5], velocity=50, acceleration=50,
        #     cnt_val=0,
        #     linear=False
        # )
        # input("press enter to continue")
        #Move to pouring
        LeftBot.move("joint", vals=[-49, 95, -87, 54, 78, 95.5], velocity=20, acceleration=20,
            cnt_val=0,
            linear=False
        )
        # input("press enter to continue") 
        LeftBot.move("joint", vals=[-49, 40, -66, 0, 68, 90], velocity=20, acceleration=20,
            cnt_val=50,
            linear=False
        )

        # input("press enter to continue") 
        LeftBot.move("joint", vals=[46, 35, -32, -22, 35, 117.5], velocity=20, acceleration=20,
            cnt_val=0,
            linear=False
        )
    #Old routine
        # print(f"Beginning Opening Can routine")
        # #Move to the starting position for opening the can
        # LeftBot.move("joint", vals=[-45, 44, -61, 16, 78, 81], velocity=max_vel, acceleration=max_accel,
        #     cnt_val=25,
        #     linear=False
        # )
        # LeftBot.move("joint", vals=[-42, 97, -71.5, 55, 76, 88], velocity=max_vel, acceleration=max_accel,
        #     cnt_val=0,
        #     linear=False
        # )
        
        # #Carefully getting under the can tab
        # LeftBot.move("joint", vals=[-41.322, 94.139, -74.925, 54.349, 77.784, 97.342], velocity=max_vel, acceleration=max_accel,
        #     cnt_val=0,
        #     linear=False
        # )
        # # input("press enter to continue")
        # LeftBot.move("joint", vals=[-40.629, 93.832, -75.905, 53.488, 78.217, 98.255], velocity=max_vel, acceleration=max_accel,
        #     cnt_val=0,
        #     linear=False
        # )
        # # input("press enter to continue")
        # LeftBot.move("joint", vals=[-40, 94.525, -76.672, 53.054, 78.613, 98.921], velocity=max_vel, acceleration=max_accel,
        #     cnt_val=0,
        #     linear=False
        # )

        # #Quickly drop the can to pop it open
        # LeftBot.move("joint", vals=[-40.323, 101.418, -75.619, 53.228, 77.982, 98.061], velocity=25, acceleration=50,
        #     cnt_val=0,
        #     linear=False
        # )
        # # LeftBot.move("joint", vals=[-40.814, 102, -75, 54, 78, 95.5], velocity=50, acceleration=50,
        # #     cnt_val=0,
        # #     linear=False
        # # )
        # # input("press enter to continue")
        # #Move to pouring
        # LeftBot.move("joint", vals=[-49, 95, -87, 54, 78, 95.5], velocity=20, acceleration=20,
        #     cnt_val=0,
        #     linear=False
        # )
        # # input("press enter to continue") 
        # LeftBot.move("joint", vals=[-49, 40, -66, 0, 68, 90], velocity=20, acceleration=20,
        #     cnt_val=50,
        #     linear=False
        # )

        # # input("press enter to continue") 
        # LeftBot.move("joint", vals=[46, 35, -32, -22, 35, 117.5], velocity=20, acceleration=20,
        #     cnt_val=0,
        #     linear=False
        # )

    #POURING ROUTINES
    if routine == 2:#Pour into cup for small sized can
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
    elif routine != 0:
        #Pour beer can
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
        # input("press enter to continue")
        LeftBot.move("joint", vals=[30, -5, -25, 21, 20, 90], velocity=30, acceleration=30,
            cnt_val=25,
            linear=False
        )
        #Prepare to drop can
        LeftBot.move("joint", vals=[15, 66, -86, -28, 83, 93], velocity=30, acceleration=30,
            cnt_val=0,
            linear=False
        )
        # input("press enter to continue")
        LeftBot.move("joint", vals=[13.007, 70.099, -78.465, -31.214, 80.941, 96.491], velocity=30, acceleration=30,
            cnt_val=0,
            linear=False
        )
        #Drop can
        # input("press enter to continue")
        LeftBot.move("joint", vals=[12.968, 70.165, -78.239, -31.194, 80.742, 96.605], velocity=10, acceleration=5,
            cnt_val=0,
            linear=False
        )
        # input("press enter to continue")
        LeftBot.move("joint", vals=[12.968, 68.673, -77.668, -31.242, 80.253, 96.908], velocity=10, acceleration=5,
            cnt_val=0,
            linear=False
        )
        # input("press enter to continue")
        LeftBot.move("joint", vals=[15.295, 66.369, -88.844, -33.068, 89.864, 91.176], velocity=10, acceleration=5,
            cnt_val=0,
            linear=False
        )
        # # input("press enter to continue")
        # LeftBot.move("joint", vals=[15, 66, -86, -28, 83, 93], velocity=30, acceleration=30,
        #     cnt_val=0,
        #     linear=False
        # )
        # # input("press enter to continue")
        # LeftBot.move("joint", vals=[13.107, 70.11, -78.405, -31.325, 80.906, 96.539], velocity=30, acceleration=30,
        #     cnt_val=0,
        #     linear=False
        # )
        # #Drop can
        # # input("press enter to continue")
        # LeftBot.move("joint", vals=[13.163, 70.238, -77.965, -31.419, 80.536, 96.781], velocity=10, acceleration=5,
        #     cnt_val=0,
        #     linear=False
        # )
        # LeftBot.move("joint", vals=[13.162, 69.163, -77.56, -31.456, 80.188, 97], velocity=10, acceleration=5,
        #     cnt_val=0,
        #     linear=False
        # )
        # # input("press enter to continue")
        # LeftBot.move("joint", vals=[13.214, 69.393, -84.488, -29.655, 86.366, 93.338], velocity=10, acceleration=5,
        #     cnt_val=0,
        #     linear=False
        # )


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