# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:41:35 2024

@author: wayne
"""

import json
import matplotlib.pyplot as plt  # Importing the plotting library

# Load the JSON file containing the data for the line graph
with open('lr_vs_arprc.json', 'r') as file:
    data = json.load(file)

# Extract the data for the x-axis (learning rate) and y-axis (average turns per set-rule change)
learning_rates = [item['learning_rate'] for item in data]
avg_turns_per_change = [item['avg_turns_per_change'] for item in data]

# Create the line graph
plt.plot(learning_rates, avg_turns_per_change, marker='o', linestyle='-', color='b', label='Learning Rate vs. Avg Turns/Change')

# Add labels and a title
plt.xlabel('Learning Rate')  # Label for the x-axis
plt.ylabel('Average Turns per Rule Change')  # Label for the y-axis
plt.title('Learning Rate vs. Average Turns per Rule Change')  # Title of the graph

# Add a legend to explain the line
plt.legend()

# Display the line graph
plt.show()
