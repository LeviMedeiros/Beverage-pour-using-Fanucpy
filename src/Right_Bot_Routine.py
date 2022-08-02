from fanucpy import Robot
import time
def right_bot_rountine(routine,leftset,rightset):
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
    # move in joint space
    # RightBot.move(
    #     "joint",
    #     vals=[90, 0, 0, 0, 0, 0],
    #     velocity=50,
    #     acceleration=50,
    #     cnt_val=0,
    #     linear=False
    # )

    # move in cartesian space
    if routine == 0:
        RightBot.move(
        "joint",
        vals=[20, 0, 0, 0, 0, 0],
        velocity=max_vel,
        acceleration=max_accel,
        cnt_val=0,
        linear=False
    )

    if routine == 2:
        # time.sleep(5)

        #input("press enter to continue")
        RightBot.move("joint", vals=[20, 0, 0, 0, 0, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        # # #PICKING UP THE CUP
        # # input("press enter to continue")
        # RightBot.move("joint", vals=[23.433, 85.093, -64.848, 0, 60.285, 0],
        # velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        # # input("press enter to continue")
        # RightBot.move("joint", vals=[22.873, 104.783, -37.108, 0.864, 35.459, 0],
        # velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        # # input("press enter to continue")
        # RightBot.move("joint", vals=[22.204, 95.207, -36.866, 0.521, 37.874, 0],
        # velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        # # input("press enter to continue")
        # RightBot.move("joint", vals=[23, 15, -36.866, 0.521, 37.874, 0],
        # velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)
  
        pour_speed = 5
        pour_accel = 5
        
        # time.sleep(3)
        #RECEIVING THE DRINK
        #Waiting to be ready to pour
        RightBot.move("joint", vals=[-40, 36.726, -37.054, 0.125, -2.634, 0],
        velocity=pour_speed, acceleration=pour_accel, cnt_val=0, linear=False)

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

        #TRANSFERRING THE CUP
        #input("press enter to continue")
        # RightBot.move("joint", vals=[-37.623, 53.923, -19.32, 0, 28.34, -43.638],
        # velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        # #input("press enter to continue")
        # RightBot.move("joint", vals=[-37.836, 48.825, -17.922, 0, 28.34, -14.931],
        # velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        # #input("press enter to continue")
        # RightBot.move("joint", vals=[-43.928, 45, -17.924, 0, 17, 0],
        # velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        #input("press enter to continue")
        RightBot.move("joint", vals=[-17, 62, -29.5, -1.5, 28.5, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        #input("press enter to continue")
        RightBot.move("joint", vals=[29, 62, -25.5, -1.5, 25, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        #input("press enter to continue")
        RightBot.move("joint", vals=[35.046, 67.638, -18.708, -1.619, 18.898, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        #input("press enter to continue")
        RightBot.move("joint", vals=[35.846, 75.288, -23.142, -1.619, 20.848, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

        #input("press enter to continue")
        RightBot.move("joint", vals=[35.846, 57.979, -36.898, -1.619, 20.848, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=True)        

        #PURGE THE CUP ******DELETE LATER*******
        # input("press enter to continue")
        # RightBot.move("joint", vals=[-40.693, -24.626, 112.756, 0.125, 30.484, 0],
        # velocity=40, acceleration=40, cnt_val=0, linear=False)  

        #input("press enter to continue")
        RightBot.move("joint", vals=[20, 0, 0, 0, 0, 0],
        velocity=max_vel, acceleration=max_accel, cnt_val=0, linear=False)

    # get robot state
    print(f"Current pose: {RightBot.get_curpos()}")
    print(f"Current joints: {RightBot.get_curjpos()}")
    print(f"Energy consumption: {RightBot.get_ins_power()}")

if __name__ == '__main__':
    right_bot_rountine(1)