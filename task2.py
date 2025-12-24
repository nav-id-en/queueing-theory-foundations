import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
mu_rate = 10
lambda_rate = 1.2 * mu_rate
capacity = 40
return_probability = 0.5
total_jobs = 100000

queues = [{"state": 0, "counter_denials": 0, "times": [0], "states": [0]} for _ in range(4)]
queue_a = {"state": 0, "times": [0], "states": [0]}
queue_b = {"state": 0, "times": [0], "states": [0]}
main_server = {"state": 0, "times": [0], "states": [0]}

time = 0
processed_jobs = 0

# Simulation
while processed_jobs < total_jobs:

    arrival_times = [np.random.exponential(1 / lambda_rate) for _ in range(4)]
    service_times = [np.random.exponential(1 / mu_rate) if q["state"] > 0 else float('inf') for q in queues]

    service_time_a = np.random.exponential(1 / (2 * mu_rate)) if queue_a["state"] > 0 else float('inf')
    service_time_b = np.random.exponential(1 / (2 * mu_rate)) if queue_b["state"] > 0 else float('inf')

    service_time_main = np.random.exponential(1 / (4 * mu_rate)) if main_server["state"] > 0 else float('inf')

    # Determine next event and its time
    next_event_time = min(arrival_times + service_times + [service_time_a, service_time_b, service_time_main])
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
        if random.random() < return_probability:
            if queues[queue_idx]["state"] < capacity:
                queues[queue_idx]["state"] += 1
        else:
            if queue_idx < 2:
                queue_a["state"] += 1
            else:
                queue_b["state"] += 1
        queues[queue_idx]["times"].append(time)
        queues[queue_idx]["states"].append(queues[queue_idx]["state"])

    elif next_event_time == service_time_a:
        queue_a["state"] -= 1
        main_server["state"] += 1
        queue_a["times"].append(time)
        queue_a["states"].append(queue_a["state"])

    elif next_event_time == service_time_b:
        queue_b["state"] -= 1
        main_server["state"] += 1
        queue_b["times"].append(time)
        queue_b["states"].append(queue_b["state"])

    elif next_event_time == service_time_main:
        main_server["state"] -= 1
        main_server["times"].append(time)
        main_server["states"].append(main_server["state"])


start_index = int(0.05 * len(queues[0]["states"]))
for i, q in enumerate(queues):
    denials_rate = q["counter_denials"] / total_jobs
    mean_state = np.mean(q["states"][start_index:])
    print(f"Queue {i + 1}: Denial rate = {denials_rate:.4f}, Average state = {mean_state:.4f}")


start_index_a = int(0.05 * len(queue_a["states"]))
start_index_b = int(0.05 * len(queue_b["states"]))
start_index_main = int(0.05 * len(main_server["states"]))

mean_state_a = np.mean(queue_a["states"][start_index_a:])
mean_state_b = np.mean(queue_b["states"][start_index_b:])
mean_state_main = np.mean(main_server["states"][start_index_main:])

print(f"Queue A: Average state = {mean_state_a:.4f}")
print(f"Queue B: Average state = {mean_state_b:.4f}")
print(f"Main Server: Average state = {mean_state_main:.4f}")


plt.figure(figsize=(12, 6))
for i, q in enumerate(queues):
    plt.step(q["times"], q["states"], where='post', label=f'Queue {i + 1}')
plt.axhline(y=capacity, color='r', linestyle='--', label='Capacity Limit')
plt.title('States of Individual Queues Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Customers')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.step(queue_a["times"], queue_a["states"], where='post', label='Queue A')
plt.step(queue_b["times"], queue_b["states"], where='post', label='Queue B')
plt.title('States of Intermediate Queues (A and B) Over Time')
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
