import threading

lock = threading.Lock()
sharedSum = 0

def addFibonacciSum(n):
    global sharedSum
    a, b = 0, 1
    for _ in range(n):
        with lock:  # Ensure only one thread updates at a time
            sharedSum += a
        a, b = b, a + b

threads = []

# Create and start 3 threads
for i in range(3):
    t = threading.Thread(target=addFibonacciSum, args=(5,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Total sum of Fibonacci numbers (shared):", sharedSum)
