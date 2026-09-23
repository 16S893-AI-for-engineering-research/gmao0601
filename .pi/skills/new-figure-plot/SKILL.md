---
name: new-figure-plot
description: Generates a Python script that produces a clean, paper-ready figure. Assists with plotting data from dat, csv, txt, xml or similar data files. Use when prompted to generate figures from existing data.
---

# New Figure Plot

> **Note:** Loading or reading this skill file — whether invoked implicitly, or explicitly via `/skill:new_figure_plot` — does not by itself indicate a desire to apply it immediately. Even when invoked with `/skill:`, do not immediately generate, overwrite, or run a plotting script; confirm the details (target data file, output location, axis labels, etc.) with the user first.

Generate a Python script that produces a publication-ready line plot figure from a data file using Matplotlib. The skill outputs a standalone `.py` script (not just an inline plot) so it can be reviewed, reused, and re-run by the user.

## Supported Input Formats

- `.csv` — comma-separated values
- `.dat` — whitespace or delimiter-separated values
- `.txt` — whitespace or delimiter-separated values
- `.xml` — parse relevant numeric fields/columns
- Similar plain-text tabular data formats

Inspect the file first to detect delimiter, header row, and column structure before writing the plotting script.

## Plot Style Requirements

- **Library:** Python with `matplotlib`
- **Font:** Helvetica, size 28, applied to axes labels, tick labels, title, and legend text
- **Colors:** Use Matplotlib's default color cycle (`plt.rcParams['axes.prop_cycle']`, i.e. the standard `C0`, `C1`, `C2`, ... colors) — do not override colors manually; let each line take the next color in the default cycle
- **Plot type:** Line plot (`plt.plot`), one line per data series/column
- **Legend:** Include a legend labeling each line (derive labels from column headers if available, otherwise use generic series names like `Series 1`, `Series 2`, etc.)
- **Axes labels:** Set x-axis and y-axis labels based on column headers/units if available in the data file; otherwise use generic labels
- **Margins:** Minimize whitespace/margins around the plot area — use tight layout and trim excess figure padding so the saved figure is compact
- **Output format:** Save the final figure as a `.jpeg` file (use `plt.savefig(..., format="jpeg", dpi=300)` or similar) in the same directory as the source data, or a location specified by the user

## Example Implementation Pattern

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Set global font
mpl.rcParams['font.family'] = 'Helvetica'
mpl.rcParams['font.size'] = 28

# Load data (adjust loader based on detected format)
data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
x = data[:, 0]
series = data[:, 1:]

fig, ax = plt.subplots(figsize=(10, 8))
n_lines = series.shape[1]
for i in range(n_lines):
    ax.plot(x, series[:, i], label=f'Series {i+1}', linewidth=2)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.legend()

# Minimize margins/whitespace
plt.tight_layout(pad=0.5)
plt.savefig('figure.jpeg', format='jpeg', dpi=300, bbox_inches='tight', pad_inches=0.05)
```

## Workflow

1. Read and inspect the input data file to determine delimiter, headers, and number of columns/series.
2. Write a standalone Python script (`.py` file) that:
   - Loads the data (e.g., via `numpy`, `pandas`, or `csv`/`xml` parsing as appropriate)
   - Applies the required Matplotlib styling (Helvetica font, size 28)
   - Plots each series as a line, letting Matplotlib's default color cycle assign colors
   - Includes a legend entry for each line
   - Labels axes based on available metadata/headers
   - Minimizes figure margins/whitespace (tight layout, trimmed padding on save)
   - Saves the figure as a `.jpeg` file
3. Save the generated script to a file (e.g., `plot_<data_filename>.py`) in the same directory as the source data, or a location specified by the user.
4. Run the script to confirm it executes without errors and produces the expected `.jpeg` output.
5. Confirm the script path and output figure path with the user.
