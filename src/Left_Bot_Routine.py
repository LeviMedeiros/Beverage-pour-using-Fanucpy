#Import Robot Library
from fanucpy import Robot

def left_bot_routine(routine):
    max_speed = 10
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
    
    if routine==1:
        #Pick up can
        LeftBot.move(
            "joint",
            vals=[-18, 71, -41.5, -12, 60, 99],
            velocity=max_speed,
            acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        LeftBot.move(
            "joint",
            vals=[-18, 83, -42, -12, 60.5, 99],
            velocity=max_speed,
            acceleration=max_accel,
            cnt_val=0,
            linear=False
        )

        LeftBot.move(
            "joint",
            vals=[-18, 63, -37, -12.5, 55.5, 100],
            velocity=max_speed,
            acceleration=max_accel,
            cnt_val=0,
            linear=False
        )
        print(f"Can picked up")
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
    
    #Open Can
    print(f"Beginning Opening Can routine")
    LeftBot.move("joint", vals=[-45, 44, -61, 16, 78, 81], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    #input("press enter to continue")
    LeftBot.move("joint", vals=[-42, 97, -71.5, 55, 76, 88], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    #input("press enter to continue")
    LeftBot.move("joint", vals=[-41.135, 93.7, -75.15, 53.997, 77.785, 94.7], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    #input("press enter to continue")
    LeftBot.move("joint", vals=[-40.814, 93.226, -76.216, 53.520, 78.261, 95.459], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    #input("press enter to continue")
    LeftBot.move("joint", vals=[-40.814, 102, -75, 54, 78, 95.5], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    #input("press enter to continue")
    #Move to pouring
    LeftBot.move("joint", vals=[-49, 95, -87, 54, 78, 95.5], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    #input("press enter to continue") 
    LeftBot.move("joint", vals=[-49, 40, -66, 0, 68, 90], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    #input("press enter to continue") 
    LeftBot.move("joint", vals=[46, 35, -32, -22, 35, 117.5], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    # input("press enter to continue") 
    if routine == 1:
        #Pour half the can out for standard can
        print(f"Waiting for cup to pour into")
    elif routine == 2:
        #Pour the whole can out for bubly/diet coke
        print(f"Waiting for cup to pour into")

    elif routine == 3:
        print(f"Waiting for cup to pour in")
        #Pour half the can out for xl beers
    
    #Leave pouring safely current waypoint totally wrong
    LeftBot.move("joint", vals=[26, 95, -87, 61, 86, 105], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )

    #Prepare to drop can
    LeftBot.move("joint", vals=[15, 66, -86, -28, 83, 93], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    # LeftBot.move("joint", vals=[12, 69, -80, -29, 82.5, 95], velocity=max_speed, acceleration=max_accel,
    #     cnt_val=0,
    #     linear=False
    # )

    LeftBot.move("joint", vals=[13.048, 68.563, -80.078, -30.874, 82.578, 95.335], velocity=10, acceleration=10,
        cnt_val=0,
        linear=False
    )
    #Drop can
    LeftBot.move("joint", vals=[11.788, 68.915, -78.836, -28.516, 81.38, 95.896], velocity=10, acceleration=10,
        cnt_val=0,
        linear=False
    )
    LeftBot.move("joint", vals=[11.794, 68.324, -78.604, -28.533, 81.174, 96], velocity=10, acceleration=10,
        cnt_val=0,
        linear=False
    )

    #leave to safe spot
    LeftBot.move("joint", vals=[15, 66, -86, -28, 83, 93], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )

    LeftBot.move("joint", vals=[-3, 70, -95, -28, 83, 93], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    LeftBot.move("joint", vals=[-10, 0, 0, 0, 0, 90], velocity=max_speed, acceleration=max_accel,
        cnt_val=0,
        linear=False
    )
    

if __name__ == "__main__":
    left_bot_routine(1)