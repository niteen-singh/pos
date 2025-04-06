# CPU Scheduling Algorithms
import sys
import os
import shutil




# 1. FCFS (First-Come, First-Served) Algorithm
# FCFS
# Process : [arrival_time, burst_time, pid]
def fcfs(process_list):
    t = 0
    gantt = []
    completed = {}
    process_list.sort()
    while process_list != []:
        if process_list[0][0] > t:
            t += 1
            gantt.append("Idle")
            continue
        else:
            process = process_list.pop(0)
            gantt.append(process[2])
            t += process[1]
            pid = process[2]
            ct = t
            tt = ct - process[0]
            wt = tt - process[1]
            completed[pid] = [ct, tt, wt]
    print(gantt)
    print(completed)


if __name__ == "__main__":
    process_list = [[2, 6, "p1"], [5, 2, "p2"], [1, 8, "p3"], [0, 3, "p4"], [4, 4, "p5"]]
    fcfs(process_list)






# 2. SJF (Shortest Job First) Non-Preemptive Algorithm
# SJF (Non pre-emptive)
# Process: [burst_time, arrival_time, pid]

def sjf(process_list):
    t = 0
    gantt = []
    completed = {}

    while process_list != []:
        available = []
        for p in process_list:
            if p[1] <= t:
                available.append(p)
        # No processes available
        if available == []:
            t += 1
            gantt.append("Idle")
            continue
        else:
            available.sort()
            process = available[0]
            # Service the process
            burst_time = process[0]
            pid = process[2]
            arrival_time = process[1]
            t += burst_time
            gantt.append(pid)
            ct = t
            tt = ct - arrival_time
            wt = tt - burst_time
            process_list.remove(process)
            completed[pid] = [ct, tt, wt]
    print(gantt)
    print(completed)


if __name__ == "__main__":
    process_list = [[6, 2, "p1"], [2, 5, "p2"], [8, 1, "p3"], [3, 0, "p4"], [4, 4, "p5"]]
    sjf(process_list)





# 3. SJF (Shortest Job First) Preemptive Algorithm
# SRTF / SJF Pre-emptive

# Process: [burst_time, arrival_time, pid]

def srtf(process_list):
    gantt = []
    burst_times = {}
    for i in process_list:
        burst_times[i[2]] = i[0]
    completion = {}
    t = 0
    while process_list != []:

        available = []
        for p in process_list:
            if p[1] <= t:
                available.append(p)

        if available == []:
            t += 1
            gantt.append("Idle")
            continue
        else:
            available.sort()
            process = available[0]
            copy_process = available.pop(0)
            t += 1
            gantt.append(process[2])
            # updating the burst time of the process
            process[0] -= 1
            process_list.remove(copy_process)
            if process[0] == 0:
                # this is where we have to note down our completion times
                process_name = process[2]
                arrival_time = process[1]
                burst_time = burst_times[process_name]
                ct = t
                tt = ct - process[1]
                wt = tt - burst_time
                completion[process_name] = [ct, tt, wt]
                continue
            else:
                process_list.append(process)

    print(gantt)
    print(completion)


if __name__ == "__main__":
    process_list = [[6, 2, "p1"], [2, 5, "p2"], [8, 1, "p3"], [3, 0, "p4"], [4, 4, "p5"]]
    srtf(process_list)






# 4. Round Robin Algorithm
# Round Robin CPU Scheduling Algorithm
# input: process list, time quanta
# Process: [Arrival time, burst time, pid]

def round_robin(process_list, time_quanta):
    t = 0
    gantt = []
    completed = {}
    # sort the processes wrt at
    process_list.sort()
    burst_times = {}
    for p in process_list:
        pid = p[2]
        burst_time = p[1]
        burst_times[pid] = burst_time
    while process_list != []:
        available = []
        for p in process_list:
            at = p[0]
            if p[0] <= t:
                available.append(p)
        # boundary condition 1
        if available == []:
            gantt.append("Idle")
            t += 1
            continue
        else:
            process = available[0]
            # Service this process now
            gantt.append(process[2])
            # remove the process
            process_list.remove(process)
            # Update the burst time
            rem_burst = process[1]
            if rem_burst <= time_quanta:
                t += rem_burst
                ct = t
                pid = process[2]
                arrival_time = process[0]
                burst_time = burst_times[pid]
                tt = ct - arrival_time
                wt = tt - burst_time
                completed[process[2]] = [ct, tt, wt]
                continue
            else:
                t += time_quanta
                process[1] -= time_quanta
                process_list.append(process)
    print(gantt)
    print(completed)


if __name__ == "__main__":
    process_list = [[2, 6, "p1"], [5, 2, "p2"], [1, 8, "p3"], [0, 3, "p4"], [4, 4, "p5"]]
    time_quanta = 2
    round_robin(process_list, time_quanta)





# 5. Priority (Non-Preemptive) Algorithm
# Priority CPU scheduling
# Non pre-emptive

# Process : [Priority, pid, bursttime, arrival time]

def priority(process_list):
    gantt = []
    t = 0
    completed = {}
    while process_list != []:
        available = []
        for p in process_list:
            arrival_time = p[3]
            if arrival_time <= t:
                available.append(p)

        if available == []:
            gantt.append("Idle")
            t += 1
            continue
        else:
            available.sort()
            process = available[0]
            # service the process
            # 1. remove the process
            process_list.remove(process)
            # 2. add to gantt chart
            pid = process[1]
            gantt.append(pid)
            # 3. update the time
            burst_time = process[2]
            t += burst_time
            # create an entry in the completed dictionary
            # Calculate ct, tt, wt
            ct = t
            arrival_time = process[3]
            tt = ct - arrival_time
            wt = tt - burst_time
            completed[pid] = [ct, tt, wt]

    print(gantt)
    print(completed)


if __name__ == "__main__":
    process_list = [[5, "p1", 6, 2], [4, "p2", 2, 5], [1, "p3", 8, 1], [2, "p4", 3, 0], [3, "p5", 4, 4]]
    priority(process_list)





# 6. Priority (Preemptive) Algorithm
# Priority premptive
# Process = [priority, pid, burst_time, arrival_time]

def priority(process_list):
    t = 0
    gantt = []
    completed = {}
    burst_times = {}
    for p in process_list:
        burst_times[p[1]] = p[2]
    while process_list != []:
        # finding the available processes
        available = []
        for p in process_list:
            arrival_time = p[3]
            if arrival_time <= t:
                available.append(p)
        if available == []:
            gantt.append("Idle")
            t += 1
            continue
        else:
            available.sort()
            process = available[0]
            gantt.append(process[1])
            t += 1
            process_list.remove(process)
            # updating the bursttime
            process[2] -= 1
            # boundary condition if process is completed
            if process[2] == 0:
                # completed
                pid = process[1]
                arrival_time = process[3]
                burst_time = burst_times[pid]
                ct = t
                tt = ct - arrival_time
                wt = tt - burst_time
                completed[pid] = [ct, tt, wt]
                continue
            else:
                process_list.append(process)
    print(gantt)
    print(completed)


if __name__ == "__main__":
    process_list = [[5, "p1", 6, 2], [2, "p2", 2, 5], [4, "p3", 8, 1], [1, "p4", 3, 0], [3, "p5", 4, 4]]
    priority(process_list)






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

