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
tic = time.perf_counter()

for i in range(1,5):
    tic2 = time.perf_counter()
    LeftBot.move("joint", vals=[44.852,0.973,-38,0,-60.168,0], velocity=100, acceleration=100,
        cnt_val=0,
        linear=False
    )
    toc2 = time.perf_counter()      
    LeftBot.move("joint", vals=[76.557,34.885,-69.776,-33,-25.288,1], velocity=100, acceleration=100,
        cnt_val=0,
        linear=False
    )
    toctoc2 = time.perf_counter()
    print(f"1 movement {toc2-tic2:0.4f}")
    print(f"2 movements {toctoc2-tic2:0.4f}")
    print(f"2nd movement{toctoc2-toc2:0.4f}")
    tic3 = time.perf_counter()
    LeftBot.move("joint", vals=[23,16,-28,-4.5,-58,1], velocity=100, acceleration=100,
        cnt_val=100,
        linear=False
    )
    toc3 = time.perf_counter()
    print(f"cnt 100 movement time {toc3-tic3:0.4f}")
    LeftBot.move("joint", vals=[-44.058,28.695,-37.897,2.2,-73.248,1], velocity=100, acceleration=100,
        cnt_val=0,
        linear=False
    )
    tic4 = time.perf_counter()
    LeftBot.move("joint", vals=[-8.163,-16.961,-5.839,52.8,-39.821,37], velocity=100, acceleration=100,
        cnt_val = 100,
        linear=False
    )
    toc4 = time.perf_counter()
    print(f"cnt 100 movement time 2:{toc4-tic4:0.4f}")   
    LeftBot.move("joint", vals=[44.852,0.973,-38.001,0,-60.168,0], velocity=100, acceleration=100,
        cnt_val=0,
        linear=False
    )
toc = time.perf_counter()
print(f"Total time {toc-tic:0.4f}")