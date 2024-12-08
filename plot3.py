import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to apply moving average smoothing
def moving_average(data, window_size=5):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Load the CSV file into a DataFrame
data = pd.read_csv("table5.csv")

# Extract the columns for plotting
x = data.iloc[:, 0]  # First column (x-axis)
y1 = data.iloc[:, 1]  # Second column (y-axis)
y2 = data.iloc[:, 2]  # Third column (y-axis)

# Apply moving average smoothing to y1 and y2 (with a window size of 5)
y1_smooth = moving_average(y1, window_size=5)
y2_smooth = moving_average(y2, window_size=5)

# Adjust x-axis to match the length of the smoothed data
x_smooth = x.iloc[len(x) - len(y1_smooth):]  # Trim x-axis to match smoothed data length

# Plot the smoothed data
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y1_smooth, marker='o', linestyle='-', label=data.columns[1], color='blue')
plt.plot(x_smooth, y2_smooth, marker='s', linestyle='--', label=data.columns[2], color='orange')

# Add labels, title, legend, and grid
plt.title(f"Smoothed Plot of {data.columns[1]} and {data.columns[2]} vs {data.columns[0]}")
plt.xlabel(data.columns[0])  # Name of the first column
plt.ylabel('Acceleration (cm/s^2)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()