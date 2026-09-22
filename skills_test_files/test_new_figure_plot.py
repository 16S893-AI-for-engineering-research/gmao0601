"""
Test script for the new_figure_plot skill.

Reads test_data.csv (time, number_of_pets, number_of_people) and generates
a paper-ready line plot figure following the skill's style requirements:

- Matplotlib, Helvetica font, size 28
- Default Matplotlib color cycle for lines
- Line plot with legend
- Minimal margins/whitespace
- Saved as JPEG

Usage:
    python test_new_figure_plot.py
"""

import csv

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

INPUT_FILE = "test_data.csv"
OUTPUT_FILE = "test_figure.jpeg"

# --- Style setup ---
mpl.rcParams["font.family"] = "Helvetica"
mpl.rcParams["font.size"] = 28

# --- Load data ---
with open(INPUT_FILE, newline="") as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = [list(map(float, row)) for row in reader]

data = np.array(rows)
x = data[:, 0]
series = data[:, 1:]
labels = headers[1:]

# --- Plot (uses Matplotlib's default color cycle) ---
fig, ax = plt.subplots(figsize=(10, 8))
n_lines = series.shape[1]
for i in range(n_lines):
    ax.plot(x, series[:, i], label=labels[i], linewidth=2)

ax.set_xlabel(headers[0].replace("_", " ").title())
ax.set_ylabel("Count")
ax.legend()

# --- Minimize margins/whitespace ---
plt.tight_layout(pad=0.5)
plt.savefig(OUTPUT_FILE, format="jpeg", dpi=300, bbox_inches="tight", pad_inches=0.05)

print(f"Saved figure to {OUTPUT_FILE}")
