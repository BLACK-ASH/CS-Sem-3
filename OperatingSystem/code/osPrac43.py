from concurrent.futures import ThreadPoolExecutor

def fibonacciList(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Thread pool with 3 workers
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fibonacciList, [5, 7, 10]))

# Display results
for i, seq in enumerate(results, 1):
    print(f"Task {i} result: {seq}")
