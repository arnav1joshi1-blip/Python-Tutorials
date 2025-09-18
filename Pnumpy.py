import numpy as np

# Project 1
data1 = np.loadtxt("sensor_data/sensor.csv", delimiter=",", skiprows=1)

avg_vals = np.mean(data1, axis=0)
min_vals = np.min(data1, axis=0)
max_vals = np.max(data1, axis=0)

temperature_col = data1[:, 0]
time_index = np.argmax(temperature_col)

battery_col = data1[:, 2]
mask1 = battery_col < 30
battery_low_count = np.sum(mask1)

out1 = np.array([avg_vals, min_vals, max_vals])
np.savetxt("sensor_data/processed.csv", out1, delimiter=",")
np.savetxt("sensor_data/temp_high_time.csv", np.array([time_index]), delimiter=",")
np.savetxt("sensor_data/battery_low_count.csv", np.array([battery_low_count]), delimiter=",")

# Project 2
data2 = np.loadtxt("robot_path/path.csv", delimiter=",", skiprows=1)

diffs = np.diff(data2, axis=0)
dist_step = np.linalg.norm(diffs, axis=1)
total_dist = np.sum(dist_step)

origin = np.array([0, 0])
dist_from_origin = np.linalg.norm(data2 - origin, axis=1)
farthest_index = np.argmax(dist_from_origin)
farthest_point = data2[farthest_index]

unique_positions, counts = np.unique(data2, axis=0, return_counts=True)
revisit_mask = counts > 1
revisited = np.any(revisit_mask)

out2 = np.array([total_dist])
np.savetxt("robot_path/total_distance.csv", out2, delimiter=",")
np.savetxt("robot_path/farthest_point.csv", farthest_point.reshape(1, 2), delimiter=",")
np.savetxt("robot_path/revisited.csv", np.array([revisited]), delimiter=",")