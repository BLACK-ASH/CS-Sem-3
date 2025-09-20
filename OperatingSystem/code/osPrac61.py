import threading
import time
import random

# Semaphores
mutex = threading.Semaphore(1)  # Protects readerCount
db = threading.Semaphore(1)     # Controls access to sharedData

# Shared resource and reader count
sharedData = 0
readerCount = 0
isRunning = True  # Stop flag

def reader(readerId):
    global readerCount, sharedData, isRunning
    while isRunning:
        # Entry section
        mutex.acquire()
        readerCount += 1
        if readerCount == 1:
            db.acquire()  # First reader locks db
        mutex.release()

        # Critical section
        print(f"[Reader] {readerId} reads {sharedData}")
        time.sleep(random.uniform(0.2, 0.5))

        # Exit section
        mutex.acquire()
        readerCount -= 1
        if readerCount == 0:
            db.release()  # Last reader unlocks db
        mutex.release()

        # Pause before next read
        time.sleep(random.uniform(0.5, 1.0))

def writer(writerId):
    global sharedData, isRunning
    while isRunning:
        db.acquire()  # Exclusive access
        sharedData += 1
        print(f"[Writer] {writerId} writes {sharedData}")
        time.sleep(random.uniform(0.3, 0.6))
        db.release()

        # Pause before next write
        time.sleep(random.uniform(0.8, 1.5))

if __name__ == "__main__":
    readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
    writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

    for t in readers + writers:
        t.start()

    time.sleep(10)  # Run simulation for 10 sec
    isRunning = False  # Stop all threads

    for t in readers + writers:
        t.join()

    print("Simulation finished.")
