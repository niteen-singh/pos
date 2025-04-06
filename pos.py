# CPU Scheduling Algorithms
import sys
import os
import shutil


# 1. FCFS (First-Come, First-Served) Algorithm
def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")


processes = [("P1", 5), ("P2", 3), ("P3", 8)]
fcfs(processes)


# 2. SJF (Shortest Job First) Non-Preemptive Algorithm
def sjf_non_preemptive(processes):
    processes.sort(key=lambda x: x[1])  # Sort by burst time
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")


processes = [("P1", 6), ("P2", 8), ("P3", 7), ("P4", 3)]
sjf_non_preemptive(processes)


# 3. SJF (Shortest Job First) Preemptive Algorithm
def sjf_preemptive(processes):
    n = len(processes)
    remaining_time = [p[1] for p in processes]
    complete = 0
    time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n

    while complete < n:
        idx = -1
        min_time = float('inf')
        for i in range(n):
            if remaining_time[i] > 0 and remaining_time[i] < min_time:
                min_time = remaining_time[i]
                idx = i

        if idx != -1:
            remaining_time[idx] -= 1
            time += 1
            if remaining_time[idx] == 0:
                complete += 1
                turnaround_time[idx] = time
                waiting_time[idx] = turnaround_time[idx] - processes[idx][1]

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")


processes = [("P1", 8), ("P2", 4), ("P3", 9), ("P4", 5)]
sjf_preemptive(processes)


# 4. Round Robin Algorithm
def round_robin(processes, time_quantum):
    n = len(processes)
    remaining_time = [p[1] for p in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0
    complete = 0

    while complete < n:
        for i in range(n):
            if remaining_time[i] > 0:
                if remaining_time[i] > time_quantum:
                    time += time_quantum
                    remaining_time[i] -= time_quantum
                else:
                    time += remaining_time[i]
                    waiting_time[i] = time - processes[i][1]
                    remaining_time[i] = 0
                    complete += 1

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")


processes = [("P1", 10), ("P2", 5), ("P3", 8)]
time_quantum = 3
round_robin(processes, time_quantum)


# 5. Priority (Non-Preemptive) Algorithm
def priority_non_preemptive(processes):
    processes.sort(key=lambda x: x[2])  # Sort by priority
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + processes[i - 1][1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")


processes = [("P1", 4, 2), ("P2", 1, 1), ("P3", 8, 3)]
priority_non_preemptive(processes)


# 6. Priority (Preemptive) Algorithm
def priority_preemptive(processes):
    n = len(processes)
    remaining_time = [p[1] for p in processes]
    complete = 0
    time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n

    while complete < n:
        idx = -1
        max_priority = float('inf')
        for i in range(n):
            if remaining_time[i] > 0 and processes[i][2] < max_priority:
                max_priority = processes[i][2]
                idx = i

        if idx != -1:
            remaining_time[idx] -= 1
            time += 1
            if remaining_time[idx] == 0:
                complete += 1
                turnaround_time[idx] = time
                waiting_time[idx] = turnaround_time[idx] - processes[idx][1]

    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")


processes = [("P1", 6, 2), ("P2", 8, 1), ("P3", 7, 3)]
priority_preemptive(processes)


# Memory Management Algorithms

# 1. FIFO Page Replacement Algorithm
def fifo_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0

    for page in pages:
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1

    print(f"Total Page Faults: {page_faults}")


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
frame_size = 3
fifo_page_replacement(pages, frame_size)


# 2. Optimal Page Replacement Algorithm
def optimal_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                farthest = -1
                index_to_replace = -1
                for j in range(len(frame)):
                    try:
                        next_use = pages[i + 1:].index(frame[j])
                    except ValueError:
                        next_use = float('inf')
                    if next_use > farthest:
                        farthest = next_use
                        index_to_replace = j
                frame[index_to_replace] = page
            page_faults += 1

    print(f"Total Page Faults: {page_faults}")


pages = [0, 2, 1, 0, 1, 2, 0, 3, 0, 4]
frame_size = 3
optimal_page_replacement(pages, frame_size)


# 3. LRU Page Replacement Algorithm
def lru_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0

    for page in pages:
        if page not in frame:
            if len(frame) < frame_size:
                frame.append(page)
            else:
                lru_index = pages.index(frame[0])
                for p in frame:
                    if pages.index(p) < lru_index:
                        lru_index = pages.index(p)
                frame[lru_index] = page
            page_faults += 1

    print(f"Total Page Faults: {page_faults}")


pages = [4, 1, 2, 1, 3, 4, 2, 3]
frame_size = 3
lru_page_replacement(pages, frame_size)


# 4. Banker’s Algorithm for Deadlock Avoidance

# step 1: Need matrix
def calc_need(allocated, max_):
    need = {}
    for pid in allocated:
        max_list = max_[pid]
        alloc_list = allocated[pid]
        need_values = []
        for i in range(len(max_list)):
            need_values.append(max_list[i] - alloc_list[i])
        need[pid] = need_values
    return need


def bankers(allocated, max_, available):
    need = calc_need(allocated, max_)
    safe_sequence = []
    not_processed = 0
    processes = []
    for pid in allocated:
        processes.append(pid)
    total_processes = len(processes)

    while not_processed < total_processes and len(safe_sequence) != total_processes:
        pid = processes.pop(0)
        # Check if the process can be serviced
        if available >= need[pid]:
            # The process can be serviced
            safe_sequence.append(pid)
            not_processed = 0
            for i in range(len(available)):
                available[i] += allocated[pid][i]
        else:
            not_processed += 1
            processes.append(pid)

    if len(safe_sequence) != total_processes:
        print("No safe sequence possible")
    else:
        print("Safe sequence possible")
        print(*safe_sequence, sep="->")
        print("Avaiable: ", available)


# get the input
if __name__ == "__main__":
    available = [3, 3, 2]
    allocated = {"p0": [0, 1, 0], "p1": [2, 0, 0], "p2": [3, 0, 2], "p3": [2, 1, 1], "p4": [0, 0, 2]}
    max_ = {"p0": [7, 5, 3], "p1": [3, 2, 2], "p2": [9, 0, 2], "p3": [2, 2, 2], "p4": [4, 3, 3]}
    bankers(allocated, max_, available)

# linux command line
import subprocess
import sys


def execute_command(command):
    try:
        if command == "wc":
            file_name = sys.argv[2]
            result = subprocess.run(['wc', file_name], capture_output=True, text=True)
            print(result.stdout)
        elif command == "ls":
            result = subprocess.run(['ls'], capture_output=True, text=True)
            print(result.stdout)
        elif command == "cat":
            file_name = sys.argv[2]
            result = subprocess.run(['cat', file_name], capture_output=True, text=True)
            print(result.stdout)
        elif command == "pwd":
            result = subprocess.run(['pwd'], capture_output=True, text=True)
            print(result.stdout)
        elif command == "cp":
            src = sys.argv[2]
            dest = sys.argv[3]
            subprocess.run(['cp', src, dest])
            print(f"Copied {src} to {dest}")
        elif command == "rm":
            file_name = sys.argv[2]
            subprocess.run(['rm', file_name])
            print(f"Removed {file_name}")
        elif command == "mkdir":
            dir_name = sys.argv[2]
            subprocess.run(['mkdir', dir_name])
            print(f"Created directory {dir_name}")
        elif command == "mv":
            src = sys.argv[2]
            dest = sys.argv[3]
            subprocess.run(['mv', src, dest])
            print(f"Moved {src} to {dest}")
        elif command == "head":
            file_name = sys.argv[2]
            result = subprocess.run(['head', file_name], capture_output=True, text=True)
            print(result.stdout)
        elif command == "tail":
            file_name = sys.argv[2]
            result = subprocess.run(['tail', file_name], capture_output=True, text=True)
            print(result.stdout)
        else:
            print("Command not recognized.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python linux_commands.py <command> [<args>]")
    else:
        command = sys.argv[1]
        execute_command(command)

# fifo Queue implementation
import queue


def fifo_queue_demo():
    # Create a FIFO queue
    fifo_queue = queue.Queue()

    # Enqueue items
    print("Enqueuing items:")
    for i in range(5):
        fifo_queue.put(i)
        print(f"Enqueued: {i}")

    # Dequeue items
    print("\nDequeuing items:")
    while not fifo_queue.empty():
        item = fifo_queue.get()
        print(f"Dequeued: {item}")


if __name__ == "__main__":
    fifo_queue_demo()

