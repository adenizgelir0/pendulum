import pandas as pd
import matplotlib.pyplot as plt
import sys

# Check if the filename is provided as a command-line argument

# Load the CSV file into a DataFrame
data = pd.read_csv("table4.csv")

# Extract the columns for plotting
x = data.iloc[:, 0]  # First column (x-axis)
y1 = data.iloc[:, 1]  # Second column (y-axis)
y2 = data.iloc[:, 2]  # Third column (y-axis)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(x, y1, marker='o', linestyle='-', label=data.columns[1], color='blue')
plt.plot(x, y2, marker='s', linestyle='--', label=data.columns[2], color='orange')

# Add labels, title, legend, and grid
plt.title(f"Plot of {data.columns[1]} and {data.columns[2]} vs {data.columns[0]}")
plt.xlabel(data.columns[0])  # Name of the first column
plt.ylabel('Velocity(cm/s)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()