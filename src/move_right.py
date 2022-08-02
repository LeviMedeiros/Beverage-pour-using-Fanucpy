    from ast import arg
    import multiprocessing
    from fanucpy import Robot
    from multiprocessing import Process
    import time

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
    
    RightBot.move("joint", vals=[-40, 49.2, -28.94, 0.125, 30.484, 0],
    velocity=2, acceleration=2, cnt_val=0, linear=False)        