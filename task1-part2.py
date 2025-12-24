import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_rate_set = np.linspace(3, 15, 1000)
mu_rate = 9
capacity = 40
return_probability = 0.5
simulation_time = 1000


denials_rate = []
mean_state = []


for lambda_rate in lambda_rate_set:
    time = 0
    state = 0
    counter_getrid = 0
    states = [state]


    while time < simulation_time:

        arrival_time = np.random.exponential(1 / lambda_rate)
        service_time = np.random.exponential(1 / mu_rate) if state > 0 else float('inf')


        if arrival_time < service_time:

            time += arrival_time
            if state < capacity:
                state += 1
            else:
                counter_getrid += 1
        else:

            time += service_time
            state -= 1


            if np.random.random() < return_probability:
                if state < capacity:
                    state += 1

        # Track queue state
        states.append(state)

    # Calculate metrics for this lambda_rate
    denials_rate.append(counter_getrid / simulation_time)  # Denial rate
    mean_state.append(np.mean(states))  # Average queue size

slope_deny, intercept_deny = np.polyfit(lambda_rate_set, denials_rate, 1)
slope_mean, intercept_mean = np.polyfit(lambda_rate_set, mean_state, 1)

print(f"Slope_deny: {slope_deny}")
print(f"Intercept_deny: {intercept_deny}")
print(f"Slope_mean: {slope_mean}")
print(f"Intercept_mean: {intercept_mean}")

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(lambda_rate_set, denials_rate, label='Denial Rate')
plt.title('Denial Rate vs Arrival Rate (λ)')
plt.xlabel('Arrival Rate (λ)')
plt.ylabel('Denial Rate')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(lambda_rate_set, mean_state, label='Mean Queue Size')
plt.title('Mean Queue Size vs Arrival Rate (λ)')
plt.xlabel('Arrival Rate (λ)')
plt.ylabel('Mean Queue Size')
plt.legend()
plt.grid()
plt.show()


