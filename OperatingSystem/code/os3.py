import threading
import time

def task(name, delay):
    print(f"Task {name} started")
    time.sleep(delay)
    print(f"Task {name} finished after {delay} seconds.")

def singleThreaded():
    startTime = time.time()
    task("A", 2)
    task("B", 2)
    endTime = time.time()
    print(f"Single-threaded execution time: {endTime - startTime} seconds")

def multiThreaded():
    startTime = time.time()

    threadA = threading.Thread(target=task, args=("A", 2))
    threadB = threading.Thread(target=task, args=("B", 2))

    threadA.start()
    threadB.start()

    threadA.join()
    threadB.join()

    endTime = time.time()
    print(f"Multi-threaded execution time: {endTime - startTime} seconds")

if __name__ == "__main__":
    print("Running single-threaded version")
    singleThreaded()

    print("\nRunning multi-threaded version")
    multiThreaded()
