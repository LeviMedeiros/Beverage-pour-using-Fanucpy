from fanucpy import Robot
from multiprocessing import Process

from Beverage_Pour.Right_Bot_Routine import right_bot_routine
from Beverage_Pour.Left_Bot_Routine import left_bot_routine

RightBot = Robot(
    robot_model="Fanuc",
    host="192.168.1.100",
    port=18735,
    ee_DO_type="RDO",
    ee_DO_num=7,
)

LeftBot = Robot(
    robot_model="Fanuc",
    host="192.168.1.101",
    port=18735,
    ee_DO_type="RDO",
    ee_DO_num=7,
)
RightBot.__version__()
RightBot.connect()

LeftBot.__version__()
LeftBot.connect()  

if __name__=='__main__':
    p1 = Process(target = left_bot_routine(RightBot))
    p1.start()
    p2 = Process(target = right_bot_routine(LeftBot))
    p2.start()


