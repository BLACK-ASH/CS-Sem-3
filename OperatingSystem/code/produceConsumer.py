import multiprocessing
import time
import random

# Producer Function
def producer(queue, n_items):
    for i in range(n_items):
        item = random.randint(1, 100)
        queue.put(item)  # Blocking put
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))

# Consumer Function
def consumer(queue, n_items):
    for i in range(n_items):
        item = queue.get()  # Blocking get
        print(f"Consumed: {item}")
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    N_ITEMS = 7
    queue = multiprocessing.Queue(maxsize=5)  # Limited size for demo

    p = multiprocessing.Process(target=producer, args=(queue, N_ITEMS))
    c = multiprocessing.Process(target=consumer, args=(queue, N_ITEMS))

    p.start()
    c.start()
    p.join()
    c.join()
