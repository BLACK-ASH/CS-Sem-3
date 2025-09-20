import threading
import time
import random

BUFFER_SIZE = 5
buffer = []

mutex = threading.Lock()
empty = threading.Semaphore(BUFFER_SIZE)  # Starts full (5 slots empty)
full = threading.Semaphore(0)             # Starts empty

running = True  # Stop flag

def producer():
    global running
    while running:
        item = random.randint(1, 100)

        if not empty.acquire(timeout=1):  # Avoid deadlock on exit
            continue

        with mutex:
            buffer.append(item)
            print(f"Produced: {item}, Buffer: {buffer}")

        full.release()
        time.sleep(random.uniform(0.1, 0.5))  # Simulate variable production time

def consumer():
    global running
    while running:
        if not full.acquire(timeout=1):  # Avoid deadlock on exit
            continue

        with mutex:
            if buffer:
                item = buffer.pop(0)
                print(f"Consumed: {item}, Buffer: {buffer}")

        empty.release()
        time.sleep(random.uniform(0.1, 0.5))  # Simulate variable consumption time

if __name__ == "__main__":
    producerThread = threading.Thread(target=producer)
    consumerThread = threading.Thread(target=consumer)

    producerThread.start()
    consumerThread.start()

    time.sleep(10)  # Let the simulation run for 10 seconds
    running = False

    # Unblock threads if they're waiting
    empty.release()
    full.release()

    producerThread.join()
    consumerThread.join()

    print("Simulation Finished")
