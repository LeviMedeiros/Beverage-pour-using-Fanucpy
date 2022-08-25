from fanucpy import Robot
import time
def right_bot_rountine(routine,leftset,rightset,leftset2):
    max_vel = 5
    max_accel = 5

    RightBot = Robot(
        robot_model="Fanuc",
        host="192.168.5.52",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )

    RightBot.__version__()

    RightBot.connect()
    print(f"Connected to RightBot")

    # move in cartesian space
    if routine == 0:
        RightBot.move(
        "joint",
        vals=[20, 0, 0, 0, 0, 0],
        velocity=20,
        acceleration=20,
        cnt_val=0,
        linear=False
    )


    # time.sleep(5)

    # input("press enter to continue")
    RightBot.move("joint", vals=[20, 0, 0, 0, 0, 0],
    velocity=30, acceleration=30, cnt_val=0, linear=False)

    # #PICKING UP THE CUP
    # input("press enter to continue")
    RightBot.move("joint", vals=[25.779, 83.807, -65.379, -1.963, 68.708, 0],
    velocity=50, acceleration=50, cnt_val=0, linear=False)

    # input("press enter to continue")
    RightBot.move("joint", vals=[23.572, 91.44, -52.614, 2.885, 44.123, 0],
    velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    # input("press enter to continue")
    RightBot.move("joint", vals=[23.852, 96.704, -44.051, 2.977, 35.562, 0],
    velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    # input("press enter to continue")
    RightBot.move("joint", vals=[25.204, 80.235, -41.361, 0.727, 32.841, 0],
    velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    # input("press enter to continue")
    RightBot.move("joint", vals=[25.208, 53.077, -10.236, 3.165, 6.355, 0],
    velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)
    
    # time.sleep(3)
    if routine == 2:
        #RECEIVING THE DRINK
        #Waiting to be ready to pour
        RightBot.move("joint", vals=[-40, 36.726, -60, 0.125, -2.634, 0],
        velocity=50, acceleration=50, cnt_val=0, linear=False)
        print(f"waiting for left")
        leftset2.wait()
        RightBot.move("joint", vals=[-40, 36.726, -37.054, 0.125, -2.634, 0],
        velocity=10, acceleration=10, cnt_val=0, linear=False)

        #First receiving position
        rightset.set()
        print(f"right arm is set to go")
        leftset.wait()
        rightset.clear()

        #Second receiving position
        time.sleep(0.5) #Delay to avoid collision
        RightBot.move("joint", vals=[-40, 36.429, -36.022, 0.125, 14.261, 0],
        velocity=2, acceleration=2, cnt_val=0, linear=False)        
        
        #D
        time.sleep(4)
        time.sleep(0.1)
        time.sleep(0.5)
        RightBot.move("joint", vals=[-40, 51.341, -27.073, 0.125, 30.484, 0],
        velocity=3, acceleration=3, cnt_val=0, linear=False)        

        time.sleep(2) #delay to wait for arm to reach position
        time.sleep(4) #delay while pouring
        time.sleep(2) #delay to avoid interference
        RightBot.move("joint", vals=[-40, -24.06, -28.94, 0.125, 30.484, 0],
        velocity=10, acceleration=10, cnt_val=0, linear=False)     
    elif routine != 0:
        RightBot.move("joint", vals=[-40, 36.726, -60, 0.125, -2.634, 0],
        velocity=50, acceleration=50, cnt_val=0, linear=False)
        print(f"waiting for left")
        leftset2.wait()
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

    #TRANSFERRING THE CUP
    # input("press enter to continue")
    RightBot.move("joint", vals=[46.190, 57.4, -19.615, 1.676, 15.726, 0],
    velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    # input("press enter to continue")
    RightBot.move("joint", vals=[45.344, 64.117, -33.194, 2.658, 29.323, 0],
    velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    # input("press enter to continue")
    RightBot.move("joint", vals=[45.898, 56.528, -40.303, 1.26, 36.415, 0],
    velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    #input("press enter to continue")
    RightBot.move("joint", vals=[20, 0, 0, 0, 0, 0],
    velocity=50, acceleration=50, cnt_val=0, linear=False)

if __name__ == '__main__':
    right_bot_rountine(1)