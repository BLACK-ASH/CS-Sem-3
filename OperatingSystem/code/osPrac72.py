def nonPreemptivePriority(processes):
    """
    processes: list of tuples (pid, arrivalTime, burstTime, priority)
    Lower priority value means higher priority.
    """
    n = len(processes)

    # Sort by arrival time first, then priority
    processes.sort(key=lambda x: (x[1], x[3]))

    completed = 0
    currentTime = 0
    startTime = {}
    completionTime = {}
    waitingTime = {}
    turnaroundTime = {}
    ganttChart = []
    readyQueue = []
    visited = [False] * n

    while completed < n:
        # Add processes that have arrived by current time
        for i in range(n):
            if processes[i][1] <= currentTime and not visited[i]:
                readyQueue.append(processes[i])
                visited[i] = True

        if readyQueue:
            # Pick highest priority (lowest number = highest priority)
            readyQueue.sort(key=lambda x: x[3])  
            pid, at, bt, pr = readyQueue.pop(0)

            if currentTime < at:
                # CPU idle until process arrives
                currentTime = at

            startTime[pid] = currentTime
            ganttChart.append((pid, currentTime, currentTime + bt))
            currentTime += bt
            completionTime[pid] = currentTime

            turnaroundTime[pid] = completionTime[pid] - at
            waitingTime[pid] = turnaroundTime[pid] - bt
            completed += 1
        else:
            # No process ready → CPU idle
            currentTime += 1

    avgWt = sum(waitingTime.values()) / n
    avgTat = sum(turnaroundTime.values()) / n

    # Print Results
    print("\n--- Non-Preemptive Priority Scheduling ---")
    print("PID\tAT\tBT\tPriority\tST\tCT\tTAT\tWT")
    for pid, at, bt, pr in processes:
        print(f"{pid}\t{at}\t{bt}\t{pr}\t\t{startTime[pid]}\t{completionTime[pid]}\t{turnaroundTime[pid]}\t{waitingTime[pid]}")

    print(f"\nAverage Waiting Time: {avgWt:.2f}")
    print(f"Average Turnaround Time: {avgTat:.2f}")

    print("\nGantt Chart:")
    for pid, start, end in ganttChart:
        print(f"| P{pid} ({start}-{end}) ", end="")
    print("|")


# Example usage
processesPriority = [
    (1, 0, 5, 2),  # (PID, Arrival Time, Burst Time, Priority)
    (2, 1, 3, 1),
    (3, 2, 8, 3),
    (4, 3, 6, 2)
]

nonPreemptivePriority(processesPriority)
