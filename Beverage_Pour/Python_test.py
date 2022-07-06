from multiprocessing import Process

rocket = 0

def func1():
    global rocket
    print('start func1')
    while rocket < 100:
        rocket += 1
        print(rocket)
    print ('end func1')

def func2():
    global rocket
    print ('start func2')
    while rocket < 100:
        rocket += 1
        print(rocket)
    print ('end func2')

if __name__=='__main__':
    p1 = Process(target = func1)
    p1.start()
    p2 = Process(target = func2)
    p2.start()