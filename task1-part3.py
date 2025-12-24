import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
mu_rate = 10  # Rate of service
lambda_rate = 2 * mu_rate  # Rate of arrivals

capacity = 40  # Maximum queue capacity
return_probability = 0.5  # Probability of a customer returning
total_jobs = 100000  # Total number of jobs to process

# Initialize variables
time = 0
state = 0  # Current queue size
times = [time]
states = [state]
counter_getrid = 0  # Count of denied arrivals
processed_jobs = 0  # Count of total jobs processed (arrivals)
counter_getrid_set = [counter_getrid]

# Simulation loop
while processed_jobs < total_jobs:
    # Calculate next arrival and service times
    arrival_time = np.random.exponential(1 / lambda_rate)
    service_time = np.random.exponential(1 / mu_rate) if state > 0 else float('inf')

    # Determine the next event
    if arrival_time < service_time:
        # Arrival event
        time += arrival_time
        processed_jobs += 1  # Increment job count
        if state < capacity:
            state += 1  # Add to the queue
        else:
            counter_getrid += 1  # Queue full, increment denial counter
    else:
        # Departure event
        time += service_time
        state -= 1  # Remove a customer from the queue

        # Check if the customer returns
        if random.random() < return_probability:
            if state < capacity:
                state += 1  # Re-add to the queue if capacity allows

    # Track queue state
    times.append(time)
    states.append(state)
    counter_getrid_set.append(counter_getrid)
# Calculate metrics
denials_rate = counter_getrid / total_jobs  # Denial rate
mean_state = np.mean(states)  # Average queue size

# Output results
print('The rate of denials because the queue is full equals to:', denials_rate)
print('The expectation of the number of jobs in the queue:', mean_state)

# Plot results
plt.figure(figsize=(10, 6))
plt.step(times, states, where='post', label='Queue State')
plt.axhline(y=capacity, color='r', linestyle='--', label='Queue Capacity')
plt.title('Queue State Over Time with Returning Customers')
plt.xlabel('Time')
plt.ylabel('Number of Customers in the System')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.step(times, counter_getrid_set, where='post', label='Queue State')
plt.title('denials vs time')
plt.xlabel('Time')
plt.ylabel('Number of denials comulative')
plt.legend()
plt.grid()
plt.show()
