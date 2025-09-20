import threading
import time

def task(name, delay):
    print(f"[{time.strftime('%H:%M:%S')}] Thread {name} starting")
    print(f"[{time.strftime('%H:%M:%S')}] Thread {name} sleeping for {delay} seconds")
    time.sleep(delay)
    print(f"[{time.strftime('%H:%M:%S')}] Thread {name} finished")

def main():
    print(f"[{time.strftime('%H:%M:%S')}] Main thread: Creating threads")

    threads = [
        threading.Thread(target=task, args=("A", 3), name="Thread-A"),
        threading.Thread(target=task, args=("B", 2), name="Thread-B"),
        threading.Thread(target=task, args=("C", 1), name="Thread-C"),
    ]

    for t in threads:
        print(f"[{time.strftime('%H:%M:%S')}] Main thread: Starting {t.name}")
        t.start()

    for t in threads:
        print(f"[{time.strftime('%H:%M:%S')}] Main thread: Waiting for {t.name} to finish")
        t.join()
        print(f"[{time.strftime('%H:%M:%S')}] Main thread: {t.name} finished")

    print(f"[{time.strftime('%H:%M:%S')}] Main thread: All threads completed")

if __name__ == "__main__":
    main()
