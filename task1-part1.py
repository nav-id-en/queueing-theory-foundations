import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
lambda_rate = 4
mu_rate = 9
capacity = 40
return_probability = 0.5
simulation_time = 1000

time = 0
state = 0
times = [time]
states = [state]
counter_getrid = 0
denials_rate = []
mean_state = []




while time < simulation_time:
    # Calculate next arrival and service times
    arrival_time = np.random.exponential(1 / lambda_rate)
    service_time = np.random.exponential(1 / mu_rate) if state > 0 else float('inf')
    #next event
    if arrival_time < service_time:
        # Arrival
        time += arrival_time
        if state < capacity:
            state += 1
        else:
            counter_getrid += 1
    else:
        # departure
        time += service_time
        state -= 1
        # Check if the customer returns
        if random.random() < return_probability:
            if state < capacity:
                state += 1
    times.append(time)
    states.append(state)
denials_rate = (counter_getrid / simulation_time)
mean_state = np.mean(states)

print('the rate of denials because the que is full equals to :' , denials_rate)
print('the Expectation of number of jobs in que :' , mean_state)

plt.figure(figsize=(10, 6))
plt.step(times, states, where='post', label='Queue State')
plt.axhline(y=capacity, color='r', linestyle='--', label='Queue Capacity')
plt.title('Queue State Over Time with Returning Customers')
plt.xlabel('Time')
plt.ylabel('Number of Customers in the System')
plt.legend()
plt.grid()
plt.show()
