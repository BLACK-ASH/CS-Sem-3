import multiprocessing
import time
import random
import queue  # For Full/Empty exceptions

# Producer Function (Blocking with try/except)
def producer(queue_obj, n_items):
    for i in range(n_items):
        item = random.randint(1, 100)
        try:
            queue_obj.put(item)  # Blocking put
            print(f"Produced: {item}")
        except queue.Full:
            print("Queue is full. Skipping item.")
        time.sleep(random.uniform(0.1, 0.5))

# Consumer Function (Blocking with try/except)
def consumer(queue_obj, n_items):
    consumed = 0
    while consumed < n_items:
        try:
            item = queue_obj.get()  # Blocking get
            print(f"Consumed: {item}")
            consumed += 1
        except queue.Empty:
            print("Queue is empty. Waiting...")
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    N_ITEMS = 7
    q = multiprocessing.Queue(maxsize=5)

    p = multiprocessing.Process(target=producer, args=(q, N_ITEMS))
    c = multiprocessing.Process(target=consumer, args=(q, N_ITEMS))

    p.start()
    c.start()
    p.join()
    c.join()
