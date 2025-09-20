import threading

def fibonacci(n, name):
    a, b = 0, 1
    print(f"{name} generating {n} Fibonacci numbers:")
    for i in range(n):
        print(f"{name}: {a}")
        a, b = b, a + b

# Create threads for two Fibonacci sequences
thread1 = threading.Thread(target=fibonacci, args=(5, "Thread-1"))
thread2 = threading.Thread(target=fibonacci, args=(7, "Thread-2"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All Fibonacci threads finished.")
