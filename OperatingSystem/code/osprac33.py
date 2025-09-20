import threading
import time

def task(name, delay):
    print(f"[{time.strftime('%H:%M:%S')}] Task {name} started")
    time.sleep(delay)
    print(f"[{time.strftime('%H:%M:%S')}] Task {name} finished")

def sequentialExecution():
    print("\n=== Sequential Execution ===")
    startTime = time.time()

    task("A", 3)
    task("B", 2)
    task("C", 1)

    endTime = time.time()
    print(f"Total time (Sequential): {endTime - startTime:.2f} seconds")

def multithreadedExecution():
    print("\n=== Multithreaded Execution ===")
    startTime = time.time()

    threads = [
        threading.Thread(target=task, args=("A", 3)),
        threading.Thread(target=task, args=("B", 2)),
        threading.Thread(target=task, args=("C", 1)),
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    endTime = time.time()
    print(f"Total time (Multithreaded): {endTime - startTime:.2f} seconds")

# Run both executions
sequentialExecution()
multithreadedExecution()
