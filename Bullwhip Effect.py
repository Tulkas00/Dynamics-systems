import numpy as np
import matplotlib.pyplot as plt

# Parameters
time_steps = 50  # Simulation time steps
stages = ['Customer', 'Retailer', 'Wholesaler', 'Distributor', 'Manufacturer']
demand_variation = 0.1  # Variability in customer demand
lead_time = 2  # Delay in order fulfillment
inventory_policy = 1.5  # Safety stock multiplier

# Initialize demand and orders
customer_demand = np.ones(time_steps) + demand_variation * np.sin(np.linspace(0, 5 * np.pi, time_steps))
orders = {stage: np.zeros(time_steps) for stage in stages}
inventory = {stage: np.zeros(time_steps) for stage in stages}

# Set initial conditions
orders['Customer'] = customer_demand
for stage in stages:
    inventory[stage][0] = 50  # Initial inventory

# Simulate the supply chain
for t in range(1, time_steps):
    for i, stage in enumerate(stages):
        if stage == 'Customer':
            continue
        # Get demand from the downstream stage
        downstream_demand = orders[stages[i - 1]][t - lead_time] if t - lead_time >= 0 else 0

        # Inventory check and order placement
        if inventory[stage][t - 1] < downstream_demand:
            order = downstream_demand * inventory_policy
        else:
            order = downstream_demand

        orders[stage][t] = order

        # Update inventory
        inventory[stage][t] = inventory[stage][t - 1] + orders[stage][t - lead_time] - downstream_demand if t - lead_time >= 0 else inventory[stage][t - 1] - downstream_demand

# Plot the results
plt.figure(figsize=(12, 8))

# Plot customer demand
plt.plot(customer_demand, label="Customer Demand", linewidth=2)

# Plot orders for each stage
for stage in stages:
    plt.plot(orders[stage], label=f"{stage} Orders", linestyle="--")

plt.title("Bullwhip Effect Simulation", fontsize=16)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Orders", fontsize=12)
plt.legend()
plt.grid()
plt.show()
