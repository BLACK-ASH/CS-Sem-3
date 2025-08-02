import threading
import time

def task(name,delay):
    print(f"[{time.strftime('%H:%M:%S')}] Task {name} Started")
    time.sleep(delay)
    print(f"[{time.strftime('%H:%M:%S')}] Task {name} Finshed")

def sequential_execution():
    print("")
    print("-------- Sequential Execution ---------")
    start = time.time()

    task("A",3)
    task("B",2)
    task("C",1)

    end = time.time()
    print(f"Total Time (Sequential) : {end-start:3f} s")

def multi_threaded_execution():
    print("")
    print("-------- Multi Threaded Execution ---------")
    start = time.time()

    threads = [
            threading.Thread(target=task,args=("A",3)),
            threading.Thread(target=task,args=("B",2)),
            threading.Thread(target=task,args=("C",1)),
        ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"Total Time (Multi Threaded) : {end-start:3f} s")

sequential_execution()
multi_threaded_execution()
