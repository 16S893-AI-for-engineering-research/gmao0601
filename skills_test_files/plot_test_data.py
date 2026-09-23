import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
import os

# Set global font
mpl.rcParams['font.family'] = 'Helvetica'
mpl.rcParams['font.size'] = 28

# Load data
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, 'test_data.csv')

with open(data_path, newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = [[float(v) for v in row] for row in reader]

data = np.array(rows)
x = data[:, 0]
series = data[:, 1:]
series_labels = header[1:]
x_label = header[0]

fig, ax = plt.subplots(figsize=(10, 8))
n_lines = series.shape[1]
for i in range(n_lines):
    ax.plot(x, series[:, i], label=series_labels[i], linewidth=2)

ax.set_xlabel(x_label)
ax.set_ylabel('Value')
ax.legend()

# Minimize margins/whitespace
plt.tight_layout(pad=0.5)

out_path = os.path.join(script_dir, 'test_data.jpeg')
plt.savefig(out_path, format='jpeg', dpi=300, bbox_inches='tight', pad_inches=0.05)
