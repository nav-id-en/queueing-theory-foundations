import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
mu_rate = 1
lambda_rate = 9
capacity = 10
return_probability = 0.1
total_jobs = 100000

queues = [{"state": 0, "counter_denials": 0, "times": [0], "states": [0]} for _ in range(15)]
collecting_servers = [{"state": 0, "times": [0], "states": [0]} for _ in range(3)]
main_server = {"state": 0, "times": [0], "states": [0]}

time = 0
processed_jobs = 0
processed_by_main_server = 0

while processed_jobs < total_jobs:

    arrival_times = [np.random.exponential(1 / lambda_rate) for _ in range(15)]

    service_times = [np.random.exponential(1 / mu_rate) if q["state"] > 0 else float('inf') for q in queues]

    service_times_collecting = [np.random.exponential(1 / (5 * mu_rate)) if q["state"] > 0 else float('inf') for q in
                                collecting_servers]

    service_time_main = np.random.exponential(1 / (15 * mu_rate)) if main_server["state"] > 0 else float('inf')

    next_event_time = min(arrival_times + service_times + service_times_collecting + [service_time_main])
    time += next_event_time

    if next_event_time in arrival_times:

        queue_idx = arrival_times.index(next_event_time)
        processed_jobs += 1
        if queues[queue_idx]["state"] < capacity:
            queues[queue_idx]["state"] += 1
        else:
            queues[queue_idx]["counter_denials"] += 1
        queues[queue_idx]["times"].append(time)
        queues[queue_idx]["states"].append(queues[queue_idx]["state"])

    elif next_event_time in service_times:

        queue_idx = service_times.index(next_event_time)
        queues[queue_idx]["state"] -= 1

        collecting_server_idx = queue_idx // 5
        collecting_servers[collecting_server_idx]["state"] += 1


        if random.random() < return_probability:
            if queues[queue_idx]["state"] < capacity:
                queues[queue_idx]["state"] += 1

        queues[queue_idx]["times"].append(time)
        queues[queue_idx]["states"].append(queues[queue_idx]["state"])

    elif next_event_time in service_times_collecting:

        collecting_server_idx = service_times_collecting.index(next_event_time)
        collecting_servers[collecting_server_idx]["state"] -= 1
        main_server["state"] += 1
        processed_by_main_server += 1

        collecting_servers[collecting_server_idx]["times"].append(time)
        collecting_servers[collecting_server_idx]["states"].append(collecting_servers[collecting_server_idx]["state"])

    elif next_event_time == service_time_main:
        main_server["state"] -= 1
        main_server["times"].append(time)
        main_server["states"].append(main_server["state"])

throughput_main_server = processed_by_main_server / time
print(f"Throughput of Main Server: {throughput_main_server:.4f} jobs per unit time")

start_index = int(0.05 * len(queues[0]["states"]))
for i, q in enumerate(queues):
    denials_rate = q["counter_denials"] / total_jobs
    mean_state = np.mean(q["states"][start_index:])
    print(f"Edge Server {i + 1}: Denial rate = {denials_rate:.4f}, Average state = {mean_state:.4f}")

start_index_collecting = int(0.05 * len(collecting_servers[0]["states"]))
for i, q in enumerate(collecting_servers):
    mean_state = np.mean(q["states"][start_index_collecting:])
    print(f"Collecting Server {i + 1}: Average state = {mean_state:.4f}")

start_index_main = int(0.05 * len(main_server["states"]))
mean_state_main = np.mean(main_server["states"][start_index_main:])
print(f"Main Server: Average state = {mean_state_main:.4f}")

plt.figure(figsize=(12, 6))
for i, q in enumerate(queues):
    plt.step(q["times"], q["states"], where='post', label=f'Edge Server {i + 1}')
plt.axhline(y=capacity, color='r', linestyle='--', label='Capacity Limit')
plt.title('States of Edge Servers Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Customers')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
for i, q in enumerate(collecting_servers):
    plt.step(q["times"], q["states"], where='post', label=f'Collecting Server {i + 1}')
plt.title('States of Collecting Servers Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Customers')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.step(main_server["times"], main_server["states"], where='post', label='Main Server')
plt.title('State of Main Server Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Customers')
plt.legend()
plt.grid()
plt.show()
