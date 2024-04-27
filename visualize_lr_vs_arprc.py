# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:41:35 2024

@author: wayne
"""

import json
import matplotlib.pyplot as plt  # Importing the plotting library

# Load the JSON file containing the data for the line graph
with open('lr_vs_arprc.json', 'r') as file:
    data = json.load(file)  # Load the JSON data

# Extract x-axis and y-axis data
learning_rates = [item['learning_rate'] for item in data]
avg_turns_per_change = [item['avg_turns_per_change'] for item in data]

# Create the line graph with appropriate dimensions
plt.figure(figsize=(10, 6))  # Set the figure size (width, height) in inches

plt.plot(learning_rates, avg_turns_per_change, marker='o', linestyle='-', color='b', label='Learning Rate vs. Avg Turns/Change')

# Add labels and a title
plt.xlabel('Learning Rate')  # Label for the x-axis
plt.ylabel('Average Turns per Set-Rule Change')  # Label for the y-axis
plt.title('Learning Rate vs. Average Turns per Set-Rule Change')  # Title for the graph

# Add a legend to explain the line
plt.legend()

# Save the graph to a file with high resolution for PowerPoint
output_file = 'learning_rate_vs_avg_turns_per_change.png'  # Output file name
plt.savefig(output_file, bbox_inches='tight', dpi=300)  # Save with high resolution and tight bounding box

# Display the line graph
plt.show()  # Optional to display after saving
