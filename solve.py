import numpy as np
from scipy.integrate import solve_ivp
import pandas as pd


video_duration = 13.21 # video duration in seconds
frame_count = 396
# Parameters
g = 9.81  # gravitational acceleration (m/s^2)
L = 41.8 / 100   # length of the pendulum (m)
save_interval = video_duration / frame_count
high_resolution_interval = save_interval / 100  # Small time step for higher resolution (10 ms)

# Define the system of ODEs
def pendulum(t, y):
    theta, omega = y  # unpack current values of angle and angular velocity
    dtheta_dt = omega
    domega_dt = - (g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Initial conditions
theta_0 = np.radians(44.172)  # initial angle (in radians)
omega_0 = 0.0             # initial angular velocity (rad/s)
y0 = [theta_0, omega_0]   # initial state

# Time span for the solution
t_span = (0, 10)  # 10 seconds
t_eval_high_res = np.arange(0, 10, high_resolution_interval)  # High resolution time points

# Solve the system with a higher resolution
solution = solve_ivp(pendulum, t_span, y0, t_eval=t_eval_high_res, method='RK45')

# Extract results
t = solution.t
theta = solution.y[0]
omega = solution.y[1]

# Select data at intervals of save_interval
save_indices = np.arange(0, len(t), int(save_interval / high_resolution_interval))
frames = np.arange(0, len(save_indices))
t_save = t[save_indices]
theta_save = theta[save_indices]
omega_save = omega[save_indices]

# Save the results to a CSV file
data = {
    "Frame": frames,
    "Time (s)": t_save,
    "Acceleration (cm/s^2)": -g*100*np.sin(theta_save),
    "Velocity (cm/s)": 100*L*omega_save
}
df = pd.DataFrame(data)

# Specify the file path
file_path = "pendulum_.csv"
df.to_csv(file_path, index=False)
