import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
lambda_rate = 10
capacity = 10

total_jobs = 1000
mu_values = np.linspace(0.1, 6, 60)

A = 1
B = 1


cost_values = []
denials_list = []
returns_list = []


for mu_rate in mu_values:
    return_probability = 2*((1/(1+np.exp(-0.25*mu_rate)))-0.5)
    time = 0
    processed_jobs = 0
    processed_by_main_server = 0
    total_denials = 0
    total_returns = 0

    queues = [{"state": 0, "counter_denials": 0, "counter_returns": 0} for _ in range(15)]

    collecting_servers = [{"state": 0} for _ in range(3)]


    main_server = {"state": 0}


    while processed_jobs < total_jobs:

        arrival_times = [np.random.exponential(1 / lambda_rate) for _ in range(15)]


        service_times = [np.random.exponential(1 / mu_rate) if q["state"] > 0 else float('inf') for q in queues]


        service_times_collecting = [np.random.exponential(1 / (5 * mu_rate)) if q["state"] > 0 else float('inf') for q
                                    in collecting_servers]


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
                total_denials += 1

        elif next_event_time in service_times:
            queue_idx = service_times.index(next_event_time)
            queues[queue_idx]["state"] -= 1

            collecting_server_idx = queue_idx // 5
            collecting_servers[collecting_server_idx]["state"] += 1

            if random.random() < return_probability:
                if queues[queue_idx]["state"] < capacity:
                    queues[queue_idx]["state"] += 1
                    total_returns += 1

        elif next_event_time in service_times_collecting:

            collecting_server_idx = service_times_collecting.index(next_event_time)
            collecting_servers[collecting_server_idx]["state"] -= 1
            main_server["state"] += 1
            processed_by_main_server += 1

        elif next_event_time == service_time_main:
            main_server["state"] -= 1

    cost_function = A * total_denials + B * total_returns
    cost_values.append(cost_function)
    denials_list.append(total_denials)
    returns_list.append(total_returns)



def plot_with_regression(x, y, title, ylabel, color, marker):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, marker=marker, color=color, label='Data Points')

    poly_coeffs = np.polyfit(x, y, 6)
    poly_eq = np.poly1d(poly_coeffs)
    x_smooth = np.linspace(min(x), max(x), 100)
    y_smooth = poly_eq(x_smooth)

    plt.plot(x_smooth, y_smooth, color='black', linestyle='--', label='Regression Curve')

    plt.xlabel('Service Rate (mu)')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()



plot_with_regression(mu_values, denials_list, 'Denied Jobs vs. Service Rate (mu)', 'Denied Jobs', 'red', 'o')


plot_with_regression(mu_values, returns_list, 'Returned Jobs vs. Service Rate (mu)', 'Returned Jobs', 'blue', 's')


plot_with_regression(mu_values, cost_values, 'Cost Function vs. Service Rate (mu)', 'Cost Function', 'green', '^')
