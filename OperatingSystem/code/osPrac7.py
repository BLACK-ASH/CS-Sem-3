def fcfsScheduling(processes):
    """
    processes: list of tuples (pid, arrivalTime, burstTime)
    """
    # Sort by arrival time
    processes.sort(key=lambda x: x[1])  

    startTime = []
    completionTime = []
    waitingTime = []
    turnaroundTime = []
    currentTime = 0
    ganttChart = []

    for pid, arrival, burst in processes:
        if currentTime < arrival:
            currentTime = arrival  # CPU idle until process arrives

        startTime.append(currentTime)
        ganttChart.append((pid, currentTime, currentTime + burst))
        currentTime += burst
        completionTime.append(currentTime)

        tat = completionTime[-1] - arrival
        wt = tat - burst

        turnaroundTime.append(tat)
        waitingTime.append(wt)

    avgWt = sum(waitingTime) / len(processes)
    avgTat = sum(turnaroundTime) / len(processes)

    # Print results
    print("\n--- FCFS Scheduling ---")
    print("PID\tAT\tBT\tST\tCT\tTAT\tWT")
    for i, p in enumerate(processes):
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{startTime[i]}\t{completionTime[i]}\t{turnaroundTime[i]}\t{waitingTime[i]}")

    print(f"\nAverage Waiting Time: {avgWt:.2f}")
    print(f"Average Turnaround Time: {avgTat:.2f}")

    print("\nGantt Chart:")
    for pid, start, end in ganttChart:
        print(f"| P{pid} ({start}-{end}) ", end="")
    print("|")


# Example usage
processes = [
    (1, 0, 5),
    (2, 2, 3),
    (3, 4, 1)
]

fcfsScheduling(processes)
