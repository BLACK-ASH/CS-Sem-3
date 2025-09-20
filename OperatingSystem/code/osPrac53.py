import threading
import queue
import time
import random

BUFFER_SIZE = 5
buffer = queue.Queue(BUFFER_SIZE)
running = True
SENTINEL = None

def producer():
    global running
    while running:
        item = random.randint(1, 100)
        buffer.put(item)
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate some delay

    # Send sentinel value to stop the consumer
    buffer.put(SENTINEL)

def consumer():
    while True:
        item = buffer.get()
        if item is SENTINEL:
            buffer.task_done()
            break
        print(f"Consumed: {item}")
        buffer.task_done()
        time.sleep(random.uniform(0.1, 0.5))  # Simulate processing delay

if __name__ == "__main__":
    producerThread = threading.Thread(target=producer)
    consumerThread = threading.Thread(target=consumer)

    producerThread.start()
    consumerThread.start()

    # Let it run for a while
    time.sleep(10)
    running = False  # Signal the producer to stop

    producerThread.join()
    consumerThread.join()

    print("Simulation Finished")
