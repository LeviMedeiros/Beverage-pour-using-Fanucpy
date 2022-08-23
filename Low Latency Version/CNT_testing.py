from fanucpy_low_latency import Robot
import time

LeftBot = Robot(
        robot_model="Fanuc",
        host="192.168.5.52",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )
LeftBot.connect() 
print(f"Connected to left")

LeftBot.move("joint", vals=[44.852,0.973,-38,0,-60.168,0], velocity=100, acceleration=100,
    cnt_val=50,
    linear=False
)
    
LeftBot.move("joint", vals=[76.557,34.885,-69.776,-33,-25.288,1], velocity=100, acceleration=100,
    cnt_val=100,
    linear=False
)

LeftBot.move("joint", vals=[44.852,16,-28,-4.5,-58,1], velocity=100, acceleration=100,
    cnt_val=50,
    linear=False
)

LeftBot.move("joint", vals=[-8.163,-16.961,-5.839,52.8,-39.821,37], velocity=100, acceleration=100,
    cnt_val = 100,
    linear=False
)