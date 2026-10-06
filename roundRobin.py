processes = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 15],
    ["P4", 3, 11],
    ["P5", 4, 20],
    ["P6", 4, 9]
]

time_quantum = 5

remaining_bt = {p[0]: p[2] for p in processes}

arrival_time = {p[0]: p[1] for p in processes}

completion_time = {}

ready_queue = []
gantt_chart = []

time = 0
completed = 0
n = len(processes)

processes.sort(key=lambda x: x[1])

i = 0

while completed < n:

    while i < n and processes[i][1] <= time:
        ready_queue.append(processes[i][0])
        i += 1

    if not ready_queue:
        time = processes[i][1]
        continue

    current = ready_queue.pop(0)

    execution_time = min(time_quantum, remaining_bt[current])

    start_time = time
    time += execution_time

    remaining_bt[current] -= execution_time

    gantt_chart.append(
        [current, start_time, time]
    )

    while i < n and processes[i][1] <= time:
        ready_queue.append(processes[i][0])
        i += 1

    if remaining_bt[current] > 0:
        ready_queue.append(current)
    else:
        completed += 1
        completion_time[current] = time

turnaround_time = {}
waiting_time = {}

for p, at, bt in processes:
    tat = completion_time[p] - at
    wt = tat - bt

    turnaround_time[p] = tat
    waiting_time[p] = wt

print("\nGantt Chart:")
for process, start, end in gantt_chart:
    print(f"{start} -- {process} -- {end}")

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

total_tat = 0
total_wt = 0

for p, at, bt in processes:
    ct = completion_time[p]
    tat = turnaround_time[p]
    wt = waiting_time[p]

    total_tat += tat
    total_wt += wt

    print(f"{p}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

print("\nAverage Turnaround Time:",
      total_tat / n)

print("Average Waiting Time:",
      total_wt / n)